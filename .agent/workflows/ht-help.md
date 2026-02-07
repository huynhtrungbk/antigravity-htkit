---
description: ⚡ Kit usage guide
---

## Available Workflows

| Command | Description |
|---------|-------------|
| `/ask` | Answer technical questions |
| `/plan` | Create implementation plan |
| `/fix` | Analyze and fix issues |
| `/debug` | Debug without auto-fixing |
| `/test` | Run tests and analyze |
| `/deploy` | Deploy to production |
| `/bootstrap` | Bootstrap new project |
| `/status` | Project status overview |
| `/vn` | Vietnamese workflow |
| `/watzup` | Review recent changes |

## Documentation

- Rules: `.agent/rules/`
- Skills: `.agent/skills/` (59 skills)
- Docs format: `docs/XX-Type-Name-YYYY-MM-DD.md`
- Features: `features/feature-name/` (per-feature details)

## Configuration

- Kit config: `.agent/.ht.json`
- Project config: `.agent/config.json`
- Metadata: `.agent/metadata.json`

## Scripts

```bash
# Check version
bash .agent/scripts/ht-version.sh show

# Get help
python3 .agent/scripts/ht-help.py

# Help on specific workflow
python3 .agent/scripts/ht-help.py fix

# Search skills
python3 .agent/scripts/ht-help.py auth
```
