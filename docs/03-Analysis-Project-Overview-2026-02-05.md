# Phân Tích Toàn Diện Dự Án Auto M Machine

**Ngày:** 2026-02-05  
**Phiên bản:** 1.0  
**Trạng thái:** ✅ Phân tích hoàn thành

---

## 1. Tổng Quan Dự Án

### 1.1. Mục Tiêu
> **AI Content Revenue OS** - Hệ thống tự động tạo và phân phối nội dung video đa nền tảng với affiliate marketing.

**Mô hình hoạt động:**
```
Start → Tạo ý tưởng → Viết script → Voice/Sub → Render video → 
Upload đa nền tảng → Gắn affiliate → Đo lường → Tối ưu → Nhân bản
```

### 1.2. Nguyên Tắc Thiết Kế
| Nguyên tắc | Mô tả |
|------------|-------|
| **Compliance-first** | Tuân thủ chính sách YouTube/Facebook/TikTok |
| **Idempotent** | Chạy lại không tạo trùng (unique keys, upsert) |
| **Observability** | Log đầy đủ, biết lỗi ở đâu |
| **Human-like** | Có jitter, rate limit, không spam |
| **Modular** | Thay LLM/TTS/ASR dễ dàng |
| **Scale by queue** | Mọi thứ chạy theo job queue |

---

## 2. Kiến Trúc Hệ Thống

### 2.1. Stack Công Nghệ

```
┌─────────────────────────────────────────────────────────────────┐
│                         n8n Orchestrator                        │
│              (Scheduler → Render → Publish → Metrics)           │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼─────────────────────┐
        ▼                    ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  PostgreSQL   │    │     Redis     │    │   FFmpeg      │
│  (DB chính)   │    │   (Cache)     │    │  (Render)     │
└───────────────┘    └───────────────┘    └───────────────┘
        │                                          │
        ▼                                          ▼
┌───────────────┐                         ┌───────────────┐
│   Tracker     │                         │ Google Drive  │
│  (FastAPI)    │                         │  (Storage)    │
└───────────────┘                         └───────────────┘
```

### 2.2. Docker Services

| Service | Image | Port | Mục đích |
|---------|-------|------|----------|
| `postgres` | postgres:16 | 5432 | Database chính |
| `redis` | redis:7 | 6379 | Cache (optional) |
| `n8n` | n8nio/n8n:latest | 5678 | Orchestrator |
| `tracker` | Custom FastAPI | 8000 | Affiliate tracking |

---

## 3. Database Schema

### 3.1. Tổng Quan Tables (11 tables)

| Table | Mục đích | Quan hệ |
|-------|----------|---------|
| `render_jobs` | Queue render video | Standalone |
| `publish_queue` | Queue publish video | → videos |
| `policy_profiles` | Profile chính sách | Standalone |
| `brand_profiles` | Thiết lập brand/subtitle | → campaign_branding |
| `outro_profiles` | Thiết lập outro video | → campaign_branding |
| `campaign_branding` | Config brand per campaign | → brand_profiles, outro_profiles |
| `affiliate_links` | Links affiliate | → campaign, video |
| `affiliate_clicks` | Log click tracking | → affiliate_links |
| `affiliate_conversions` | Log conversions | → affiliate_links |
| `rate_limits` | Token bucket rate limit | Standalone |
| `retry_log` | Log retry/errors | Standalone |

### 3.2. Default Brand Profiles

| Slug | Font | Subtitle Size | Outro |
|------|------|---------------|-------|
| `calm` | Montserrat | 44 | outro_calm |
| `strong` | Oswald | 50 | outro_strong |
| `minimal` | Inter | 42 | outro_minimal |

---

## 4. Workflows n8n

### 4.1. Pipeline Chính

```
WF-SCHEDULER → WF-RENDER → WF-PUBLISH → WF-METRICS-OPTIMIZE
     │              │            │               │
     ▼              ▼            ▼               ▼
 Tạo jobs     Render video   Upload YT/FB    Lấy stats
              + subtitles    + comment/pin   + tối ưu
```

### 4.2. Chi Tiết Workflows

| Workflow | Size | Chức năng |
|----------|------|-----------|
| `WF-SCHEDULER-PROD.json` | 3.3KB | Đọc campaigns → tạo render_jobs |
| `WF-RENDER-PROD.json` | 10.2KB | Lấy job → compliance → render → upload Drive |
| `WF-PUBLISH-PROD.json` | 6.2KB | Download → upload platforms → comment |
| `WF-METRICS-OPTIMIZE-PROD.json` | 2KB | Lấy stats → tính score → điều chỉnh |

---

## 5. Video Render Pipeline

### 5.1. render.sh Capabilities (222 dòng)

| Feature | Mô tả |
|---------|-------|
| **Auto Aspect** | 9:16 (Shorts), 16:9 (YouTube), 1:1 (Square) |
| **Watermark** | Dynamic drift (chống reuse) |
| **Subtitles** | Burn-in với 3 preset styles |
| **Outro** | Auto/Manual với random duration jitter |
| **Audio** | Loudness normalize -14 LUFS |

### 5.2. Supported Platforms

| Platform | Aspect | Resolution |
|----------|--------|------------|
| YouTube Shorts | 9:16 | 1080x1920 |
| Facebook Reels | 9:16 | 1080x1920 |
| TikTok | 9:16 | 1080x1920 |
| Instagram Reels | 9:16 | 1080x1920 |
| YouTube Long | 16:9 | 1920x1080 |
| Square | 1:1 | 1080x1080 |

