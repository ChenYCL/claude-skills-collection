# DeepWiki API Reference

## 1. DeepWiki MCP Server (Official)

**Base URL:** `https://mcp.deepwiki.com/`  
**Auth:** None required (public repos)  
**Protocols:** Streamable HTTP (`/mcp` - recommended), SSE (`/sse` - legacy)

### Tools

#### read_wiki_structure
Get the table of contents for a repository's documentation.
- **Input:** `{ "repo": "owner/repo" }`
- **Output:** List of documentation topics with hierarchy

#### read_wiki_contents
Get the full content of a specific documentation topic.
- **Input:** `{ "repo": "owner/repo", "topic": "topic-slug" }`
- **Output:** Full markdown content of the topic

#### ask_question
Ask a natural language question about a repository.
- **Input:** `{ "repo": "owner/repo", "question": "How does X work?" }`
- **Output:** AI-powered context-grounded answer

### MCP Client Config

```json
{
  "mcpServers": {
    "deepwiki": {
      "serverUrl": "https://mcp.deepwiki.com/mcp"
    }
  }
}
```

Claude Code: `claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp`

## 2. DeepWiki Web (Direct Fetch)

DeepWiki pages are available at `https://deepwiki.com/{owner}/{repo}`.

### URL Patterns

| Pattern | Description |
|---------|-------------|
| `https://deepwiki.com/{owner}/{repo}` | Repository overview + sidebar TOC |
| `https://deepwiki.com/{owner}/{repo}/{page-slug}` | Specific documentation page |

### Page Slug Format
- Top-level: `{N}-{title}` (e.g., `1-overview`, `2-feature-flags-system`)
- Sub-page: `{N.M}-{title}` (e.g., `4.1-fiber-architecture`)
- Deep sub: `{N.M.K}-{title}` (e.g., `3.2.1-webpack-config`)

### Extracting Content from HTML
The DeepWiki HTML page contains:
- **Sidebar navigation:** `<a href="/{owner}/{repo}/{slug}">` links for all pages
- **Main content:** Article body with headings, tables, code blocks, diagrams
- **Metadata:** Last indexed date, commit hash

Key elements to parse:
1. All `<a>` tags with `href` matching `/{owner}/{repo}/{slug}` → wiki structure
2. Text content after the "Menu" marker → page documentation
3. "Relevant source files" section → linked source code files

## 3. Limitations

- Only public GitHub repositories are available without auth
- Private repos require a Devin account (https://devin.ai)
- Some repos may not be indexed yet — visit deepwiki.com to request indexing
- Web scraping may include navigation/chrome text; filter accordingly
- Rate limits apply to both MCP and web endpoints
