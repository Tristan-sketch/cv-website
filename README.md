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

## Build a static version

```bash
python build.py
```

This writes plain HTML and CSS into `build/`. That folder can be hosted on any static host, for example GitHub Pages or Netlify, without running Python on the server.

## Project structure

```
app.py          # Flask app and the menu
cv_data.py      # All content of the CV
pixel_art.py    # Pixel sprites, rendered as SVG
build.py        # Renders the site into build/
templates/      # HTML template (Jinja)
static/         # CSS and a small script for the clock, typing effect and d-pad
```
