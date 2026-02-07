#!/usr/bin/env python3
"""Display formatters for Antigravity-HTKit help system."""

import re
from .guides import CATEGORY_GUIDES, TASK_MAPPINGS, expand_synonyms
from .fuzzy import fuzzy_match

# Disambiguation threshold
DISAMBIGUATION_THRESHOLD = 0.5


def emit_output_type(output_type: str) -> None:
    """Emit output type marker for LLM presentation guidance."""
    print(f"@HT_OUTPUT_TYPE:{output_type}")
    print()


def show_overview(workflows: list, skills: list) -> None:
    """Display overview with quick start guide."""
    emit_output_type("category-guide")

    print("# Antigravity-HTKit Commands")
    print()
    print(f"{len(workflows)} workflows, {len(skills)} skills.")
    print()
    print("**Quick Start:**")
    print("- `/plan` - Lập kế hoạch triển khai")
    print("- `/fix` - Phân tích và sửa lỗi")
    print("- `/debug` - Debug mà không tự sửa")
    print("- `/test` - Chạy test và phân tích kết quả")
    print()
    print("**Common Workflows:**")
    print("- Feature mới: `/plan` → approve → implement → `/test`")
    print("- Bug fix: `/debug` → `/fix` → `/test`")
    print("- Deploy: `/test` → `/deploy`")
    print("- Review: `/watzup` → `/status`")
    print()
    print("**Workflows:**")
    for wf in workflows:
        power = '⚡' * wf['power_level'] if wf['power_level'] > 0 else ''
        print(f"- `{wf['name']}` {power} — {wf['description']}")
    print()
    print("**Usage:**")
    print("- `/ht-help <workflow>` - Hướng dẫn workflow cụ thể")
    print("- `/ht-help <task description>` - Gợi ý workflow phù hợp")
    print()
    print("**Tips:**")
    print("- Dùng `/vn` cho dự án Việt Nam")
    print("- Dùng `/ask` cho câu hỏi kỹ thuật nhanh")
    print("- Dùng `/bootstrap` để khởi tạo dự án mới")


def show_category_guide(category: str, workflows: list) -> None:
    """Display category guide with workflow and tips."""
    emit_output_type("category-guide")

    cat_key = None
    category_lower = category.lower()

    # Find matching category
    for key in CATEGORY_GUIDES.keys():
        if key.lower() == category_lower:
            cat_key = key
            break

    # Fuzzy match for typos
    if not cat_key:
        for key in CATEGORY_GUIDES.keys():
            if fuzzy_match(category_lower, key.lower()):
                cat_key = key
                break

    if not cat_key:
        available = ", ".join(f"`{c}`" for c in sorted(CATEGORY_GUIDES.keys()))
        print(f"Workflow '{category}' not found.")
        print()
        print(f"Available: {available}")
        return

    guide = CATEGORY_GUIDES[cat_key]
    print(f"# {guide['title']}")
    print()

    if "workflow" in guide:
        print("**Workflow:**")
        for step, cmd in guide["workflow"]:
            print(f"- {step}: {cmd}")
        print()

    if "tip" in guide:
        print(f"*Tip: {guide['tip']}*")


def do_search(term: str, workflows: list, skills: list) -> None:
    """Search workflows and skills by keyword."""
    emit_output_type("search-results")

    term_lower = term.lower()
    matches = []

    for wf in workflows:
        if term_lower in wf["name"].lower() or term_lower in wf["description"].lower():
            matches.append(("workflow", wf["name"], wf["description"]))

    for sk in skills:
        if term_lower in sk["name"].lower() or term_lower in sk["description"].lower():
            matches.append(("skill", sk["name"], sk["description"][:80]))

    if not matches:
        print(f"No results for '{term}'.")
        print()
        available = ", ".join(f"`{c}`" for c in sorted(CATEGORY_GUIDES.keys()))
        print(f"Try browsing: {available}")
        return

    print(f"# Search: {term}")
    print()
    print(f"Found {len(matches)} matches:")
    for kind, name, desc in matches[:10]:
        prefix = "📋" if kind == "workflow" else "🔧"
        print(f"- {prefix} `{name}` — {desc}")


def recommend_task(task: str, workflows: list) -> None:
    """Recommend workflows for a task description."""
    emit_output_type("task-recommendations")

    task_expanded = expand_synonyms(task)
    task_lower = task_expanded
    words = task_lower.split()

    ACTION_VERBS = {
        "fix", "debug", "test", "create", "build", "implement", "deploy",
        "plan", "design", "review", "check", "verify", "find", "search",
    }

    first_word_is_action = words[0] in ACTION_VERBS if words else False

    scores = {}
    for cat, keywords in TASK_MAPPINGS.items():
        score = 0.0
        for kw in keywords:
            if ' ' in kw:
                if kw in task_lower:
                    score += 3.0
            else:
                matched_pos = -1
                is_fuzzy = False

                match = re.search(r'\b' + re.escape(kw) + r'\b', task_lower)
                if match:
                    char_count = 0
                    for i, word in enumerate(words):
                        if char_count <= match.start() < char_count + len(word):
                            matched_pos = i
                            break
                        char_count += len(word) + 1
                else:
                    for i, word in enumerate(words):
                        if fuzzy_match(word, kw):
                            matched_pos = i
                            is_fuzzy = True
                            break

                if matched_pos >= 0:
                    if len(words) > 1:
                        if first_word_is_action and matched_pos == 0:
                            weight = 2.5
                        elif first_word_is_action:
                            weight = 1.0
                        else:
                            weight = 1.0 + (matched_pos / (len(words) - 1))
                    else:
                        weight = 2.0

                    if is_fuzzy:
                        weight *= 0.8

                    score += weight
        if score > 0:
            scores[cat] = score

    if not scores:
        available = ", ".join(f"`/{c}`" for c in sorted(CATEGORY_GUIDES.keys()))
        print(f"Not sure about: {task}")
        print()
        print(f"Try: {available}")
        return

    sorted_cats = sorted(scores.items(), key=lambda x: -x[1])

    # Check for ambiguity
    if len(sorted_cats) >= 2:
        top_score = sorted_cats[0][1]
        second_score = sorted_cats[1][1]
        if top_score - second_score < DISAMBIGUATION_THRESHOLD and top_score > 0:
            _format_disambiguation(task, sorted_cats[:3])
            return

    top_cat = sorted_cats[0][0]
    guide = CATEGORY_GUIDES.get(top_cat, {})

    print(f"# Recommended: /{top_cat}")
    print()

    if guide:
        print(f"**{guide.get('title', top_cat.title())}**")
        print()
        if "workflow" in guide:
            for step, cmd in guide["workflow"]:
                print(f"- {step}: {cmd}")
        print()
        if "tip" in guide:
            print(f"*Tip: {guide['tip']}*")

    # Show alternatives if any
    if len(sorted_cats) > 1:
        alternatives = [f"`/{cat}`" for cat, _ in sorted_cats[1:3]]
        print()
        print(f"**Alternatives:** {', '.join(alternatives)}")


def _format_disambiguation(task: str, candidates: list) -> None:
    """Output disambiguation prompt for close-scoring categories."""
    print(f"# Clarify: {task}")
    print()
    print("Matches multiple workflows:")
    print()

    for i, (cat, score) in enumerate(candidates[:3], 1):
        guide = CATEGORY_GUIDES.get(cat, {})
        title = guide.get("title", cat.title())
        print(f"{i}. **{title}** — `/{cat}`")

    print()
    print("*Reply with workflow name or rephrase.*")
