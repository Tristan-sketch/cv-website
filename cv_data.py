"""All content of the CV website.

Edit this file to change what the website shows. Every claim points to a
source in SOURCES, which the site lists as an audit trail ("Prüfpfad").
"""

# Full URL of the published site, e.g. "https://tristan-sketch.github.io/cv-website".
# Needed for link previews (Open Graph image) and the print footer. None until hosted.
SITE_URL = "https://tristan-sketch.github.io/cv-website"

# Legal notice. Leave as None until you decide whether the site needs one;
# never fill in an address you do not want to publish.
IMPRESSUM = None  # e.g. {"name": "...", "address": ["Straße 1", "12345 Ort"], "email": "..."}

# Name of the hosting provider for the privacy page, e.g. "GitHub Pages (GitHub Inc.)".
HOSTING_PROVIDER = "GitHub Pages (GitHub Inc., USA)"

# Contact for the privacy page. Without an e-mail address the page points to LinkedIn.
PRIVACY_CONTACT = {"name": "Tristan Hartenstein", "email": None}

SOURCES = {
    "linkedin": {
        "label": "LinkedIn-Profil",
        "url": "https://www.linkedin.com/in/tristan-hartenstein-7b6a43306",
    },
    "code": {
        "label": "Quellcode auf GitHub",
        "url": "https://github.com/Tristan-sketch",
    },
    "site": {
        "label": "Diese Website selbst",
        "url": "https://github.com/Tristan-sketch/cv-website",
    },
}

# Terms a reader outside auditing may not know. Explained in the text and in the glossary.
GLOSSARY = {
    "RSW": "Rechnungswesen, Steuern, Wirtschaftsrecht – BWL-Studiengang der DHBW, "
    "hier mit Schwerpunkt Wirtschaftsprüfung.",
    "DHBW": "Duale Hochschule Baden-Württemberg. Das Studium wechselt zwischen Theoriephasen "
    "an der Hochschule und Praxisphasen im Unternehmen.",
    "Deltaprüfung": "Zulassungsprüfung der DHBW für Studieninteressierte mit Fachhochschulreife.",
    "Audit & Assurance": "Abschlussprüfung und prüfungsnahe Leistungen einer "
    "Wirtschaftsprüfungsgesellschaft.",
}

PROFILE = {
    "name": "Tristan Hartenstein",
    "short_name": "Tristan",
    "role": "Dualer Student Wirtschaftsprüfung",
    "screen_role": "Audit @ Deloitte",
    "location": "Großraum München",
    "tagline": "Angehender Wirtschaftsprüfer mit einem Faible für Technik.",
    "summary": "Dualer Student der Wirtschaftsprüfung an der DHBW mit Praxisphasen bei "
    "Deloitte – interessiert an Prüfung, Unternehmenssteuerrecht und Transaktionen.",
    "about": [
        "Ich studiere dual Wirtschaftsprüfung im Studiengang RSW (Rechnungswesen, Steuern, "
        "Wirtschaftsrecht) an der DHBW. Meine Praxisphasen verbringe ich bei Deloitte "
        "im Bereich Audit & Assurance, Industry.",
        "Besonders interessieren mich Wirtschaftsprüfung, Unternehmenssteuerrecht "
        "und Transaktionen.",
        "Vor dem Studium war ich im IT-Praktikum bei Titanom Technologies und habe dort "
        "meine erste eigene Web-App gebaut. Die Neugier auf Technik ist geblieben – "
        "deshalb ist auch dieser Lebenslauf eine kleine App, deren Aussagen sich "
        "im Prüfpfad nachvollziehen lassen.",
    ],
    "study_start": "2025-10-01",
    "study_end": "2028-10-01",
}

QUICK_FACTS = [
    {"label": "Standort", "value": "Großraum München", "source": "linkedin"},
    {"label": "Studium", "value": "B.Sc. Wirtschaftsprüfung (RSW), DHBW", "source": "linkedin"},
    {
        "label": "Deltaprüfung",
        "value": "988 / 1000 Punkte",
        "note": "Zulassungsprüfung der DHBW für Studieninteressierte mit Fachhochschulreife",
        "source": "linkedin",
    },
    {
        "label": "Sprachen",
        "value": "Deutsch (Muttersprache), Englisch (verhandlungssicher)",
        "source": "linkedin",
    },
]

