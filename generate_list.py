import os

def generate_list(folder="."):
    entries = []
    for root, dirs, files in os.walk(folder):
        rel_root = os.path.relpath(root, folder)
        for name in files:
            if name == "_redirects" or name == "list.html":
                continue
            path = os.path.join(rel_root, name).replace("\\", "/")
            entries.append(path)

    entries.sort()
    with open("list.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html><html><head><title>File List</title></head><body><h1>Public Files</h1><ul>")
        for entry in entries:
            f.write(f'<li><a href="{entry}">{entry}</a></li>')
        f.write("</ul></body></html>")

if __name__ == "__main__":
    generate_list()
