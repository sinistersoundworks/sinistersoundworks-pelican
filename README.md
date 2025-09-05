# Sinister Soundworks Website

This is the official website for Sinister Soundworks, built with Pelican static site generator.

## Development

### Prerequisites
- Python 3.11+
- pip

### Setup
```bash
pip install -r requirements.txt
```

### Local Development
```bash
# Start development server with auto-reload
make devserver

# Build site
make html

# Clean build
make clean && make html

# Build for production
make publish
```

### Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the main branch.

## Project Structure

- `content/` - Site content (articles, pages, assets)
- `themes/sinister/` - Custom theme templates and assets
- `pelicanconf.py` - Development configuration
- `publishconf.py` - Production configuration
- `requirements.txt` - Python dependencies

## Features

- Responsive design with Bootstrap
- Audio portfolio with Plyr player
- Smooth scrolling navigation
- Dynamic navbar background on scroll
- FAQ page with mixing preparation guide
- Social media integration
- SEO optimized
