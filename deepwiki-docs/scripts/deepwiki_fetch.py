#!/usr/bin/env python3
"""
DeepWiki Docs Fetcher - Fetch documentation from deepwiki.com for any GitHub repository.

Supports two modes:
1. Web scraping: Fetch and parse deepwiki.com pages directly
2. MCP API: Call the DeepWiki MCP server endpoints

Usage:
    python deepwiki_fetch.py structure <owner/repo>
    python deepwiki_fetch.py content <owner/repo> [page_path]
    python deepwiki_fetch.py export <owner/repo> [--output <file>]
    python deepwiki_fetch.py ask <owner/repo> "<question>"
"""

import sys
import json
import re
import argparse
import urllib.request
import urllib.error
from html.parser import HTMLParser
from typing import Optional


# ─── HTML Parser for DeepWiki pages ───────────────────────────────────────────

class DeepWikiHTMLParser(HTMLParser):
    """Parse DeepWiki HTML pages to extract structured content."""

    def __init__(self):
        super().__init__()
        self.links = []          # sidebar nav links
        self.content_parts = []  # main content text
        self.in_nav = False
        self.in_content = False
        self.current_tag = None
        self.current_attrs = {}
        self.skip_tags = {'script', 'style', 'noscript', 'svg', 'path'}
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.current_tag = tag
        self.current_attrs = attrs_dict

        if tag in self.skip_tags:
            self.skip_depth += 1
            return

        # Collect sidebar navigation links (wiki structure)
        if tag == 'a' and 'href' in attrs_dict:
            href = attrs_dict['href']
            # DeepWiki sidebar links follow pattern: /<owner>/<repo>/<page>
            if re.match(r'^/[^/]+/[^/]+/[\w.-]+', href):
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.skip_depth > 0:
            self.skip_depth -= 1

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        text = data.strip()
        if text and text != 'Loading...':
            self.content_parts.append(text)


# ─── Core Functions ───────────────────────────────────────────────────────────

