# Skill Development Rules

Guidelines for building high-quality Claude skills in this repository.

## Naming

- Skill folder: `lowercase-hyphen-separated`
- SKILL.md `name` field: must match folder name exactly
- Scripts: `snake_case.py` or `kebab-case.sh`

## SKILL.md Requirements

1. YAML frontmatter with `name` and `description` (both required)
2. Description must include:
   - What the skill does
   - Specific trigger conditions ("Use when...")
   - Example phrases that should activate it
3. Body under 500 lines
4. Use imperative/infinitive form in instructions

## Description Quality Checklist

- [ ] Includes 3+ trigger phrases
- [ ] Mentions specific file types or tools if applicable
- [ ] Avoids vague terms like "helps with" or "assists in"
- [ ] Specifies what NOT to use the skill for (if ambiguous)

## Script Standards

- Shebang line: `#!/usr/bin/env python3`
- Prefer stdlib over pip packages
- If pip needed: document in SKILL.md with `pip install --break-system-packages`
- Include `--help` / argparse for CLI scripts
- Handle errors gracefully with informative messages to stderr
- Test scripts before packaging

## File Organization

```
skill-name/
├── SKILL.md              # Required
├── scripts/              # Executable code
├── references/           # On-demand documentation
└── assets/               # Templates, images (not loaded into context)
```

- Do NOT create: README.md, CHANGELOG.md, tests/, docs/ inside a skill
- References are loaded only when Claude needs them
- Assets are used in output, never read into context

## Progressive Disclosure

1. **Frontmatter** (~100 words) — always in context, triggers skill
2. **SKILL.md body** (<5k words) — loaded when skill activates
3. **References/scripts** (unlimited) — loaded on demand

Split content when SKILL.md approaches 500 lines.

## Packaging

```bash
cd skills/<name>
zip -r ../../<name>.skill .
```

Verify: the zip must contain `<name>/SKILL.md` at root level (not nested deeper).
