#!/usr/bin/env python3
"""Category guides and intent data for Antigravity-HTKit help system."""

import re
from .fuzzy import fuzzy_match

# Synonym mappings for normalization (term → canonical)
SYNONYMS = {
    "alerts": "notifications",
    "alert": "notification",
    "ci": "github actions",
    "ci/cd": "github actions",
    "pipeline": "github actions",
    "auth": "authentication",
    "db": "database",
    "repo": "repository",
    "deps": "dependencies",
    "pr": "pull request",
    "specs": "tests",
    "e2e": "integration test",
}

# Task keyword mappings for intent detection
TASK_MAPPINGS = {
    "fix": ["fix", "bug", "error", "broken", "issue", "crash", "fail", "wrong", "not working"],
    "plan": ["plan", "design", "architect", "research", "think", "analyze", "strategy", "how to", "approach"],
    "bootstrap": ["start", "new", "init", "setup", "project", "scaffold", "generate", "begin"],
    "test": ["test", "check", "verify", "validate", "spec", "unit", "integration", "coverage", "e2e"],
    "deploy": ["deploy", "production", "release", "publish", "ship", "live"],
    "debug": ["debug", "trace", "inspect", "investigate", "root cause", "stack trace"],
    "ask": ["ask", "question", "explain", "what is", "how does", "why"],
    "status": ["status", "health", "overview", "progress", "state"],
    "watzup": ["watzup", "summary", "wrap up", "what's up", "recent", "changes", "review"],
    "vn": ["vietnamese", "tiếng việt", "việt nam", "vn"],
}

# Category guides aligned with actual workflows
CATEGORY_GUIDES = {
    "fix": {
        "title": "Sửa Lỗi — /fix",
        "workflow": [
            ("Bắt đầu", "`/fix` \"mô tả lỗi\""),
            ("Debug sâu", "`/debug` \"chi tiết hơn\""),
            ("Kiểm tra", "`/test`"),
        ],
        "tip": "Gửi kèm error message để debug nhanh hơn",
    },
    "plan": {
        "title": "Lập Kế Hoạch — /plan",
        "workflow": [
            ("Phân tích", "`/plan` \"mô tả task\""),
            ("Duyệt plan", "Xem file Analysis + Plan trong docs/"),
            ("Triển khai", "Approve → agent thực thi"),
        ],
        "tip": "Plan luôn tạo Analysis trước, sau đó Plan — cần user approve trước khi code",
    },
    "bootstrap": {
        "title": "Khởi Tạo Dự Án — /bootstrap",
        "workflow": [
            ("Chọn stack", "`/bootstrap` \"mô tả yêu cầu\""),
            ("Agent hỏi", "Loại dự án, tech stack, database..."),
            ("Tự động", "Khởi tạo project + docs + README"),
        ],
        "tip": "Nêu rõ tech stack mong muốn để agent khởi tạo nhanh hơn",
    },
    "test": {
        "title": "Chạy Test — /test",
        "workflow": [
            ("Chạy test", "`/test`"),
            ("Phân tích", "Agent report pass/fail + root cause"),
        ],
        "tip": "Agent không tự fix — chỉ báo cáo kết quả. Dùng `/fix` để sửa",
    },
    "deploy": {
        "title": "Deploy — /deploy",
        "workflow": [
            ("Kiểm tra", "Verify tests + build"),
            ("Deploy", "`/deploy`"),
            ("Verify", "Agent check health sau khi deploy"),
        ],
        "tip": "Hỗ trợ Docker, SSH, Cloudflare Workers, và nhiều platform khác",
    },
    "debug": {
        "title": "Debug — /debug",
        "workflow": [
            ("Phân tích", "`/debug` \"mô tả vấn đề\""),
            ("Root cause", "Agent đọc logs + code → tìm nguyên nhân"),
            ("Đề xuất", "Giải thích + đề xuất fix (không tự sửa)"),
        ],
        "tip": "Debug chỉ phân tích — dùng `/fix` để agent tự sửa",
    },
    "ask": {
        "title": "Hỏi Đáp — /ask",
        "workflow": [
            ("Hỏi", "`/ask` \"câu hỏi kỹ thuật\""),
            ("Trả lời", "Agent research codebase + docs nếu cần"),
        ],
        "tip": "Dùng cho câu hỏi kỹ thuật, kiến trúc, hoặc library",
    },
    "status": {
        "title": "Trạng Thái — /status",
        "workflow": [
            ("Kiểm tra", "`/status`"),
            ("Report", "Git status, services, build, TODOs"),
        ],
        "tip": "Chạy đầu session để nắm tình hình dự án",
    },
    "watzup": {
        "title": "Tóm Tắt — /watzup",
        "workflow": [
            ("Review", "`/watzup`"),
            ("Summary", "Xem commits gần đây + file thay đổi"),
        ],
        "tip": "Chạy cuối session để nắm progress và plan next steps",
    },
    "vn": {
        "title": "Workflow Tiếng Việt — /vn",
        "workflow": [
            ("Kích hoạt", "`/vn`"),
            ("Quy tắc", "Output tiếng Việt, code comments tiếng Anh"),
            ("Flow", "Phân tích → Plan → Duyệt → Triển khai → Report"),
        ],
        "tip": "Tất cả docs và analysis sẽ bằng tiếng Việt",
    },
}


def expand_synonyms(text: str) -> str:
    """Replace synonyms with canonical terms."""
    result = text.lower()
    sorted_synonyms = sorted(SYNONYMS.items(), key=lambda x: -len(x[0]))
    for synonym, canonical in sorted_synonyms:
        pattern = r'\b' + re.escape(synonym) + r'\b'
        result = re.sub(pattern, canonical, result, flags=re.IGNORECASE)
    return result


def detect_intent(input_str: str, workflow_names: list) -> str:
    """Smart auto-detection of user intent."""
    if not input_str:
        return "overview"

    input_lower = input_str.lower()
    words = input_str.split()

    # Multiple words = likely task description
    if len(words) >= 2:
        return "task"

    # Single word: check if it's a known workflow
    if input_lower in [w.lower() for w in workflow_names]:
        return "category"

    # Check CATEGORY_GUIDES
    if input_lower in [c.lower() for c in CATEGORY_GUIDES.keys()]:
        return "category"

    # Fuzzy match against categories
    all_categories = set(w.lower() for w in workflow_names) | set(c.lower() for c in CATEGORY_GUIDES.keys())
    for cat in all_categories:
        if fuzzy_match(input_lower, cat):
            return "category"

    # Fuzzy match against task keywords
    for cat, keywords in TASK_MAPPINGS.items():
        for kw in keywords:
            if ' ' not in kw and fuzzy_match(input_lower, kw):
                return "task"

    return "search"
