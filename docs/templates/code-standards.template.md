# Tiêu Chuẩn Code

**Ngày tạo:** 2026-02-05  
**Phiên bản:** 1.0  
**Trạng thái:** 📝 Template

---

## 1. Quy Tắc Chung

### Nguyên Tắc Cốt Lõi
- **YAGNI** - You Aren't Gonna Need It
- **KISS** - Keep It Simple, Stupid
- **DRY** - Don't Repeat Yourself

### Giới Hạn File
- Tối đa **200 dòng** mỗi file code
- Chia nhỏ file lớn thành modules

---

## 2. Naming Conventions

| Loại | Convention | Ví dụ |
|------|------------|-------|
| Files | kebab-case | `user-service.ts` |
| Classes | PascalCase | `UserService` |
| Functions | camelCase | `getUserById` |
| Constants | UPPER_SNAKE | `MAX_RETRY_COUNT` |
| Variables | camelCase | `userData` |

---

## 3. Git Commit

### Format
```
<type>(<scope>): <description>

[optional body]
```

### Types
- `feat:` - Tính năng mới
- `fix:` - Sửa lỗi
- `docs:` - Tài liệu
- `style:` - Format, không thay đổi logic
- `refactor:` - Tái cấu trúc
- `test:` - Thêm test
- `chore:` - Công việc khác

---

## 4. Code Style

### TypeScript/JavaScript
- Dùng `const` > `let`, tránh `var`
- Arrow functions cho callbacks
- Async/await thay vì .then()
- Try/catch cho error handling

### Comments
- Chỉ comment cho logic phức tạp
- TODO comments với format: `// TODO: description`
- Không commit commented code

---

## 5. Testing

- Viết test trước khi commit
- Coverage tối thiểu: 80%
- Không dùng mock data để pass test giả
