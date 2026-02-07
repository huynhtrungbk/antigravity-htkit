# Documentation Management

## Structure

```
docs/                                ← Tài liệu tổng (timeline dự án)
├── 10-Analysis-Production-VPS-2026-02-07.md
├── 11-Report-Kit-Slim-Down-2026-02-07.md
├── 12-Feature-Payment-Integration-2026-02-08.md   ← tóm tắt + link
└── ...

features/                            ← Chi tiết từng tính năng
├── payment-integration/
│   ├── 01-analysis.md
│   ├── 02-plan.md
│   └── 03-report.md
├── dashboard-upgrade/
│   ├── 01-analysis.md
│   ├── 02-plan.md
│   └── 03-report.md
└── ...
```

## Quy tắc

### docs/ — Timeline dự án

- Format: `XX-Type-Name-YYYY-MM-DD.md`
- Đánh số liên tục (kiểm tra số cuối cùng, +1)
- Types: `Analysis`, `Plan`, `Report`, `Fix`, `Feature`
- File `Feature` trong docs/ = tóm tắt ngắn + link đến `features/`
- Mọi hoạt động đều có entry trong docs/ (không bỏ sót)

### features/ — Chi tiết tính năng

- Mỗi feature 1 thư mục: `features/ten-tinh-nang/`
- Bên trong đánh số: `01-analysis.md`, `02-plan.md`, `03-report.md`
- Có thể thêm `assets/` nếu cần screenshots, diagrams

### Khi nào dùng gì?

| Công việc | Lưu ở đâu |
|-----------|-----------|
| Phân tích, báo cáo, fix bug | `docs/` (file lẻ) |
| Feature mới / nâng cấp feature | `docs/` (tóm tắt) + `features/` (chi tiết) |

## Approval Flow

- Analysis → lưu trước khi tạo Plan
- Plan → lưu và gửi user duyệt trước khi triển khai
- Sau khi duyệt → triển khai liên tục tất cả phases
- Report → lưu sau khi hoàn thành