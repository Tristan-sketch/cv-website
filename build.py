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

    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise SystemExit(f"Rendering failed with status {response.status_code}")
        (BUILD / "index.html").write_bytes(response.data)

    print(f"Website built into {BUILD}")


if __name__ == "__main__":
    main()
