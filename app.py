from datetime import date

from flask import Flask, render_template

import cv_data
from pixel_art import pixel_svg

app = Flask(__name__)
app.jinja_env.globals["pixel"] = pixel_svg

# The menu on the device screen. Each entry links to a section on the page.
MENU = [
    {"id": "about", "label": "Über mich", "icon": "user"},
    {"id": "skills", "label": "Skills", "icon": "terminal"},
    {"id": "experience", "label": "Erfahrung", "icon": "briefcase"},
    {"id": "projects", "label": "Projekte", "icon": "star"},
    {"id": "education", "label": "Ausbildung", "icon": "cap"},
    {"id": "contact", "label": "Kontakt", "icon": "mail"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        menu=MENU,
        profile=cv_data.PROFILE,
        skills=cv_data.SKILLS,
        experience=cv_data.EXPERIENCE,
        projects=cv_data.PROJECTS,
        education=cv_data.EDUCATION,
        fun_facts=cv_data.FUN_FACTS,
        contact=cv_data.CONTACT,
        year=date.today().year,
    )


if __name__ == "__main__":
    app.run(debug=True)
