# CLAUDE.md

> Shared configuration for Claude Code / Claude AI. This file is automatically loaded when Claude works in this repository.

## Project Overview

This is a curated collection of custom Claude skills, rules, and configurations. It serves as:
- A personal skill library for extending Claude's capabilities
- A shared configuration hub (`CLAUDE.md`, rules, commands)
- A best-practices reference for building new skills

## Repository Structure

```
├── CLAUDE.md              # This file — global Claude context
├── skills/                # Custom skills (.skill packages)
│   └── <skill-name>/     # Each skill is a self-contained folder
│       ├── SKILL.md      # Core instructions + YAML frontmatter
│       ├── scripts/      # Executable code (Python/Bash)
│       ├── references/   # Documentation Claude reads on-demand
│       └── assets/       # Templates, images, fonts
├── rules/                 # Reusable rule sets and guidelines
├── .claude/               # Claude Code project configuration
│   ├── commands/         # Custom slash commands
│   └── settings/         # Project settings
└── docs/                  # Documentation and guides
```

## Code Style Guidelines

### Python
```python
# Always use type hints
def process_data(items: list[str], limit: int = 10) -> dict[str, int]:
    """Process items and return counts."""
    ...

# Prefer dataclasses/Pydantic for data structures
@dataclass
class Config:
    host: str
    port: int = 8080

# Use context managers for resources
with open(path) as f:
    data = f.read()

# Prefer list comprehensions for simple transforms
names = [user.name for user in users if user.active]
```

### TypeScript/JavaScript
```typescript
// Use explicit types, avoid `any`
function fetchUser(id: string): Promise<User | null> { ... }

// Prefer const, use readonly for immutable data
const config: Readonly<Config> = { ... };

// Use optional chaining and nullish coalescing
const name = user?.profile?.name ?? 'Anonymous';

// Async/await over .then() chains
const data = await fetchData();
```

### Go
```go
// Handle errors explicitly, never ignore
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doSomething failed: %w", err)
}

// Use defer for cleanup
f, err := os.Open(path)
if err != nil { return err }
defer f.Close()

// Prefer small interfaces
type Reader interface {
    Read(p []byte) (n int, err error)
}
```

### Rust
```rust
// Use Result for fallible operations
fn parse_config(path: &str) -> Result<Config, ConfigError> { ... }

// Prefer iterators over manual loops
let names: Vec<_> = users.iter()
    .filter(|u| u.active)
    .map(|u| u.name.clone())
    .collect();

// Use ? for error propagation
let data = fs::read_to_string(path)?;
```

### Bash/Shell
```bash
#!/usr/bin/env bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Quote all variables
echo "${filename}"

# Use [[ ]] for conditionals
if [[ -f "$file" ]]; then
    ...
fi

# Prefer $() over backticks
result=$(command)
```

## Git Conventions

### Commit Messages
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`

**Examples:**
```
feat(code-review): add security checklist
fix(debug): handle null stack traces
docs(readme): add installation guide
refactor(api-docs): extract schema generator
```

### Branch Naming
- `feat/<name>` — New feature
- `fix/<name>` — Bug fix
- `docs/<name>` — Documentation
- `refactor/<name>` — Code refactoring

## Skills Conventions

### Structure
- Each skill lives in `skills/<skill-name>/` with a `SKILL.md` at root
- Skill names: lowercase, hyphen-separated (e.g., `code-review`)
- Scripts use only stdlib when possible; document any pip dependencies
- SKILL.md body stays under 500 lines; split details into `references/`
- Write clear, trigger-rich descriptions in YAML frontmatter

### SKILL.md Template
```yaml
---
name: skill-name
description: >
  Clear description of what this skill does.
  Include trigger phrases: "do X", "help with Y".
---

# Skill Name

Main instructions here...

## Workflow
1. Step one
2. Step two

## References
See [references/details.md](references/details.md) for more.
```

## Development Workflow

### Adding a New Skill
1. Create `skills/<name>/SKILL.md`
2. Add references and scripts as needed
3. Test with Claude (upload or local)
4. Update README.md skill table
5. Commit: `feat(skill): add <name> skill`

### Testing Skills
```bash
# Package for upload
cd skills/<name>
zip -r ../../<name>.skill .

# Test scripts directly
python skills/<name>/scripts/script.py --help
```

## Active Skills

| Skill | Description | Status |
|-------|-------------|--------|
| `deepwiki-docs` | Fetch & index GitHub repo docs from DeepWiki | ✅ Ready |
| `code-review` | Professional code review assistant | ✅ Ready |
| `git-commit` | Semantic commit message generator | ✅ Ready |
| `api-docs` | API documentation generator | ✅ Ready |
| `debug-assistant` | Systematic debugging helper | ✅ Ready |
| `refactor-patterns` | Refactoring patterns guide | ✅ Ready |

## Quick Reference

- DeepWiki: `https://deepwiki.com/{owner}/{repo}`
- Anthropic Skills Repo: `https://github.com/anthropics/skills`
- Skill Docs: `https://support.claude.com/en/articles/12512198`
- Conventional Commits: `https://www.conventionalcommits.org/`

## AI-Assisted Development Best Practices

1. **Be specific** — Clear prompts get better results
2. **Provide context** — Share relevant code, errors, constraints
3. **Iterate** — Refine outputs through conversation
4. **Verify** — Always review generated code before committing
5. **Test** — AI-generated code needs testing like any other code
6. **Learn** — Use AI explanations to deepen understanding
