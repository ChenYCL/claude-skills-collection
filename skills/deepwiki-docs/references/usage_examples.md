# DeepWiki Docs - Usage Examples

## Example 1: Quick Library Lookup

**User:** "How does React's hooks system work internally?"

**Workflow:**
1. Fetch structure: `python scripts/deepwiki_fetch.py structure facebook/react`
2. Identify relevant page: `4.3-react-hooks-system`
3. Fetch content: `python scripts/deepwiki_fetch.py content facebook/react 4.3-react-hooks-system`
4. Summarize the content for the user

## Example 2: Build Knowledge Index

**User:** "Create a comprehensive reference doc for the FastAPI library"

**Workflow:**
1. Fetch structure first to confirm repo is indexed
2. Run: `python scripts/deepwiki_fetch.py index tiangolo/fastapi --output fastapi_docs.md`
3. Present the generated markdown document

## Example 3: Architecture Overview

**User:** "What's the architecture of LangChain?"

**Workflow:**
1. Use `web_fetch` on `https://deepwiki.com/langchain-ai/langchain` to get the overview
2. Parse the sidebar for the full table of contents
3. Fetch the overview and architecture pages
4. Synthesize a concise architecture summary

## Example 4: Compare Approaches in Documentation

**User:** "How does Next.js handle routing vs Remix?"

**Workflow:**
1. Fetch structure for both `vercel/next.js` and `remix-run/remix`
2. Find routing-related pages in each
3. Fetch those specific pages
4. Compare and summarize

## Example 5: Using web_fetch Directly (No Script)

When the script is not needed, use `web_fetch` directly:

```
# Get repo overview and structure
web_fetch("https://deepwiki.com/{owner}/{repo}")

# Get specific page
web_fetch("https://deepwiki.com/{owner}/{repo}/{page-slug}")
```

Parse the HTML to extract sidebar links (structure) and main content (documentation).

## Example 6: Find Docs for a Website's Tech Stack

**User:** "Find all documentation for the shadcn/ui library"

**Workflow:**
1. `python scripts/deepwiki_fetch.py export shadcn-ui/ui --output shadcn_toc.md`
2. Present the TOC to user
3. Fetch specific pages as requested
