---
name: mcp-builder
description: >
  Guide for building MCP (Model Context Protocol) servers that enable Claude to interact with external services.
  Use when: (1) building MCP servers, (2) integrating external APIs with Claude,
  (3) creating custom tools for Claude, (4) connecting services via MCP.
  Triggers: "MCP server", "MCP", "model context protocol", "claude tools",
  "build integration", "connect API", "create MCP".
---

# MCP Server Builder

Build high-quality MCP (Model Context Protocol) servers that enable Claude to interact with external services through well-designed tools.

## What is MCP?

MCP (Model Context Protocol) is a standard protocol for connecting AI models to external services. MCP servers expose "tools" that Claude can call to:
- Fetch data from APIs
- Execute actions in external systems
- Access local resources
- Process files and data

## Quick Start

### Python (FastMCP)

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("My Service")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city.

    Args:
        city: Name of the city
    """
    # Your implementation
    return f"Weather in {city}: Sunny, 72°F"

@mcp.tool()
def search_database(query: str, limit: int = 10) -> list[dict]:
    """Search the database.

    Args:
        query: Search query string
        limit: Maximum results to return
    """
    # Your implementation
    return [{"id": 1, "title": "Result"}]

if __name__ == "__main__":
    mcp.run()
```

### TypeScript (MCP SDK)

```typescript
// server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  { name: "my-service", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler("tools/list", async () => ({
  tools: [
    {
      name: "get_weather",
      description: "Get current weather for a city",
      inputSchema: {
        type: "object",
        properties: {
          city: { type: "string", description: "City name" }
        },
        required: ["city"]
      }
    }
  ]
}));

server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "get_weather") {
    return {
      content: [{ type: "text", text: `Weather in ${args.city}: Sunny` }]
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

const transport = new StdioServerTransport();
server.connect(transport);
```

## Tool Design Principles

### 1. Clear Names
```python
# Good
@mcp.tool()
def search_users(query: str) -> list[dict]:
    """Search for users by name or email."""

# Bad
@mcp.tool()
def do_search(q: str) -> list:
    """Search stuff."""
```

### 2. Descriptive Docstrings
```python
@mcp.tool()
def create_issue(
    title: str,
    body: str,
    labels: list[str] = None,
    assignee: str = None
) -> dict:
    """Create a new GitHub issue.

    Args:
        title: Issue title (required)
        body: Issue description in markdown
        labels: List of label names to apply
        assignee: GitHub username to assign

    Returns:
        Created issue with id, number, and url
    """
```

### 3. Proper Error Handling
```python
@mcp.tool()
def get_user(user_id: int) -> dict:
    """Get user by ID."""
    try:
        user = db.get_user(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")
        return user
    except ConnectionError as e:
        raise RuntimeError(f"Database connection failed: {e}")
```

### 4. Type Hints
```python
from typing import Optional

@mcp.tool()
def search_items(
    query: str,
    category: Optional[str] = None,
    limit: int = 10,
    include_metadata: bool = False
) -> list[dict]:
    """Search items with filters."""
```

## Project Structure

```
my-mcp-server/
├── src/
│   ├── __init__.py
│   ├── server.py       # MCP server entry point
│   ├── tools/          # Tool implementations
│   │   ├── __init__.py
│   │   ├── search.py
│   │   └── actions.py
│   └── utils/          # Shared utilities
│       └── api.py
├── tests/
│   └── test_tools.py
├── pyproject.toml
└── README.md
```

## Configuration

### Claude Desktop Config
```json
{
  "mcpServers": {
    "my-service": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

### Environment Variables
```python
import os

@mcp.tool()
def call_api(endpoint: str) -> dict:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY environment variable required")
    # Use api_key...
```

## Common Patterns

### Pagination
```python
@mcp.tool()
def list_items(
    page: int = 1,
    per_page: int = 20,
    cursor: str = None
) -> dict:
    """List items with pagination.

    Returns:
        items: List of items
        next_cursor: Cursor for next page (null if last page)
        total: Total item count
    """
    items, next_cursor, total = db.paginate(page, per_page, cursor)
    return {
        "items": items,
        "next_cursor": next_cursor,
        "total": total
    }
```

### Resource Access
```python
@mcp.resource("file://{path}")
def read_file(path: str) -> str:
    """Read a local file."""
    with open(path) as f:
        return f.read()
```

### Async Tools
```python
import asyncio
import httpx

@mcp.tool()
async def fetch_url(url: str) -> str:
    """Fetch content from URL."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text
```

## Testing

```python
# test_tools.py
import pytest
from my_server import mcp

def test_search_users():
    result = mcp.tools["search_users"](query="john")
    assert isinstance(result, list)
    assert len(result) > 0

def test_search_users_empty():
    result = mcp.tools["search_users"](query="nonexistent123")
    assert result == []

def test_search_users_invalid():
    with pytest.raises(ValueError):
        mcp.tools["search_users"](query="")
```

## Best Practices

1. **Single responsibility** - One tool does one thing well
2. **Idempotent reads** - GET-style tools should be safe to retry
3. **Explicit errors** - Raise clear exceptions with context
4. **Rate limiting** - Respect API limits, add delays if needed
5. **Timeouts** - Set reasonable timeouts for external calls
6. **Logging** - Log important events for debugging
7. **Security** - Never expose secrets in responses

## Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [FastMCP Docs](https://github.com/jlowin/fastmcp)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
