# Quy Trình Quản Lý Tài Liệu Dự Án

**Ngày tạo:** 2026-02-05  
**Phiên bản:** 1.0

---

## 1. Quy Tắc Đánh Số & Đặt Tên

Tất cả tài liệu được đánh số theo thứ tự và có ngày tháng:

```
[SỐ]-[LOẠI]-[TÊN]-[NGÀY].md

Ví dụ:
01-Analysis-System-Overview-2026-02-05.md
02-Plan-Feature-Implementation-2026-02-05.md
03-Report-Implementation-Results-2026-02-05.md
```

**Loại tài liệu:**
- `Analysis` - Phân tích (trước khi lập kế hoạch)
- `Plan` - Kế hoạch (trước khi triển khai, cần duyệt)
- `Report` - Báo cáo (sau khi triển khai)
- `Walkthrough` - Hướng dẫn chi tiết

---

## 2. Quy Trình Làm Việc

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   PHÂN TÍCH  │─────▶│   KẾ HOẠCH   │─────▶│   DUYỆT ĐÃ   │─────▶│  TRIỂN KHAI  │
│   Analysis   │      │     Plan     │      │   Approval   │      │ Implementation│
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
      │                      │                      │                      │
      ▼                      ▼                      ▼                      ▼
   Lưu trữ              Lưu trữ              Chờ duyệt              Báo cáo
```

### Bước 1: Phân tích → Lưu tài liệu `Analysis`
### Bước 2: Lập kế hoạch → Lưu tài liệu `Plan`  
### Bước 3: **Chờ duyệt** từ người dùng
### Bước 4: Triển khai → Lưu tài liệu `Report`

---

## 3. Quy Tắc Đặc Biệt

| Quy tắc | Mô tả |
|---------|-------|
| ✅ Tự động lưu | Tất cả tệp tin được tự động lưu (không cần hỏi) |
| ⏸️ Chờ duyệt kế hoạch | Kế hoạch PHẢI được duyệt trước khi triển khai |
| 🚀 Tự động tiếp tục | Sau khi hoàn thành phase, tự động chuyển phase tiếp |
| 📁 Chỉ mở tài liệu | Chỉ mở file phân tích/kế hoạch/báo cáo, KHÔNG mở file code |

---

## 4. Thư Mục Lưu Trữ

```
./docs/
├── 00-Documentation-Guidelines-2026-02-05.md  (file này)
├── 01-Analysis-xxx.md
├── 02-Plan-xxx.md
├── 03-Report-xxx.md
└── ...
```

---

## 5. Kit Đã Cài Đặt

**Trung-Videcode-Kit-Antigravity** đã được cài đặt thành công vào dự án với:
- 📦 40 Agents
- 🛠️ 84 Skills  
- 🔄 28 Workflows

Sử dụng các slash commands như `/plan`, `/fix`, `/cook`, `/bootstrap` để kích hoạt workflows.
