# Claude Skills Collection

A comprehensive collection of custom [Claude Skills](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples), rules, and configurations for extending Claude's capabilities — built for developers and power users.

## Skills Overview

### Document Processing
| Skill | Description |
|-------|-------------|
| [`xlsx`](skills/xlsx/) | Excel spreadsheet creation, editing, and analysis |
| [`pdf`](skills/pdf/) | PDF reading, merging, splitting, OCR, and forms |
| [`pptx`](skills/pptx/) | PowerPoint presentations with templates and charts |
| [`docx`](skills/docx/) | Word documents with formatting and styles |

### Developer Tools
| Skill | Description |
|-------|-------------|
| [`deepwiki-docs`](skills/deepwiki-docs/) | Fetch documentation from DeepWiki for any GitHub repo |
| [`code-review`](skills/code-review/) | Professional code review with security checks |
| [`git-commit`](skills/git-commit/) | Conventional commit message generator |
| [`api-docs`](skills/api-docs/) | OpenAPI/Swagger documentation generator |
| [`debug-assistant`](skills/debug-assistant/) | Systematic debugging methodology |
| [`refactor-patterns`](skills/refactor-patterns/) | SOLID principles and refactoring guide |
| [`mcp-builder`](skills/mcp-builder/) | Build MCP servers for Claude integrations |
| [`skill-creator`](skills/skill-creator/) | Guide for creating new Claude skills |

### Design & Creative
| Skill | Description |
|-------|-------------|
| [`canvas-design`](skills/canvas-design/) | Create visual art and designs in PNG/PDF |
| [`algorithmic-art`](skills/algorithmic-art/) | Generative art with p5.js |
| [`theme-factory`](skills/theme-factory/) | Apply visual themes to artifacts |
| [`brand-guidelines`](skills/brand-guidelines/) | Professional brand colors and typography |
| [`slack-gif-creator`](skills/slack-gif-creator/) | Animated GIFs optimized for Slack |
| [`web-artifacts-builder`](skills/web-artifacts-builder/) | React + Tailwind + shadcn/ui components |

### Communication & Writing
| Skill | Description |
|-------|-------------|
| [`internal-comms`](skills/internal-comms/) | Status reports, updates, newsletters |
| [`doc-coauthoring`](skills/doc-coauthoring/) | Structured documentation workflow |

## Quick Start

### Use a skill in Claude.ai

1. Download a `.skill` file from [Releases](../../releases), or package one:
   ```bash
   cd skills/code-review
   zip -r ../../code-review.skill .
   ```
2. Go to **Claude.ai → Settings → Capabilities → Skills**
3. Click **Upload skill** → select the `.zip` / `.skill` file
4. Toggle **ON** and start chatting!

### Use with Claude Code

```bash
# Clone this repo
git clone https://github.com/ChenYCL/claude-skills-collection.git

# Copy skills to Claude Code directory
cp -r skills/code-review ~/.claude/skills/

# Or use as project skills
cp -r skills/code-review .claude/skills/
```

## Repository Structure

```
claude-skills-collection/
├── CLAUDE.md                      # Global Claude context & rules
├── README.md                      # This file
├── skills/                        # All skills
│   ├── xlsx/                     # Document processing
│   ├── pdf/
│   ├── pptx/
│   ├── docx/
│   ├── deepwiki-docs/            # Developer tools
│   ├── code-review/
│   ├── git-commit/
│   ├── api-docs/
│   ├── debug-assistant/
│   ├── refactor-patterns/
│   ├── mcp-builder/
│   ├── skill-creator/
│   ├── canvas-design/            # Design & creative
│   ├── algorithmic-art/
│   ├── theme-factory/
│   ├── brand-guidelines/
│   ├── slack-gif-creator/
│   ├── web-artifacts-builder/
│   ├── internal-comms/           # Communication
│   └── doc-coauthoring/
├── rules/                         # Coding rules & guidelines
├── .claude/                       # Claude Code config
│   └── commands/                  # Custom slash commands
├── docs/                          # Guides & documentation
├── .github/workflows/            # GitHub Actions
├── .gitignore
└── LICENSE
```

## Creating a New Skill

1. Use the `/new-skill` command in Claude Code, or:
2. Create a folder in `skills/<skill-name>/`
3. Add a `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: >
     Clear description with trigger phrases.
     Use when: (1) case one, (2) case two.
     Triggers: "keyword", "phrase".
   ---
   ```
4. Add scripts, references, and assets as needed
5. Test → Package → Upload

See [`skill-creator`](skills/skill-creator/) for detailed guidance.

## CLAUDE.md Rules

This repo includes a comprehensive `CLAUDE.md` with:

- Code style guidelines (Python, TypeScript, Go, Rust, Bash)
- Git commit conventions (Conventional Commits)
- Project structure standards
- Best practices for AI-assisted development

Copy `CLAUDE.md` to your project root to apply these rules.

## Contributing

Ideas and improvements are welcome! Open an issue or PR.

## License

MIT — See [LICENSE](LICENSE).

---

> 20 skills and growing. Built with Claude for the Claude ecosystem.