---

## 6. Policy & Compliance Engine

### 6.1. Hard Blocks (Cấm tuyệt đối)

- Medical claims, diagnosis, treatment
- Financial guarantees/promises
- Hate/Violence/Sexual content
- Political persuasion
- Impersonation

### 6.2. Blocklist Keywords

```
EN: "cure instantly", "guaranteed income", "get rich quick", "miracle cure"
VI: "chữa khỏi 100%", "đảm bảo kiếm tiền", "làm giàu nhanh", "cam kết khỏi bệnh"
```

### 6.3. Platform Rate Limits

| Platform | Comment/Hour | Posts/Day |
|----------|--------------|-----------|
| YouTube Shorts | 20 | 120 |
| Facebook Reels | 15 | 80 |
| TikTok | 10 | 60 |

---

## 7. Affiliate System

### 7.1. Tracker Service (FastAPI)

```
/r/{code}      → Redirect + log click
/postback/{network} → Nhận conversion postback
```

### 7.2. Link Modes

| Mode | Mô tả |
|------|-------|
| `bio` | Link trong bio profile |
| `comment` | Link trong comment |
| `pin` | Link trong pinned comment |
| `both` | Bio + Comment/Pin |

---

## 8. Đánh Giá Trạng Thái Dự Án

### 8.1. Hoàn Thiện

| Component | Trạng thái | Chi tiết |
|-----------|------------|----------|
| Docker Stack | ✅ 100% | Postgres, Redis, n8n, Tracker |
| Database Schema | ✅ 100% | 11 tables, indexes |
| Render Pipeline | ✅ 100% | FFmpeg, 3 brand presets |
| Policy Engine | ✅ 100% | Blocklist, rate limits |
| n8n Workflows | ⚠️ 80% | Có skeleton, cần customize |
| Tracker Service | ✅ 100% | FastAPI hoàn chỉnh |

### 8.2. Cần Hoàn Thiện (Theo MASTER_PLAN)

| Feature | Ưu tiên | Mô tả |
|---------|---------|-------|
| TTS/Sub per-video | 🔴 Cao | Generate voice theo script |
| Facebook upload thật | 🔴 Cao | Hiện tại là skeleton |
| Auto trend discovery | 🟡 Trung bình | Tìm niche/topic tự động |
| A/B testing hook | 🟢 Thấp | Test 3 variants per script |

---

## 9. Cấu Trúc Thư Mục Hoàn Chỉnh

```
Auto M Machine/
├── .agent/                    # Kit configuration (229MB)
│   ├── agents/               # 40 agents
│   ├── skills/               # 84 skills
│   ├── workflows/            # 28+ workflows
│   └── config.json           # Kit config (đã tối ưu)
├── GEMINI.md                 # Kit instructions
├── README.md                 # Project README
├── docs/                     # Tài liệu dự án
│   ├── 00-Documentation-Guidelines-2026-02-05.md
│   ├── 01-Analysis-Kit-Evaluation-2026-02-05.md
│   ├── 02-Analysis-Kit-Deep-Improvement-2026-02-05.md
│   ├── 03-Analysis-Project-Overview-2026-02-05.md (file này)
│   └── templates/            # Template docs
├── plans/                    # Kế hoạch triển khai
│   └── reports/
└── ai-content-revenue-os-production/
    ├── MASTER_PLAN.md        # Tài liệu gốc (309 dòng)
    ├── README.md             # Hướng dẫn deploy
    ├── docker-compose.yml    # Docker stack
    ├── n8n/                  # 4 workflow files
    │   ├── WF-SCHEDULER-PROD.json
    │   ├── WF-RENDER-PROD.json
    │   ├── WF-PUBLISH-PROD.json
    │   └── WF-METRICS-OPTIMIZE-PROD.json
    ├── policy/               # Compliance rules
    │   └── policy_profiles.json
    ├── scripts/              # Render scripts
    │   └── render.sh
    ├── services/             # Backend services
    │   └── tracker/
    │       ├── app.py
    │       └── Dockerfile
    └── sql/                  # Database schema
        └── production.sql
```

---

## 10. Khuyến Nghị Tiếp Theo

### Ưu Tiên Cao
1. **Hoàn thiện TTS pipeline** - Generate voice từ script
2. **Implement Facebook upload** - Thay skeleton bằng real upload
3. **Test deployment** - Deploy Docker stack và verify

### Ưu Tiên Trung Bình
4. **Customize n8n workflows** - Điều chỉnh theo campaigns thực tế
5. **Add campaigns table** - Hiện schema thiếu bảng campaigns gốc
6. **Setup credentials** - YouTube OAuth2, Google Drive, DB

### Ưu Tiên Thấp
7. **Auto trend discovery** - Tìm topics tự động
8. **A/B testing** - Test multiple hook variants

---

## 11. Kết Luận

> **Dự án AI Content Revenue OS là hệ thống automation hoàn chỉnh cho content marketing đa nền tảng.**

**Điểm mạnh:**
- ✅ Kiến trúc modular, scale được
- ✅ Compliance-first approach
- ✅ Full pipeline từ A-Z
- ✅ Multi-platform support

**Cần cải thiện:**
- ⚠️ Facebook upload còn skeleton
- ⚠️ TTS chưa hoàn thiện
- ⚠️ Thiếu bảng campaigns gốc

**Trạng thái:** Sẵn sàng deploy và customize theo nhu cầu cụ thể.
