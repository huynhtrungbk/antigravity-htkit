#!/usr/bin/env python3
"""Workflow and skill discovery for Antigravity-HTKit help system."""

import re
from pathlib import Path


def parse_frontmatter(file_path: Path) -> dict:
    """Parse YAML frontmatter from a markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception:
        return {}

    if not content.startswith('---'):
        return {}

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return {}

    frontmatter = content[3:end_idx].strip()
    result = {}

    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip()

    return result


def discover_workflows(workflows_dir: Path) -> list:
    """Scan .agent/workflows/ and build workflow catalog."""
    workflows = []

    if not workflows_dir.exists():
        return workflows

    for md_file in sorted(workflows_dir.glob("*.md")):
        fm = parse_frontmatter(md_file)
        description = fm.get('description', '')

        if not description:
            continue

        name = md_file.stem
        clean_desc = re.sub(r'^[⚡\s]+', '', description).strip()

        # Count power level (⚡ count)
        power_level = description.count('⚡')

        workflows.append({
            "name": f"/{name}",
            "description": clean_desc,
            "power_level": power_level,
            "filename": md_file.name,
        })

    return workflows


def discover_skills(skills_dir: Path) -> list:
    """Scan .agent/skills/ and build skill catalog."""
    skills = []

    if not skills_dir.exists():
        return skills

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        fm = parse_frontmatter(skill_md)
        description = fm.get('description', '')

        skills.append({
            "name": skill_dir.name,
            "description": description[:120],
            "has_scripts": (skill_dir / "scripts").exists(),
            "has_references": (skill_dir / "references").exists(),
        })

    return skills