# Every skill names where it was used, so it is shown with evidence instead of as a claim.
SKILLS = [
    {
        "group": "Fachlich",
        "items": [
            {"name": "Rechnungslegungsstandards", "evidence": "Studium RSW", "source": "linkedin"},
            {"name": "IFRS", "evidence": "Studium RSW", "source": "linkedin"},
            {"name": "Steuern", "evidence": "Studium RSW", "source": "linkedin"},
            {"name": "Wirtschaftsprüfung", "evidence": "Deloitte Audit", "source": "linkedin"},
        ],
    },
    {
        "group": "Tech",
        "items": [
            {"name": "TypeScript", "evidence": "BlogPost · Titanom 2024", "source": "code"},
            {"name": "React / Next.js", "evidence": "BlogPost · Titanom 2024", "source": "code"},
            {"name": "Tailwind CSS", "evidence": "BlogPost · Titanom 2024", "source": "code"},
            {"name": "SQL", "evidence": "BlogPost · Titanom 2024", "source": "code"},
            {"name": "Python / Flask", "evidence": "Diese Website", "source": "site"},
            {"name": "Git & GitHub", "evidence": "Beide Projekte", "source": "code"},
        ],
    },
]

EXPERIENCE = [
    {
        "title": "Junior Staff – Audit Industry",
        "company": "Deloitte",
        "period": "Okt. 2025 – heute",
        "year": "2025",
        "location": "Großraum München",
        "points": [
            "Praxisphasen des dualen Studiums Wirtschaftsprüfung (RSW)",
            "Audit & Assurance im Bereich Industry",
        ],
        "source": "linkedin",
    },
    {
        "title": "Praktikum Informationstechnologie",
        "company": "Titanom Technologies",
        "period": "März 2024 – Juli 2024",
        "year": "2024",
        "location": "Großraum München",
        "points": [
            "Eigene Blog-Plattform mit Next.js, TypeScript und Tailwind CSS entwickelt",
            "Datenbank mit Drizzle ORM und PostgreSQL angebunden, inklusive Migrationen",
            "Benutzer-Login, Kommentare und Kategorien umgesetzt",
        ],
        "source": "linkedin",
    },
    {
        "title": "Praktikum Produktion & Marketing",
        "company": "additive elements GmbH",
        "period": "Sept. 2023 – Feb. 2024",
        "year": "2023",
        "location": "Großraum München",
        "points": [],
        "source": "linkedin",
    },
]

PROJECTS = [
    {
        "name": "BlogPost",
        "description": "Blog-Plattform mit Accounts, Kategorien und Kommentaren. "
        "Entstanden im Praktikum bei Titanom, später auf eigenes Login und SQLite umgebaut.",
        "stack": ["Next.js", "TypeScript", "Tailwind", "SQLite"],
        "link": "https://github.com/Tristan-sketch/BlogPost",
        "public": False,
        "source": "code",
    },
    {
        "name": "Diese Website",
        "description": "Mein Lebenslauf als Website, gebaut mit Python und Flask. "
        "Inhalte, Pixel-Grafiken und Prüfpfad entstehen aus Python-Daten.",
        "stack": ["Python", "Flask", "Jinja", "CSS"],
        "link": "https://github.com/Tristan-sketch/cv-website",
        "public": False,
        "source": "site",
    },
]

EDUCATION = [
    {
        "title": "Bachelor of Science – Wirtschaftsprüfung (RSW)",
        "school": "Duale Hochschule Baden-Württemberg (DHBW)",
        "period": "Okt. 2025 – Okt. 2028",
        "source": "linkedin",
    },
    {
        "title": "Fachabitur – Wirtschaft und Verwaltung",
        "school": "Staatliche Fachoberschule Germering",
        "period": "Sept. 2023 – Juli 2025",
        "source": "linkedin",
    },
]

CONTACT = [
    {
        "label": "LinkedIn",
        "value": "tristan-hartenstein",
        "url": "https://www.linkedin.com/in/tristan-hartenstein-7b6a43306",
    },
    {"label": "GitHub", "value": "Tristan-sketch", "url": "https://github.com/Tristan-sketch"},
]
