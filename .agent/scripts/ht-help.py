#!/usr/bin/env python3
"""
Antigravity-HTKit Help Command — Modular entry point.
Scans .agent/workflows/ and .agent/skills/ to build catalog at runtime.

Usage:
    python3 ht-help.py                    # Overview with quick start
    python3 ht-help.py fix                # Category guide with workflow
    python3 ht-help.py debug login error  # Task recommendations
    python3 ht-help.py auth               # Search (unknown word)
"""

import sys
import io
from pathlib import Path

# Fix Windows console encoding for Unicode characters
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Add scripts dir to path for lib imports
sys.path.insert(0, str(Path(__file__).parent))

from lib.discovery import discover_workflows, discover_skills
from lib.guides import detect_intent
from lib.display import show_overview, show_category_guide, do_search, recommend_task


def main():
    """Main entry point."""
    # Resolve .agent directory
    script_dir = Path(__file__).resolve().parent
    agent_dir = script_dir.parent

    workflows_dir = agent_dir / "workflows"
    skills_dir = agent_dir / "skills"

    # Discover available workflows and skills
    workflows = discover_workflows(workflows_dir)
    skills = discover_skills(skills_dir)

    if not workflows:
        print("Error: No workflows found in .agent/workflows/")
        print("Expected: .agent/workflows/*.md with YAML frontmatter")
        sys.exit(1)

    # Get user input
    user_input = " ".join(sys.argv[1:]).strip() if len(sys.argv) > 1 else ""

    # Handle special flags
    if user_input in ("--version", "-v"):
        print(f"Antigravity-HTKit Help v1.1.0")
        print(f"Workflows: {len(workflows)}, Skills: {len(skills)}")
        return

    # Detect intent and route
    workflow_names = [wf["name"].lstrip("/") for wf in workflows]
    intent = detect_intent(user_input, workflow_names)

    if intent == "overview":
        show_overview(workflows, skills)
    elif intent == "category":
        show_category_guide(user_input, workflows)
    elif intent == "task":
        recommend_task(user_input, workflows)
    else:
        do_search(user_input, workflows, skills)


if __name__ == "__main__":
    main()
