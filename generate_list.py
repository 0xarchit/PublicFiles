import os
from datetime import datetime
from typing import List


SKIP_DIRS = {".git", ".github", ".vscode", "node_modules", "__pycache__", ".netlify"}
SKIP_FILES = {"_redirects", "list.html", "generate_list.py"}


def generate_list(folder: str = ".") -> None:
    entries: List[str] = []
    for root, dirs, files in os.walk(folder):
        # prune unwanted dirs in-place for performance and correctness
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]

        rel_root = os.path.relpath(root, folder)
        rel_root = "" if rel_root == "." else rel_root.replace("\\", "/")

        for name in files:
            if name in SKIP_FILES or name.startswith("."):
                continue

            path = f"{rel_root}/{name}" if rel_root else name
            path = path.replace("\\", "/")
            entries.append(path)

    entries.sort(key=lambda p: p.lower())

    # Write HTML
    updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    with open("list.html", "w", encoding="utf-8") as f:
        html_start = (
            """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Public Files</title>
        <style>
            body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:2rem;}
            header{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;flex-wrap:wrap}
            input[type="search"]{padding:.5rem .75rem;border:1px solid #ccc;border-radius:6px;min-width:18rem}
            ul{list-style:none;padding-left:0}
            li{margin:.25rem 0}
            a{color:#1a73e8;text-decoration:none}
            a:hover{text-decoration:underline}
            .muted{color:#666;font-size:.9rem}
        </style>
    </head>
    <body>
        <header>
            <h1>Public Files</h1>
            <input id="q" type="search" placeholder="Filter files..." />
        </header>
    <p class="muted">Updated: __UPDATED__</p>
        <ul id="list">
""".strip()
        )
        f.write(html_start.replace("__UPDATED__", updated))

        for entry in entries:
            href = "/" + entry  # absolute path from site root (Netlify)
            f.write(f"\n      <li><a href=\"{href}\">{entry}</a></li>")

        f.write(
            """
        </ul>
        <script>
            const q = document.getElementById('q');
            const list = document.getElementById('list');
            q.addEventListener('input', () => {
                const term = q.value.toLowerCase();
                for (const li of list.children) {
                    const text = li.textContent.toLowerCase();
                    li.style.display = text.includes(term) ? '' : 'none';
                }
            });
        </script>
    </body>
</html>
"""
                )


if __name__ == "__main__":
    generate_list()
