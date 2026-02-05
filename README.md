# Claude Skills Collection

A curated collection of custom [Claude Skills](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples), rules, and configurations for extending Claude's capabilities — built for developers.

## Skills

| Skill | Description | Use Case |
|-------|-------------|----------|
| [`deepwiki-docs`](skills/deepwiki-docs/) | Fetch & index documentation from DeepWiki | Look up open-source library docs, build knowledge indexes |
| [`code-review`](skills/code-review/) | Professional code review assistant | PR reviews, code quality analysis, security checks |
| [`git-commit`](skills/git-commit/) | Semantic commit message generator | Conventional commits, changelog entries |
| [`api-docs`](skills/api-docs/) | API documentation generator | OpenAPI specs, endpoint documentation |
| [`debug-assistant`](skills/debug-assistant/) | Systematic debugging helper | Error analysis, stack traces, root cause finding |
| [`refactor-patterns`](skills/refactor-patterns/) | Refactoring patterns & best practices | Code smells, SOLID principles, design patterns |

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

# Skills in .claude/skills/ are auto-discovered
cp -r skills/code-review ~/.claude/skills/

# Or use as a project skill
cp -r skills/code-review .claude/skills/
```

## Repository Structure

```
claude-skills-collection/
├── CLAUDE.md                      # Global Claude context & rules
├── README.md                      # This file
├── skills/                        # Custom skills
│   ├── deepwiki-docs/            # Documentation fetcher
│   ├── code-review/              # Code review assistant
│   ├── git-commit/               # Commit message generator
│   ├── api-docs/                 # API documentation
│   ├── debug-assistant/          # Debugging helper
│   └── refactor-patterns/        # Refactoring guide
├── rules/                         # Coding rules & guidelines
├── .claude/                       # Claude Code config
│   └── commands/                  # Custom slash commands
├── docs/                          # Guides & documentation
├── .gitignore
└── LICENSE
```

## Creating a New Skill

1. Use the `/new-skill` command in Claude Code, or:
2. Create a folder in `skills/<skill-name>/`
3. Add a `SKILL.md` with YAML frontmatter (`name` + `description`)
4. Add scripts, references, and assets as needed
5. Test → Package → Upload

See [`docs/best-practices.md`](docs/best-practices.md) for detailed guidance.

## CLAUDE.md Rules

This repo includes a comprehensive `CLAUDE.md` with:

- Code style guidelines (Python, TypeScript, Go, Rust)
- Git commit conventions
- Project structure standards
- Best practices for AI-assisted development

Copy `CLAUDE.md` to your project root to apply these rules.

## Roadmap

- [x] Core skill: `deepwiki-docs`
- [x] Skill: `code-review`
- [x] Skill: `git-commit`
- [x] Skill: `api-docs`
- [x] Skill: `debug-assistant`
- [x] Skill: `refactor-patterns`
- [ ] Skill: `test-generator` — Generate unit tests from code
- [ ] Skill: `perf-analyzer` — Performance analysis guide
- [ ] GitHub Actions: Auto-package skills on release

## License

MIT — See [LICENSE](LICENSE).

---

> Built with Claude for the Claude ecosystem.
