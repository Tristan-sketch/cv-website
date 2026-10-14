# cv-website

My CV as a website, built with Python and Flask. The design is inspired by small hacker gadgets: a dark page, an orange pixel screen and a d-pad you can actually use.

## Run it locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Change the content

All texts live in [`cv_data.py`](cv_data.py): profile, skills, experience, projects, education and contact links. Values in `[square brackets]` are placeholders.

The pixel art (avatar and icons) is drawn in [`pixel_art.py`](pixel_art.py) as rows of `#` and `.`. Change a row and the drawing changes.

Every claim points to a source in `SOURCES`. The site turns this into an audit trail ("Prüfpfad"): each item gets a reference like B1, listed with its source at the end of the page.

Before publishing, set `SITE_URL` (for link previews and the print footer), `HOSTING_PROVIDER` and, if you need one, `IMPRESSUM` in `cv_data.py`.

## Images

`python make_images.py` draws the link preview (`static/og.png`) and the favicon from the same pixel sprites, with a small built-in pixel font. Run it again after changing the avatar.

## Build a static version

```bash
python build.py
```

This writes plain HTML and CSS into `build/`. That folder can be hosted on any static host, for example GitHub Pages or Netlify, without running Python on the server.

## Project structure

```
app.py          # Flask app: menu, audit trail, study progress, screen readouts
cv_data.py      # All content of the CV, its sources and the glossary
pixel_art.py    # Pixel sprites, rendered as SVG
make_images.py  # Draws og.png and the favicon with Pillow
build.py        # Renders the site into build/
templates/      # HTML templates (Jinja): CV page and privacy page
static/         # CSS, local fonts (OFL), images and a small script for the device
```
