#!/usr/bin/env python3
"""Tests for Antigravity-HTKit help system v1.1.0."""

import sys
import subprocess
from pathlib import Path


def run_help(args: str = "") -> str:
    """Run ht-help.py and return output."""
    cmd = [sys.executable, ".agent/scripts/ht-help.py"] + args.split() if args else [sys.executable, ".agent/scripts/ht-help.py"]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(Path(__file__).resolve().parent.parent.parent))
    return result.stdout + result.stderr


def test_overview():
    """Test: overview shows all workflows."""
    output = run_help()
    errors = []
    if "Antigravity-HTKit Commands" not in output:
        errors.append("Missing title")
    if "11 workflows" not in output:
        errors.append("Missing workflow count")
    if "59 skills" not in output:
        errors.append("Missing skills count")
    if "/plan" not in output:
        errors.append("Missing /plan workflow")
    if "/fix" not in output:
        errors.append("Missing /fix workflow")
    if "@HT_OUTPUT_TYPE" not in output:
        errors.append("Missing @HT_OUTPUT_TYPE marker")
    return errors


def test_category_guide():
    """Test: category guide shows workflow steps."""
    output = run_help("fix")
    errors = []
    if "Sửa Lỗi" not in output:
        errors.append("Missing Vietnamese title")
    if "/fix" not in output:
        errors.append("Missing /fix reference")
    if "Workflow:" not in output:
        errors.append("Missing workflow section")
    if "Tip:" not in output:
        errors.append("Missing tip")
    return errors


def test_task_recommendation():
    """Test: task description gets recommendation."""
    output = run_help("debug login error")
    errors = []
    if "Recommended:" not in output:
        errors.append("Missing recommendation")
    if "/debug" not in output and "/fix" not in output:
        errors.append("Missing relevant workflow")
    return errors


def test_search():
    """Test: unknown word triggers search."""
    output = run_help("auth")
    errors = []
    if "Search:" not in output:
        errors.append("Missing search header")
    if "better-auth" not in output:
        errors.append("Missing better-auth result")
    return errors


def test_version():
    """Test: --version flag works."""
    output = run_help("--version")
    errors = []
    if "v1.1.0" not in output:
        errors.append("Missing version 1.1.0")
    if "Workflows: 11" not in output:
        errors.append("Missing workflow count")
    if "Skills: 59" not in output:
        errors.append("Missing skills count")
    return errors


def test_all_categories():
    """Test: all category guides load without error."""
    categories = ["fix", "plan", "bootstrap", "test", "deploy", "debug", "ask", "status", "watzup", "vn"]
    errors = []
    for cat in categories:
        output = run_help(cat)
        if "not found" in output:
            errors.append(f"Category '{cat}' not found")
        if "Workflow:" not in output:
            errors.append(f"Category '{cat}' missing workflow section")
    return errors


def test_no_legacy():
    """Test: no legacy CK references in output."""
    output = run_help()
    errors = []
    if "@CK_OUTPUT_TYPE" in output:
        errors.append("Legacy @CK_OUTPUT_TYPE found")
    if "/ck:" in output:
        errors.append("Legacy /ck: prefix found")
    if "commands/" in output.lower():
        errors.append("Legacy commands/ reference found")
    return errors


def main():
    """Run all tests."""
    tests = [
        ("Overview", test_overview),
        ("Category guide", test_category_guide),
        ("Task recommendation", test_task_recommendation),
        ("Search", test_search),
        ("Version", test_version),
        ("All categories", test_all_categories),
        ("No legacy refs", test_no_legacy),
    ]

    total_errors = 0
    for name, test_fn in tests:
        errors = test_fn()
        status = "✅" if not errors else "❌"
        print(f"{status} {name}")
        if errors:
            for e in errors:
                print(f"   → {e}")
            total_errors += len(errors)

    print(f"\n{'✅ All tests passed!' if total_errors == 0 else f'❌ {total_errors} error(s) found'}")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
