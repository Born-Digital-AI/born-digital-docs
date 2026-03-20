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
ASSETS_DIR = "docs/.gitbook/assets"
page_id_map = {}  # pageId -> path (populated after structure fetch)

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def download_file(url, dest_path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        with open(dest_path, "wb") as f:
            f.write(r.read())

# --- Download all files and build fileId -> local path map ---
print("Fetching files list...")
os.makedirs(ASSETS_DIR, exist_ok=True)

file_map = {}  # fileId -> relative markdown path
all_files = []
url = f"{BASE_URL}/spaces/{SPACE_ID}/content/files"
while url:
    data = fetch(url)
    all_files.extend(data.get("items", []))
    next_page = data.get("next", {})
    url = next_page.get("url") if next_page else None

print(f"Found {len(all_files)} files, downloading...")
for file in all_files:
    file_id = file["id"]
    name = file["name"]
    download_url = file["downloadURL"]
    dest = os.path.join(ASSETS_DIR, name)

    # handle duplicate filenames
    if os.path.exists(dest):
        base, ext = os.path.splitext(name)
        dest = os.path.join(ASSETS_DIR, f"{base}_{file_id[:6]}{ext}")
        name = os.path.basename(dest)

    print(f"  Downloading {name} ({file.get('size', 0) / 1024 / 1024:.1f}MB)...")
    try:
        download_file(download_url, dest)
        file_map[file_id] = f".gitbook/assets/{name}"
    except Exception as e:
        print(f"  ERROR downloading {name}: {e}")
        file_map[file_id] = ""

print(f"Downloaded {len(file_map)} files.\n")

# --- Markdown conversion ---
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
    if t == "images":
        # container for one or more image nodes
        return children_text()
    if t == "image":
        alt = node.get("data", {}).get("alt", "")
        ref = node.get("data", {}).get("ref", {})
        src = ""
        if ref.get("kind") == "file":
            file_id = ref.get("file", "")
            src = file_map.get(file_id, "")
        if not src:
            src = node.get("data", {}).get("src", "")
        return f"![{alt}]({src})\n\n"
    if t == "link":
        data = node.get("data", {})
        href = data.get("href", "")
        ref = data.get("ref", {})
        if not href and ref.get("kind") == "page":
            page_path = page_id_map.get(ref.get("page", ""), "")
            href = f"../{page_path}.md" if page_path else ""
        text = children_text().strip()
        return f"[{text}]({href})" if text else ""
    if t == "divider":
        return "---\n\n"
    if t == "table":
        data = node.get("data", {})
        definition = data.get("definition", {})
        records = data.get("records", {})
        view = data.get("view", {})
        columns = view.get("columns", list(definition.keys()))
        fragments_list = node.get("fragments", [])

        # build fragmentId -> nodes map (skip non-string fragment keys)
        frag_map = {f["fragment"]: f["nodes"] for f in fragments_list if "fragment" in f and isinstance(f["fragment"], str)}

        # sort records by orderIndex
        sorted_records = sorted(records.items(), key=lambda x: x[1].get("orderIndex", ""))

        if not sorted_records:
            return ""

        # build header row from column titles (empty string if no title)
        headers = [definition.get(col, {}).get("title", "") or "" for col in columns]

        # render each record
        rows = []
        for rec_id, rec in sorted_records:
            cells = []
            for col in columns:
                frag_id = rec.get("values", {}).get(col, "")
                if isinstance(frag_id, dict):
                    # page/anchor reference — skip, cell content is in fragment nodes
                    cell_md = ""
                else:
                    frag_nodes = frag_map.get(frag_id, [])
                    cell_md = "".join(node_to_md(n, depth) for n in frag_nodes).strip().replace("\n", " ")
                cells.append(cell_md)
            rows.append(cells)

        # assemble markdown table
        lines = []
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows:
            lines.append("| " + " | ".join(row) + " |")
        return "\n".join(lines) + "\n\n"
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
    return f"docs/{path_str}.md"

def ensure_dir(filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

# --- Fetch and write pages ---
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

# populate page_id_map for link resolution
for p in all_pages:
    if p.get("id") and p.get("path"):
        page_id_map[p["id"]] = p["path"]

print(f"Found {len(sheets)} pages, {len(groups)} groups")

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
        time.sleep(0.1)
    except Exception as e:
        print(f"  ERROR: {e}")
        failed.append(path)
        ensure_dir(filepath)
        with open(filepath, "w") as f:
            f.write(f"# {page.get('title', path)}\n\n_Content coming soon._\n")

# --- Build SUMMARY.md ---
print("\nBuilding SUMMARY.md...")

def build_summary(pages, indent=0):
    lines = []
    for p in pages:
        title = p["title"]
        kind = p.get("kind", "sheet")
        path = p.get("path", "")
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

with open(".gitbook.yaml", "w") as f:
    f.write("root: ./docs\n")

print(f"\nDone. Failed: {failed}")
print("Files ready in docs/")
