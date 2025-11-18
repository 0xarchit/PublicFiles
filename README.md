# PublicFiles

A modern file browser and viewer application for managing and accessing public documents. Built with Python, Tailwind CSS, and hosted on Netlify.

## Overview

PublicFiles is a sophisticated file management system that provides:

- **Dynamic File Listing**: Automatically generates an interactive HTML file browser from your directory structure
- **Multi-Format Viewer**: Supports PDFs, images, videos, audio, spreadsheets, documents, Markdown, JSON, and more
- **Dark Mode Support**: Built-in theme toggle for light and dark interfaces
- **Search & Filter**: Quick search functionality to find files in your collection
- **Responsive Design**: Fully responsive UI that works on desktop, tablet, and mobile devices
- **Zero Dependencies Server-Side**: Pure Python build process for generating the file listing

## Features

### File Browser (`list.html`)
- Hierarchical expandable folder structure
- File count indicators
- File path-based search filtering
- Dark/light theme toggle
- Search with live filtering
- Auto-generated file counts

### File Viewer (`view.html`)
- **Document Formats**:
  - PDF with zoom, pan, and page navigation
  - Microsoft Office (DOCX, XLSX, PPTX)
  - Legacy Word Documents (DOC)
  - Markdown with LaTeX math support
  - JSON with tree visualization

- **Media Files**:
  - Images (JPG, PNG, SVG, WebP, etc.)
  - Video (MP4, WebM, OGG, etc.)
  - Audio (MP3, WAV, OGG, etc.)

- **Data Files**:
  - CSV with table preview
  - Excel spreadsheets with multi-sheet support

- **Diagrams**:
  - Mermaid diagrams (flowcharts, sequences, etc.)
  - SVG graphics

- **Code Files**:
  - Syntax-highlighted code blocks
  - Plain text with formatting

### Advanced Features
- **PDF Zoom Overlay**: Click PDFs to open in a zoomable, pannable modal
- **LaTeX Math Rendering**: KaTeX support for mathematical expressions
- **Theme Persistence**: Remembers user's theme preference
- **Responsive Grid**: Dynamic table rendering for large datasets
- **Error Handling**: Graceful fallbacks for unsupported formats
- **File Metadata**: Display file type, size, and last updated timestamp

## Project Structure

```
PublicFiles/
├── generate_list.py          # Build script to generate file listing
├── netlify.toml              # Netlify deployment config
├── view.html                 # Universal file viewer
├── list.html                 # Generated file browser (auto-created)
├── _redirects                # URL redirect rules
├── styles/
│   └── tailwind.css         # Compiled Tailwind CSS
└── README.md                 # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js and npm (for Tailwind CSS)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/0xarchit/PublicFiles.git
cd PublicFiles
```

2. Install Node dependencies:
```bash
npm install
```

3. (Optional) Build Tailwind CSS:
```bash
npm run build:css
```

### Running Locally

1. Generate the file listing:
```bash
python generate_list.py
```

This creates/updates `list.html` with your current directory structure.

2. Open in a web browser:
   - Open `list.html` to browse your files
   - Click any file to view it in `view.html`

### Customization

#### Excluding Directories

Edit the `SKIP_DIRS` set in `generate_list.py`:
```python
SKIP_DIRS = {".git", ".github", ".vscode", "node_modules", "__pycache__", ".netlify", "styles"}
```

#### Excluding Files

Edit the `SKIP_FILES` set in `generate_list.py`:
```python
SKIP_FILES = {"_redirects", "list.html", "generate_list.py", "netlify.toml", "view.html", "codathon2.html", "package-lock.json", "package.json", "tailwind.config.js"}
```

#### Styling

Modify `styles/tailwind-input.css` and rebuild:
```bash
npm run build:css
```

## Deployment

### Netlify Deployment

The project is configured for automatic deployment on Netlify:

1. Connect your GitHub repository to Netlify
2. Netlify uses the `netlify.toml` configuration
3. On every push, the build runs `python generate_list.py`
4. The entire directory is published

**Build Command**: `python generate_list.py`  
**Publish Directory**: `.` (root)

### Environment Variables

- `PYTHON_VERSION = 3.11` (configured in netlify.toml)

## Usage

### Viewing Files

1. Open `list.html` to see the file browser
2. Use the search box to filter files
3. Click on any file to open it in the viewer
4. The viewer automatically detects file type and renders appropriately

### PDF Viewing

- Click on PDF canvas to open in zoom overlay
- Use zoom buttons or scroll to zoom in/out
- Use arrow buttons to navigate pages
- Press ESC or click close button to exit


## Technologies Used

- **Backend**: Python 3.11+
- **Frontend**: 
  - HTML5
  - CSS3 with Tailwind CSS
  - Vanilla JavaScript (no framework)
  
- **Libraries** (CDN-based):
  - marked.js - Markdown rendering
  - DOMPurify - HTML sanitization
  - Papa Parse - CSV parsing
  - pdf.js - PDF rendering
  - Mermaid - Diagram rendering
  - XLSX - Spreadsheet parsing
  - Mammoth - DOCX conversion
  - KaTeX - Math rendering
  - JSZip - ZIP file handling

- **Deployment**: Netlify

## File Size Limits

- **Spreadsheet Preview**: Limited to first 200 rows
- **PDF**: Rendered via pdf.js with full page support
- **Video/Audio**: Limited by browser capabilities

## Browser Support

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance

- **Build Time**: ~1 second (Python file scanning)
- **File Listing**: Generated on each build
- **Lazy Loading**: Assets loaded on demand
- **Minified CSS**: Optimized Tailwind CSS
- **CDN**: All heavy libraries served via CDN

## Author

0xArchit

---