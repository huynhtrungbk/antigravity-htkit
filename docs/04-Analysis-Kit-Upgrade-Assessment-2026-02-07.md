# Phân Tích Đánh Giá Nâng Cấp Antigravity-HTKit v1.0.0

**Ngày:** 2026-02-07  
**Phiên bản Kit:** 1.0.0  
**Mục đích:** Đánh giá toàn diện kit sau rebranding, phát hiện vấn đề cần nâng cấp/điều chỉnh

---

## 1. Tổng Quan Hiện Tại

| Thành phần | Số lượng | Dung lượng | Trạng thái |
|------------|----------|------------|------------|
| Skills | 59 (tất cả có SKILL.md) | 135 MB | ✅ Tốt |
| Workflows | 11 files | 1.5 MB | ✅ Tốt |
| Scripts | 18 files (4704 dòng) | 2.4 MB | ⚠️ Cần xem lại |
| Rules | 3 files | 512 KB | ✅ Tốt |
| Config files | 3 (.ht.json, config.json, metadata.json) | — | ⚠️ Trùng lặp |

**Rebranding:** ✅ Sạch — Không còn reference cũ (claudekit, videcode, .ck.)

---

## 2. Vấn Đề Phát Hiện

### 🔴 VẤN ĐỀ NGHIÊM TRỌNG

#### 2.1 `ht-help.py` phụ thuộc vào `.agent/commands/` — thư mục không tồn tại

**Chi tiết:** Script chính `ht-help.py` scan `.agent/commands/` để build command catalog. Thư mục này **không tồn tại** trong v1.0.0 (đã bị xóa khi slim down từ Ultimate).

**Hậu quả:**
- `python3 .agent/scripts/ht-help.py` → `Error: .agent/commands/ directory not found.`
- Toàn bộ test (`test_ht_help.py`) fail
- Help system không hoạt động

**Khuyến nghị:** Viết lại `ht-help.py` để scan `.agent/workflows/` thay vì `.agent/commands/`, hoặc xây dựng catalog từ `skills_data.yaml` + `commands_data.yaml`.

---

#### 2.2 `ht-help.py` vượt giới hạn 200 dòng (1165 dòng)

**Chi tiết:** File lớn nhất trong kit, vi phạm rule "Keep code files under 200 lines — split into modules when exceeded".

**Khuyến nghị:** Module hóa thành:
- `ht-help.py` — entry point (~50 dòng)
- `lib/intent_detection.py` — fuzzy match, synonyms, task mapping
- `lib/category_guides.py` — workflow guides data
- `lib/display.py` — output formatting
- `lib/discovery.py` — command/workflow scanning

---

#### 2.3 Stale workflow references trong help system

**Chi tiết:** `CATEGORY_GUIDES` trong `ht-help.py` tham chiếu nhiều commands **không tồn tại** trong v1.0.0:

| Command tham chiếu | Có tồn tại? |
|---------------------|-------------|
| `/cook`, `/cook:auto` | ❌ |
| `/code`, `/code:parallel` | ❌ |
| `/scout`, `/scout:ext` | ❌ |
| `/preview` | ❌ |
| `/journal` | ❌ |
| `/brainstorm` | ❌ |
| `/design:fast`, `/design:screenshot`, `/design:3d` | ❌ |
| `/docs:init`, `/docs:update` | ❌ |
| `/review:codebase` | ❌ |
| `/content:fast`, `/content:good`, `/content:cro` | ❌ |
| `/integrate:polar`, `/integrate:sepay` | ❌ |
| `/skill:create`, `/skill:optimize` | ❌ |
| `/fix:test` | ❌ |
| `/git:cm`, `/git:cp`, `/git:pr` | ❌ |
| `/worktree` | ❌ |
| `/kanban` | ❌ |
| `/plan:fast`, `/plan:hard`, `/plan:validate` | ❌ |
| `/bootstrap:auto:fast` | ❌ |

**Workflows thực sự có:** `/ask`, `/bootstrap`, `/debug`, `/deploy`, `/fix`, `/ht-help`, `/plan`, `/status`, `/test`, `/vn`, `/watzup`

**Khuyến nghị:** Cập nhật `CATEGORY_GUIDES` cho khớp với 11 workflows thực tế.

---

### 🟡 VẤN ĐỀ TRUNG BÌNH

#### 2.4 Config trùng lặp giữa `config.json` và `.ht.json`

| Field | `config.json` | `.ht.json` |
|-------|---------------|------------|
| `responseLanguage` | `"vi"` | `"vi"` |
| `codingLevel` | `3` | — |
| `gemini.model` | `"gemini-3.0-flash"` | — |
| `version` | — | `"1.0.0"` |
| `author` | — | `"huynhtrungbk"` |

**Khuyến nghị:** Hợp nhất vào `.ht.json` (config chính) và đơn giản hóa `config.json` thành project-specific settings.

---

#### 2.5 Thiếu thư mục `features/` và `plans/`