def fetch_url(url: str, timeout: int = 30) -> str:
    """Fetch URL content with error handling."""
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; DeepWikiSkill/1.0)',
        'Accept': 'text/html,application/json',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        if e.code == 404:
            print("Repository may not be indexed on DeepWiki. Visit https://deepwiki.com to index it.", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def fetch_wiki_structure(owner_repo: str) -> list[dict]:
    """
    Fetch the wiki structure (table of contents) for a repository.
    Returns a list of {title, path, url} dicts.
    """
    url = f"https://deepwiki.com/{owner_repo}"
    html = fetch_url(url)

    parser = DeepWikiHTMLParser()
    parser.feed(html)

    # Deduplicate and filter links
    seen = set()
    structure = []
    prefix = f"/{owner_repo}/"

    for href in parser.links:
        if href.startswith(prefix) and href not in seen:
            seen.add(href)
            # Extract page slug and create a readable title
            slug = href[len(prefix):]
            # Convert slug like "4.1-fiber-architecture" to "Fiber Architecture"
            title = re.sub(r'^\d+(\.\d+)*-?', '', slug)
            title = title.replace('-', ' ').replace('(', '(').replace(')', ')').strip()
            title = title.title() if title else slug
            structure.append({
                'title': title,
                'slug': slug,
                'path': href,
                'url': f"https://deepwiki.com{href}"
            })

    return structure


def fetch_wiki_page(owner_repo: str, page_slug: str) -> dict:
    """
    Fetch a single wiki page's content.
    Returns {title, url, content} dict.
    """
    url = f"https://deepwiki.com/{owner_repo}/{page_slug}"
    html = fetch_url(url)

    parser = DeepWikiHTMLParser()
    parser.feed(html)

    content = '\n'.join(parser.content_parts)

    return {
        'title': page_slug,
        'url': url,
        'content': content
    }


def export_wiki_structure(owner_repo: str, output_path: Optional[str] = None) -> str:
    """
    Export the full wiki structure as a formatted markdown index.
    Optionally saves to a file.
    """
    structure = fetch_wiki_structure(owner_repo)

    lines = [
        f"# DeepWiki Documentation Index: {owner_repo}",
        "",
        f"Source: https://deepwiki.com/{owner_repo}",
        f"Total pages: {len(structure)}",
        "",
        "## Table of Contents",
        ""
    ]

    for i, page in enumerate(structure, 1):
        indent = ""
        # Detect hierarchy from slug numbering (e.g., "1-overview", "1.1-core-types")
        slug = page['slug']
        match = re.match(r'^(\d+(?:\.\d+)*)', slug)
        if match:
            depth = match.group(1).count('.')
            indent = "  " * depth
        lines.append(f"{indent}{i}. [{page['title']}]({page['url']})")

    result = '\n'.join(lines)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Exported to: {output_path}", file=sys.stderr)

    return result


def build_knowledge_index(owner_repo: str, output_path: Optional[str] = None) -> str:
    """
    Build a comprehensive LLM knowledge document by fetching all wiki pages.
    This creates a single markdown document with all documentation content.
    """
    structure = fetch_wiki_structure(owner_repo)

    lines = [
        f"# {owner_repo} - Complete Documentation",
        "",
        f"Source: https://deepwiki.com/{owner_repo}",
        f"Pages: {len(structure)}",
        "",
        "---",
        ""
    ]

    for page in structure:
        print(f"  Fetching: {page['slug']}...", file=sys.stderr)
        try:
            page_data = fetch_wiki_page(owner_repo, page['slug'])
            lines.append(f"## {page['title']}")
            lines.append(f"_Source: {page['url']}_")
            lines.append("")
            lines.append(page_data['content'])
            lines.append("")
            lines.append("---")
            lines.append("")
        except Exception as e:
            lines.append(f"## {page['title']}")
            lines.append(f"_Error fetching: {e}_")
            lines.append("")

    result = '\n'.join(lines)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Knowledge index exported to: {output_path}", file=sys.stderr)

    return result


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Fetch documentation from DeepWiki for GitHub repositories'
    )
    sub = parser.add_subparsers(dest='command', required=True)

    # structure
    p_struct = sub.add_parser('structure', help='Get wiki table of contents')
    p_struct.add_argument('repo', help='owner/repo (e.g. facebook/react)')

    # content
    p_content = sub.add_parser('content', help='Get a specific wiki page')
    p_content.add_argument('repo', help='owner/repo')
    p_content.add_argument('page', nargs='?', default=None, help='Page slug (e.g. 1-overview)')

    # export
    p_export = sub.add_parser('export', help='Export wiki structure as markdown index')
    p_export.add_argument('repo', help='owner/repo')
    p_export.add_argument('--output', '-o', help='Output file path')

    # index
    p_index = sub.add_parser('index', help='Build full LLM knowledge document')
    p_index.add_argument('repo', help='owner/repo')
    p_index.add_argument('--output', '-o', help='Output file path')

    # ask (placeholder — requires MCP or direct API)
    p_ask = sub.add_parser('ask', help='Ask a question about a repository (via web)')
    p_ask.add_argument('repo', help='owner/repo')
    p_ask.add_argument('question', help='Your question')

    args = parser.parse_args()

    if args.command == 'structure':
        structure = fetch_wiki_structure(args.repo)
        print(json.dumps(structure, indent=2, ensure_ascii=False))

    elif args.command == 'content':
        if args.page:
            page = fetch_wiki_page(args.repo, args.page)
        else:
            # Fetch overview (first page)
            structure = fetch_wiki_structure(args.repo)
            if structure:
                page = fetch_wiki_page(args.repo, structure[0]['slug'])
            else:
                print("No pages found.", file=sys.stderr)
                sys.exit(1)
        print(json.dumps(page, indent=2, ensure_ascii=False))

    elif args.command == 'export':
        result = export_wiki_structure(args.repo, args.output)
        if not args.output:
            print(result)

    elif args.command == 'index':
        output = args.output or f"{args.repo.replace('/', '_')}_docs.md"
        build_knowledge_index(args.repo, output)
        print(f"Done. Knowledge index saved to: {output}")

    elif args.command == 'ask':
        # Use web_fetch on the repo's DeepWiki page as fallback
        print(f"To ask questions, use the DeepWiki MCP server or visit:")
        print(f"  https://deepwiki.com/{args.repo}")
        print(f"\nQuestion: {args.question}")
        print("\nTip: For programmatic Q&A, configure the DeepWiki MCP server:")
        print("  URL: https://mcp.deepwiki.com/mcp")


if __name__ == '__main__':
    main()
