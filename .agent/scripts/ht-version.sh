#!/bin/bash
# ht-version.sh — Antigravity-HTKit version manager
# Usage: bash .agent/scripts/ht-version.sh [bump|show|changelog]

set -euo pipefail

METADATA=".agent/metadata.json"
GEMINI="GEMINI.md"

show_version() {
  echo "╔══════════════════════════════════════════════╗"
  echo "║         Antigravity-HTKit                    ║"
  echo "║         by @huynhtrungbk                     ║"
  echo "╚══════════════════════════════════════════════╝"
  echo ""
  
  if [ -f "$METADATA" ]; then
    VERSION=$(python3 -c "import json; print(json.load(open('$METADATA'))['version'])")
    NAME=$(python3 -c "import json; print(json.load(open('$METADATA'))['name'])")
    SKILLS=$(python3 -c "import json; print(json.load(open('$METADATA'))['stats']['skills'])")
    WORKFLOWS=$(python3 -c "import json; print(json.load(open('$METADATA'))['stats'].get('workflows', 'N/A'))")
    echo "  Name:       $NAME"
    echo "  Version:    v$VERSION"
    echo "  Skills:     $SKILLS"
    echo "  Workflows:  $WORKFLOWS"
    echo "  Repo:       https://github.com/huynhtrungbk/antigravity-htkit"
    echo ""
    
    # Count actual
    ACTUAL_SKILLS=$(ls -d .agent/skills/*/ 2>/dev/null | wc -l | tr -d ' ')
    ACTUAL_WF=$(ls .agent/workflows/*.md 2>/dev/null | wc -l | tr -d ' ')
    echo "  On disk: $ACTUAL_SKILLS skills, $ACTUAL_WF workflows"
  else
    echo "  metadata.json not found"
  fi
}

bump_version() {
  local PART=${1:-patch}
  local CURRENT=$(python3 -c "import json; print(json.load(open('$METADATA'))['version'])")
  IFS='.' read -ra VER <<< "$CURRENT"
  
  case $PART in
    major) VER[0]=$((VER[0] + 1)); VER[1]=0; VER[2]=0;;
    minor) VER[1]=$((VER[1] + 1)); VER[2]=0;;
    patch) VER[2]=$((VER[2] + 1));;
  esac
  
  local NEW="${VER[0]}.${VER[1]}.${VER[2]}"
  local DATE=$(date -u +"%Y-%m-%dT%H:%M:%S.000Z")
  
  python3 -c "
import json
data = json.load(open('$METADATA'))
data['version'] = '$NEW'
data['buildDate'] = '$DATE'
json.dump(data, open('$METADATA', 'w'), indent=2)
print(f'Bumped: v$CURRENT → v$NEW')
"
  
  # Update GEMINI.md
  sed -i '' "s|v$CURRENT|v$NEW|g" "$GEMINI"
  echo "Updated $GEMINI"
}

changelog() {
  echo "# Antigravity-HTKit Changelog"
  echo ""
  echo "## v1.1.0 (2026-02-07)"
  echo "- Rewrite ht-help.py: modular architecture (lib/)"
  echo "- Scan .agent/workflows/ instead of dead .agent/commands/"
  echo "- Update CATEGORY_GUIDES to match 11 actual workflows"
  echo "- Replace @CK_OUTPUT_TYPE with @HT_OUTPUT_TYPE"
  echo "- Merge config.json overlap into .ht.json"
  echo "- Fix metadata.json (scripts: 50→18, +workflows: 11)"
  echo "- Remove stale scan_commands.py, duplicate test files"
  echo "- Create missing features/ and plans/ directories"
  echo "- Replace commands_data.yaml (51 /ck:* → 11 workflows)"
  echo ""
  echo "## v1.0.0 (2026-02-07)"
  echo "- Initial release as Antigravity-HTKit"
  echo "- 59 skills across 8 categories"
  echo "- Fully rebranded from previous kit"
  echo "- Custom config: .ht.json, Vietnamese support"
  echo "- By @huynhtrungbk"
}

case "${1:-show}" in
  show) show_version;;
  bump) bump_version "${2:-patch}";;
  changelog) changelog;;
  *) echo "Usage: ht-version.sh [show|bump major|minor|patch|changelog]";;
esac