**Chi tiết:** `documentation-management.md` yêu cầu cấu trúc `features/` chi tiết và `.ht.json` reference `featuresFolder: "./features/"`. Cả hai thư mục đều **không tồn tại**.

**Khuyến nghị:** 
- Tạo `features/.gitkeep`
- Hoặc xóa references nếu không dùng

---

#### 2.6 `metadata.json` thống kê sai — `"scripts": 50`

**Chi tiết:** Metadata ghi 50 scripts nhưng thực tế chỉ có 18.

```json
"stats": {
    "skills": 59,      // ✅ Đúng
    "categories": 8,   // ✅ Đúng
    "scripts": 50      // ❌ Sai (thực tế: 18)
}
```

**Khuyến nghị:** Sửa thành `"scripts": 18`.

---

#### 2.7 `@CK_OUTPUT_TYPE` — Legacy output marker

**Chi tiết:** `ht-help.py` còn 6 lần sử dụng `@CK_OUTPUT_TYPE` (prefix "CK" từ ClaudeKit).

**Khuyến nghị:** Đổi thành `@HT_OUTPUT_TYPE` hoặc xóa nếu không cần thiết.

---

### 🟢 VẤN ĐỀ NHỎ

#### 2.8 Scripts quá lớn khác

| Script | Dòng | Giới hạn |
|--------|------|----------|
| `worktree.cjs` | 822 | > 200 |
| `worktree.test.cjs` | 759 | > 200 |
| `test_ht_help.py` | 420 | > 200 |
| `validate-docs.cjs` | 342 | > 200 |
| `resolve_env.py` | 329 | > 200 |

**Khuyến nghị:** Ưu tiên refactor `ht-help.py` trước, các file khác tùy chọn.

---

#### 2.9 Test files trùng tên

- `test-ht-help.py` (218 dòng)
- `test_ht_help.py` (420 dòng)
- `test_ht_help_integration.py` (127 dòng)

**Khuyến nghị:** Xóa `test-ht-help.py` (cũ/nhỏ hơn), giữ `test_ht_help.py`.

---

#### 2.10 `scan_commands.py` scan thư mục không tồn tại

**Chi tiết:** Script scan `.agent/commands/` — cùng vấn đề với `ht-help.py`.

**Khuyến nghị:** Xóa hoặc viết lại để scan workflows.

---

## 3. Đánh Giá Tổng Thể

### ✅ Điểm Mạnh
- **Rebranding sạch** — không còn reference cũ
- **59 skills đều có SKILL.md** — cấu trúc đầy đủ
- **11 workflows hoạt động tốt** — coverage Engineering + Marketing
- **Rules rõ ràng** — development, documentation, primary workflow
- **`ht-version.sh` hoạt động hoàn hảo**
- **Config identity chính xác** — admin, email, github

### ❌ Điểm Yếu
- **Help system không hoạt động** (critical blocker)
- **Nhiều phantom commands** trong help (guide người dùng sai)
- **Scripts không tuân thủ rule 200 dòng** của chính kit
- **Config phân tán** giữa 3 files

### 📊 Điểm Số: **7/10** (giảm từ 9/10 do phát hiện thêm vấn đề)

---

## 4. Khuyến Nghị Ưu Tiên

### Phase 1: Khắc Phục Ngay (Critical)
| # | Hành động | Ưu tiên |
|---|-----------|---------|
| 1 | Viết lại `ht-help.py` — scan workflows thay vì commands | 🔴 |
| 2 | Cập nhật `CATEGORY_GUIDES` cho khớp 11 workflows thực tế | 🔴 |
| 3 | Sửa `metadata.json` scripts count | 🔴 |

### Phase 2: Cải Thiện (Medium)
| # | Hành động | Ưu tiên |
|---|-----------|---------|
| 4 | Module hóa `ht-help.py` thành 5 files nhỏ | 🟡 |
| 5 | Hợp nhất config (config.json → .ht.json) | 🟡 |
| 6 | Tạo `features/` directory hoặc xóa references | 🟡 |
| 7 | Đổi `@CK_OUTPUT_TYPE` → `@HT_OUTPUT_TYPE` | 🟡 |

### Phase 3: Tùy Chọn (Low)
| # | Hành động | Ưu tiên |
|---|-----------|---------|
| 8 | Xóa `test-ht-help.py` trùng | 🟢 |
| 9 | Xóa/viết lại `scan_commands.py` | 🟢 |
| 10 | Refactor scripts lớn khác | 🟢 |

---

## 5. Kết Luận

> **Kit hoạt động tốt ở mức skills và workflows, nhưng hệ thống help/discovery bị hỏng hoàn toàn** do vẫn phụ thuộc vào cấu trúc cũ (`.agent/commands/`). Cần ưu tiên sửa `ht-help.py` để khôi phục khả năng self-discovery của kit.

**Trạng thái:** ⚠️ Cần nâng cấp Phase 1 trước khi phân phối
