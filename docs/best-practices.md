# Best Practices for Claude Skills

Collected from Anthropic's official docs, community experience, and personal iteration.

## 1. Write Trigger-Rich Descriptions

The `description` field in YAML frontmatter is the **most important part** of your skill. Claude uses it to decide when to activate the skill. Be specific.

**Bad:** `"Helps with documentation"`

**Good:** `"Fetch and index documentation from DeepWiki (deepwiki.com) for any public GitHub repository. Use when looking up docs for an open-source library, needing to understand a repo's architecture, or when coding tasks would benefit from consulting upstream library documentation. Triggers on 'look up docs for X', 'how does X library work', 'fetch documentation for owner/repo'."`

## 2. Start Simple, Iterate

Don't try to build the perfect skill on attempt one. The recommended cycle:

1. Build minimal version with just SKILL.md
2. Upload and test with real prompts
3. Note what breaks or triggers incorrectly
4. Add scripts/references as needed
5. Repeat 3-5 times

Most production-quality skills went through 5-6 iterations.

## 3. One Skill, One Purpose

Create separate skills for different workflows. A focused skill triggers more reliably than a "do everything" skill.

If you need skills to work together, reference each other in their descriptions.

## 4. Use Progressive Disclosure

Don't put everything in SKILL.md. Split like this:

| Content | Where | When Loaded |
|---------|-------|-------------|
| Name + description | Frontmatter | Always |
| Core workflow steps | SKILL.md body | When skill activates |
| Detailed API docs | `references/` | When Claude needs specifics |
| Reusable scripts | `scripts/` | Executed on demand |
| Templates/images | `assets/` | Copied into output |

## 5. Scripts > Repeated Code

If Claude would rewrite the same code every time, make it a script:
- More reliable (tested once, used many times)
- Token efficient (output only, code not loaded into context)
- Deterministic (same input → same output)

## 6. CLAUDE.md Best Practices

For repository-level CLAUDE.md files:

- **Do:** Document what Claude gets wrong (corrections)
- **Do:** Link to detailed docs: `"For FooBarError, see docs/troubleshooting.md"`
- **Do:** Specify safe alternatives: `"Never use --force; prefer --force-with-lease instead"`
- **Don't:** Embed entire files (wastes context every run)
- **Don't:** Write a comprehensive manual (keep it focused)
- **Don't:** Just say "never do X" without an alternative

## 7. Context Window is a Public Good

Every token in SKILL.md is a token not available for the user's actual task. Challenge every line: "Does Claude really need this? Is this something Claude already knows?"

Prefer concise examples over verbose explanations.

## 8. Test Both Triggering and Execution

Two failure modes:
1. **Skill doesn't trigger:** Description too vague → add more trigger phrases
2. **Skill triggers but results are bad:** Instructions unclear → add examples, constraints, explicit steps

## 9. Handle Errors Gracefully

Scripts should:
- Print helpful error messages to stderr
- Return non-zero exit codes on failure
- Suggest next steps when things go wrong

## 10. Security

- Never hardcode API keys or secrets in skills
- Review downloaded skills before enabling
- Use environment variables for sensitive configuration
- Be cautious with skills that run arbitrary bash commands

## Further Reading

- [Anthropic: How to create Skills](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)
- [Anthropic: Using Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Anthropic: Agent Skills Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Official Skills Repo](https://github.com/anthropics/skills)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
