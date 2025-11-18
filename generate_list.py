import os
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Any


SKIP_DIRS = {".git", ".github", ".vscode", "node_modules", "__pycache__", ".netlify", "styles"}
SKIP_FILES = {"_redirects", "list.html", "generate_list.py", "netlify.toml", "view.html", "codathon2.html", "package-lock.json", "package.json", "tailwind.config.js", "README.md"}


Tree = Dict[str, Any]


def generate_list(folder: str = ".") -> None:
    """Generate a hierarchical list.html with expandable folders and file links."""
    

    def make_node() -> Tree:
        return {"dirs": {}, "files": []}

    def ensure_dir(root_node: Tree, parts: List[str]) -> Tree:
        node = root_node
        for part in parts:
            dirs = node["dirs"]  
            if part not in dirs:  
                dirs[part] = make_node()  
            node = dirs[part]  
        return node

    def insert_file(root_node: Tree, parts: List[str], filename: str) -> None:
        node = ensure_dir(root_node, parts)
        node["files"].append(filename)  

    
    tree: Tree = make_node()
    total_files = 0
    for root, dirs, files in os.walk(folder):
        
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]

        rel_root = os.path.relpath(root, folder)
        rel_root = "" if rel_root == "." else rel_root.replace("\\", "/")
        parts = [] if rel_root == "" else rel_root.split("/")

        
        ensure_dir(tree, parts)

        
        for d in dirs:
            if d in SKIP_DIRS or d.startswith("."):
                continue
            ensure_dir(tree, parts + [d])

        
        for name in files:
            if name in SKIP_FILES or name.startswith("."):
                continue
            insert_file(tree, parts, name)
            total_files += 1

    
    
    ist_tz = timezone(timedelta(hours=5, minutes=30), name="IST")
    updated = datetime.now(ist_tz).strftime("%Y-%m-%d %H:%M:%S IST (GMT+05:30)")
    total = total_files
    with open("list.html", "w", encoding="utf-8") as f:
        html_start = (
            """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Public Files</title>
        <link rel="stylesheet" href="styles/tailwind.css" />
        <script>
            (function() {
                try {
                    const stored = localStorage.getItem('uv-theme');
                    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                    if (stored === 'dark' || (!stored && prefersDark)) {
                        document.documentElement.classList.add('dark');
                    } else {
                        document.documentElement.classList.remove('dark');
                    }
                } catch (e) { /* no-op */ }
            })();
        </script>
    </head>
    <body class="bg-gray-50 text-gray-900 dark:bg-gray-900 dark:text-gray-100">
        <div class="min-h-screen">
            <header class="border-b border-gray-200 dark:border-gray-800">
                <div class="mx-auto max-w-5xl px-4 py-6 flex items-center justify-between gap-4">
                    <h1 class="text-2xl font-semibold tracking-tight">Public Files</h1>
                    <div class="flex items-center gap-3">
                        <span id="fileCount" class="text-sm text-gray-600 dark:text-gray-400">__TOTAL__ files</span>
                        <button id="themeToggle" class="inline-flex items-center gap-2 rounded-md border border-gray-300 dark:border-gray-700 px-3 py-1.5 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" aria-label="Toggle dark mode">
                            <span class="sr-only">Toggle dark mode</span>
                            <span id="iconSun" class="hidden dark:inline">☀️</span>
                            <span id="iconMoon" class="inline dark:hidden">🌙</span>
                            <span class="hidden sm:inline">Theme</span>
                        </button>
                    </div>
                </div>
            </header>
            <main class="mx-auto max-w-5xl px-4 py-6">
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                    <input id="q" type="search" placeholder="Filter files..." class="w-full sm:max-w-md rounded-md border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 px-3 py-2 shadow-sm placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500" />
                    <span class="text-xs text-gray-500">Updated: __UPDATED__</span>
                </div>
                <ul id="tree" class="mt-6 space-y-1">
""".strip()
        )
        f.write(html_start.replace("__UPDATED__", updated).replace("__TOTAL__", str(total)))

        
        import urllib.parse as _up

        def count_files(node: Tree) -> int:
            c = len(node["files"])  
            for child in node["dirs"].values():  
                c += count_files(child)  
            return c

        def write_dir(dir_name: str, node: Tree, base_path: str, level: int = 0) -> None:
            full_path = f"{base_path}/{dir_name}" if base_path else dir_name
            files_count = count_files(node)
            indent = "  " * (level + 1)
            f.write(
                f"\n      <li data-type=\"dir\" data-path=\"{full_path}\">"
                f"\n{indent}<details class=\"group\" >"
                f"\n{indent}  <summary class=\"flex items-center gap-2 rounded-md px-2 py-1.5 text-sm hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer\">"
                f"<span class=\"text-yellow-600 dark:text-yellow-400\">📁</span>"
                f"<span class=\"font-medium\">{dir_name}</span>"
                f"<span class=\"ml-2 rounded-full border border-gray-200 dark:border-gray-700 px-1.5 py-0.5 text-[11px] text-gray-600 dark:text-gray-300\">{files_count}</span>"
                f"</summary>"
            )
            f.write(f"\n{indent}  <ul class=\"ml-4 border-l border-gray-200 dark:border-gray-800 pl-3 space-y-1\">")

            
            for child_name in sorted(node["dirs"].keys(), key=lambda s: s.lower()):  
                write_dir(child_name, node["dirs"][child_name], full_path, level + 2)  

            
            for file_name in sorted(node["files"], key=lambda s: s.lower()):  
                rel = f"{full_path}/{file_name}" if full_path else file_name
                file_q = _up.quote(rel, safe="")
                f.write(
                    f"\n{indent}    <li data-type=\"file\" data-path=\"{rel}\">"
                    f"<a class=\"inline-flex items-center gap-2 rounded-md px-2 py-1.5 text-sm hover:bg-blue-50 hover:text-blue-700 dark:hover:bg-blue-900/30 transition-colors\" href=\"/view?file={file_q}\">"
                    f"<span class=\"text-gray-500\">📄</span><span>{file_name}</span>"
                    f"</a></li>"
                )

            f.write(f"\n{indent}  </ul>")
            f.write(f"\n{indent}</details>")
            f.write("\n      </li>")

        
        
        for file_name in sorted(tree["files"], key=lambda s: s.lower()):  
            rel = file_name
            file_q = _up.quote(rel, safe="")
            f.write(
                f"\n      <li data-type=\"file\" data-path=\"{rel}\">"
                f"<a class=\"inline-flex items-center gap-2 rounded-md px-2 py-1.5 text-sm hover:bg-blue-50 hover:text-blue-700 dark:hover:bg-blue-900/30 transition-colors\" href=\"/view?file={file_q}\">"
                f"<span class=\"text-gray-500\">📄</span><span>{file_name}</span>"
                f"</a></li>"
            )

        
        for dir_name in sorted(tree["dirs"].keys(), key=lambda s: s.lower()):  
            write_dir(dir_name, tree["dirs"][dir_name], base_path="", level=0)  

        f.write(
            """
                </ul>
                <script>
                    const q = document.getElementById('q');
                    const tree = document.getElementById('tree');
                    const fileCount = document.getElementById('fileCount');
                    const allFiles = () => Array.from(tree.querySelectorAll('li[data-type="file"]'));
                    const allDirs = () => Array.from(tree.querySelectorAll('li[data-type="dir"]'));
                    const total = allFiles().length;

                    function updateCount() {
                        const visible = allFiles().filter(li => li.offsetParent !== null).length;
                        fileCount.textContent = (visible === total) ? `${total} files` : `${visible} / ${total} files`;
                    }

                    function setVisibility(el, show) {
                        el.style.display = show ? '' : 'none';
                    }

                    function applyFilter() {
                        const term = (q.value || '').toLowerCase().trim();
                        if (!term) {
                            // reset: show all and collapse folders
                            allFiles().forEach(li => setVisibility(li, true));
                            allDirs().forEach(dir => {
                                setVisibility(dir, true);
                                const details = dir.querySelector('details');
                                if (details) details.open = false;
                            });
                            updateCount();
                            return;
                        }

                        // Hide all initially
                        allFiles().forEach(li => setVisibility(li, false));
                        allDirs().forEach(dir => setVisibility(dir, false));

                        // Show files that match
                        const matchingFiles = allFiles().filter(li => {
                            const path = (li.getAttribute('data-path') || '').toLowerCase();
                            const text = (li.textContent || '').toLowerCase();
                            return path.includes(term) || text.includes(term);
                        });
                        matchingFiles.forEach(li => setVisibility(li, true));

                        // Ensure ancestor folders are visible and opened
                        matchingFiles.forEach(li => {
                            let parent = li.parentElement;
                            while (parent && parent !== tree) {
                                if (parent.tagName.toLowerCase() === 'ul') {
                                    const dirLi = parent.closest('li[data-type="dir"]');
                                    if (dirLi) {
                                        setVisibility(dirLi, true);
                                        const details = dirLi.querySelector('details');
                                        if (details) details.open = true;
                                    }
                                }
                                parent = parent.parentElement;
                            }
                        });

                        // Also show/expand folders whose name matches term
                        allDirs().forEach(dir => {
                            const text = (dir.getAttribute('data-path') || dir.textContent || '').toLowerCase();
                            if (text.includes(term)) {
                                setVisibility(dir, true);
                                const details = dir.querySelector('details');
                                if (details) details.open = true;
                            }
                        });

                        updateCount();
                    }

                    q.addEventListener('input', applyFilter);
                    updateCount();

                    const toggle = document.getElementById('themeToggle');
                    const root = document.documentElement;
                    function setTheme(dark) {
                        if (dark) root.classList.add('dark'); else root.classList.remove('dark');
                        try { localStorage.setItem('uv-theme', dark ? 'dark' : 'light'); } catch (e) {}
                    }
                    toggle.addEventListener('click', () => {
                        const darkNow = !root.classList.contains('dark');
                        setTheme(darkNow);
                    });
                </script>
            </main>
        </div>
    </body>
</html>
"""
    )


if __name__ == "__main__":
    generate_list()
