#!/usr/bin/env python3
"""Fetch GitBook content and convert to markdown files."""
import json
import os
import ssl
import time
import urllib.request
import urllib.error

ssl._create_default_https_context = ssl._create_unverified_context

TOKEN = "gb_api_f84ZNSSSfAoDfavWWDjkFzq0WisGpxHyFxRddlay"
SPACE_ID = "6iQTvxgRZRwPS1NgIGEb"
BASE_URL = "https://api.gitbook.com/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def node_to_md(node, depth=0):
    t = node.get("type", "")
    nodes = node.get("nodes", [])

    def children_text():
        return "".join(node_to_md(n, depth) for n in nodes)

    if node.get("object") == "text":
        text = "".join(leaf.get("text", "") for leaf in node.get("leaves", []))
        marks = []
        for leaf in node.get("leaves", []):
            marks = [m.get("type") for m in leaf.get("marks", [])]
        if "bold" in marks:
            text = f"**{text}**"
        if "italic" in marks:
            text = f"*{text}*"
        if "code" in marks:
            text = f"`{text}`"
        return text

    if t == "paragraph":
        return children_text() + "\n\n"
    if t == "heading-1":
        return f"# {children_text()}\n\n"
    if t == "heading-2":
        return f"## {children_text()}\n\n"
    if t == "heading-3":
        return f"### {children_text()}\n\n"
    if t == "heading-4":
        return f"#### {children_text()}\n\n"
    if t == "list-unordered":
        items = []
        for li in nodes:
            li_text = "".join(node_to_md(n, depth) for n in li.get("nodes", []))
            items.append(f"- {li_text.strip()}")
        return "\n".join(items) + "\n\n"
    if t == "list-ordered":
        items = []
        for i, li in enumerate(nodes, 1):
            li_text = "".join(node_to_md(n, depth) for n in li.get("nodes", []))
            items.append(f"{i}. {li_text.strip()}")
        return "\n".join(items) + "\n\n"
    if t == "list-item":
        return children_text()
    if t == "blockquote":
        content = children_text().strip()
        return "\n".join(f"> {line}" for line in content.splitlines()) + "\n\n"
    if t in ("code", "code-block"):
        lang = node.get("data", {}).get("syntax", "")
        code = children_text().strip()
        return f"```{lang}\n{code}\n```\n\n"
    if t == "hint":
        style = node.get("data", {}).get("style", "info")
        content = children_text().strip()
        return f"> **{style.upper()}:** {content}\n\n"
    if t == "image":
        src = node.get("data", {}).get("src", "")
        alt = node.get("data", {}).get("alt", "")
        return f"![{alt}]({src})\n\n"
    if t == "link":
        href = node.get("data", {}).get("href", "")
        text = children_text().strip()
        return f"[{text}]({href})"
    if t == "divider":
        return "---\n\n"
    if t == "table":
        return "_[Table content - see GitBook for full view]_\n\n"
    if t in ("tabs", "tab"):
        return children_text()
    if t == "expandable":
        title_nodes = node.get("data", {}).get("title", "")
        return f"**{title_nodes}**\n\n{children_text()}"

    # fallback
    return children_text()

def doc_to_markdown(page):
    title = page.get("title", "")
    description = page.get("description", "")
    doc = page.get("document", {})
    nodes = doc.get("nodes", [])

    parts = [f"# {title}\n\n"]
    if description:
        parts.append(f"{description}\n\n")
    for node in nodes:
        parts.append(node_to_md(node))
    return "".join(parts).strip() + "\n"

def slug_to_path(path_str):
    """Convert GitBook path to file path under docs/"""
    return f"docs/{path_str}.md"

def ensure_dir(filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

# Load full structure
print("Fetching space structure...")
structure = fetch(f"{BASE_URL}/spaces/{SPACE_ID}/content")

def collect_pages(pages, result=None):
    if result is None:
        result = []
    for p in pages:
        result.append(p)
        if p.get("pages"):
            collect_pages(p["pages"], result)
    return result

all_pages = collect_pages(structure["pages"])
sheets = [p for p in all_pages if p.get("kind") == "sheet" and p.get("path")]
groups = [p for p in all_pages if p.get("kind") == "group"]

print(f"Found {len(sheets)} pages, {len(groups)} groups")

# Fetch and write each page
failed = []
for i, page in enumerate(sheets):
    page_id = page["id"]
    path = page["path"]
    filepath = slug_to_path(path)
    print(f"[{i+1}/{len(sheets)}] {path}")

    try:
        full_page = fetch(f"{BASE_URL}/spaces/{SPACE_ID}/content/page/{page_id}")
        md = doc_to_markdown(full_page)
        ensure_dir(filepath)
        with open(filepath, "w") as f:
            f.write(md)
        time.sleep(0.1)  # rate limit
    except Exception as e:
        print(f"  ERROR: {e}")
        failed.append(path)
        # Write stub
        ensure_dir(filepath)
        with open(filepath, "w") as f:
            f.write(f"# {page.get('title', path)}\n\n_Content coming soon._\n")

# Build SUMMARY.md
print("\nBuilding SUMMARY.md...")

def build_summary(pages, indent=0):
    lines = []
    for p in pages:
        title = p["title"]
        kind = p.get("kind", "sheet")
        path = p.get("path", "")
        slug = p.get("slug", "")
        prefix = "  " * indent

        if kind == "group":
            lines.append(f"{prefix}## {title}\n")
            if p.get("pages"):
                lines.extend(build_summary(p["pages"], indent))
        else:
            if path:
                lines.append(f"{prefix}* [{title}]({path}.md)")
            else:
                lines.append(f"{prefix}* {title}")

        if p.get("pages") and kind != "group":
            lines.extend(build_summary(p["pages"], indent + 1))

    return lines

summary_lines = ["# Table of Contents\n"]
summary_lines.extend(build_summary(structure["pages"]))

with open("docs/SUMMARY.md", "w") as f:
    f.write("\n".join(summary_lines) + "\n")

# Write .gitbook.yaml
with open(".gitbook.yaml", "w") as f:
    f.write("root: ./docs\n")

print(f"\nDone. Failed: {failed}")
print("Files ready in docs/")
