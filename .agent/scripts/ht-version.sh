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
    echo "  Name:     $NAME"
    echo "  Version:  v$VERSION"
    echo "  Skills:   $SKILLS"
    echo "  Repo:     https://github.com/huynhtrungbk/antigravity-htkit"
    echo ""
    
    # Count actual skills
    ACTUAL=$(ls -d .agent/skills/*/ 2>/dev/null | wc -l | tr -d ' ')
    echo "  Actual skills on disk: $ACTUAL"
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
  echo "## v1.0.0 ($(date +%Y-%m-%d))"
  echo "- Initial release as Antigravity-HTKit"
  echo "- 59 skills across 8 categories"
  echo "- Fully rebranded from ClaudeKit/CK" 
  echo "- All paths migrated: .claude/ → .agent/"
  echo "- Custom config: .ht.json"
  echo "- Custom help: /ht-help"
  echo "- Vietnamese language support"
  echo "- By @huynhtrungbk"
}

case "${1:-show}" in
  show) show_version;;
  bump) bump_version "${2:-patch}";;
  changelog) changelog;;
  *) echo "Usage: ht-version.sh [show|bump major|minor|patch|changelog]";;
esac
