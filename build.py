"""Render the website into static files in the build/ folder.

The result can be hosted anywhere that serves plain files, for example
GitHub Pages or Netlify, without running Python on the server.

    python build.py
"""

import shutil
from pathlib import Path

from app import app

ROOT = Path(__file__).parent
BUILD = ROOT / "build"


def main():
    if BUILD.exists():
        shutil.rmtree(BUILD)
    shutil.copytree(ROOT / "static", BUILD / "static")

    pages = {"/": "index.html", "/datenschutz.html": "datenschutz.html"}
    with app.test_client() as client:
        for route, filename in pages.items():
            response = client.get(route)
            if response.status_code != 200:
                raise SystemExit(f"Rendering {route} failed with status {response.status_code}")
            (BUILD / filename).write_bytes(response.data)

    print(f"Website built into {BUILD}")


if __name__ == "__main__":
    main()
