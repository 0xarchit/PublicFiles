import os
from datetime import datetime, timezone, timedelta
from typing import List


SKIP_DIRS = {".git", ".github", ".vscode", "node_modules", "__pycache__", ".netlify"}
SKIP_FILES = {"_redirects", "list.html", "generate_list.py", "netlify.toml"}


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
    # Show time in India Standard Time (GMT+05:30)
    ist_tz = timezone(timedelta(hours=5, minutes=30), name="IST")
    updated = datetime.now(ist_tz).strftime("%Y-%m-%d %H:%M:%S IST (GMT+05:30)")
    total = len(entries)
    with open("list.html", "w", encoding="utf-8") as f:
        html_start = (
            """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Public Files</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        <script>
            (function() {
                try {
                    const stored = localStorage.getItem('theme');
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
                <ul id="list" class="mt-6 grid gap-2">
""".strip()
        )
        f.write(html_start.replace("__UPDATED__", updated).replace("__TOTAL__", str(total)))

        for entry in entries:
            href = "/" + entry  # absolute path from site root (Netlify)
            f.write(f"\n      <li><a href=\"{href}\">{entry}</a></li>")

        f.write(
            """
                </ul>
                <script>
                    const q = document.getElementById('q');
                    const list = document.getElementById('list');
                    const fileCount = document.getElementById('fileCount');
                    const total = list.children.length;

                    function updateCount() {
                        let visible = 0;
                        for (const li of list.children) {
                            if (li.style.display !== 'none') visible++;
                        }
                        fileCount.textContent = (visible === total) ? `${total} files` : `${visible} / ${total} files`;
                    }

                    q.addEventListener('input', () => {
                        const term = q.value.toLowerCase();
                        for (const li of list.children) {
                            const text = li.textContent.toLowerCase();
                            li.style.display = text.includes(term) ? '' : 'none';
                        }
                        updateCount();
                    });

                    updateCount();

                    const toggle = document.getElementById('themeToggle');
                    const root = document.documentElement;
                    function setTheme(dark) {
                        if (dark) root.classList.add('dark'); else root.classList.remove('dark');
                        try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
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
