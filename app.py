import copy
from datetime import date

from flask import Flask, render_template

import cv_data
from pixel_art import pixel_svg

app = Flask(__name__)
app.jinja_env.globals["pixel"] = pixel_svg

# The menu on the device screen. Most entries link to a section on the page.
MENU = [
    {"id": "about", "label": "Über mich", "icon": "user"},
    {"id": "experience", "label": "Erfahrung", "icon": "briefcase"},
    {"id": "education", "label": "Ausbildung", "icon": "cap"},
    {"id": "skills", "label": "Skills", "icon": "terminal"},
    {"id": "projects", "label": "Projekte", "icon": "star"},
    {"id": "audit", "label": "Prüfpfad", "icon": "check"},
    {"id": "contact", "label": "Kontakt", "icon": "mail"},
    {"id": "print", "label": "Drucken", "icon": "printer", "action": "print"},
]

DELTA_SCORE, DELTA_MAX = 988, 1000


def study_progress(today: date) -> int:
    """Share of the dual study programme that has passed, in percent."""
    start = date.fromisoformat(cv_data.PROFILE["study_start"])
    end = date.fromisoformat(cv_data.PROFILE["study_end"])
    share = (today - start).days / (end - start).days
    return round(min(max(share, 0), 1) * 100)


def build_audit_trail(data: dict) -> list[dict]:
    """Give every claim a reference number (B1, B2, ...) and list it with its sources.

    The reference is stored on the item as "ref" so the template can show it next to the claim.
    """
    trail = []

    def add(item: dict, claim: str, source_keys: list[str]):
        ref = f"B{len(trail) + 1}"
        item["ref"] = ref
        sources = [cv_data.SOURCES[key] for key in dict.fromkeys(source_keys)]
        trail.append({"ref": ref, "claim": claim, "sources": sources})

    for job in data["experience"]:
        add(job, f"{job['title']} bei {job['company']}, {job['period']}", [job["source"]])
    for entry in data["education"]:
        add(entry, f"{entry['title']}, {entry['school']}, {entry['period']}", [entry["source"]])
    for fact in data["quick_facts"]:
        add(fact, f"{fact['label']}: {fact['value']}", [fact["source"]])
    for group in data["skills"]:
        names = ", ".join(item["name"] for item in group["items"])
        add(group, f"Skills {group['group']}: {names}", [item["source"] for item in group["items"]])
    for project in data["projects"]:
        add(project, f"Projekt {project['name']}", [project["source"]])
    return trail


def build_readouts(data: dict, progress: int, trail: list[dict]) -> dict:
    """Short facts the device screen shows while the matching section is on screen."""
    return {
        "about": {"title": "Profil", "rows": [("Rolle", "Dual · RSW"), ("Praxis", "Deloitte"), ("Ort", "München")]},
        "experience": {
            "title": "Stationen",
            "timeline": [(job["year"], job["company"].split()[0]) for job in reversed(data["experience"])],
        },
        "education": {
            "title": "Studium",
            "bars": [
                ("Studium", progress, 100, f"{progress} %"),
                ("Delta", DELTA_SCORE, DELTA_MAX, f"{DELTA_SCORE}/{DELTA_MAX}"),
            ],
        },
        "skills": {
            "title": "Skills",
            "rows": [(group["group"], str(len(group["items"]))) for group in data["skills"]],
        },
        "projects": {"title": "Projekte", "rows": [(p["name"], p["stack"][0]) for p in data["projects"]]},
        "audit": {
            "title": "Prüfpfad",
            "rows": [("Aussagen", str(len(trail))), ("Quellen", str(len(cv_data.SOURCES))), ("Status", "belegt")],
        },
        "contact": {"title": "Kontakt", "rows": [(item["label"], "bereit") for item in data["contact"]]},
    }


def page_context() -> dict:
    today = date.today()
    # Work on a copy so the reference numbers are added fresh for every render.
    data = copy.deepcopy(
        {
            "profile": cv_data.PROFILE,
            "quick_facts": cv_data.QUICK_FACTS,
            "skills": cv_data.SKILLS,
            "experience": cv_data.EXPERIENCE,
            "projects": cv_data.PROJECTS,
            "education": cv_data.EDUCATION,
            "contact": cv_data.CONTACT,
        }
    )
    trail = build_audit_trail(data)
    progress = study_progress(today)
    return {
        **data,
        "menu": MENU,
        "glossary": cv_data.GLOSSARY,
        "audit_trail": trail,
        "study_progress": progress,
        "readouts": build_readouts(data, progress, trail),
        "site_url": cv_data.SITE_URL,
        "impressum": cv_data.IMPRESSUM,
        "hosting_provider": cv_data.HOSTING_PROVIDER,
        "privacy_contact": cv_data.PRIVACY_CONTACT,
        "year": today.year,
        "as_of": today.strftime("%d.%m.%Y"),
    }


@app.route("/")
def index():
    return render_template("index.html", **page_context())


@app.route("/datenschutz.html")
def privacy():
    return render_template("datenschutz.html", **page_context())


if __name__ == "__main__":
    app.run(debug=True)
