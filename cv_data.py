"""All content of the CV website.

Edit this file to change what the website shows.
"""

PROFILE = {
    "name": "Tristan Hartenstein",
    "short_name": "Tristan",
    "role": "Dualer Student Wirtschaftsprüfung",
    "screen_role": "Audit @ Deloitte",
    "location": "Großraum München",
    "tagline": "Angehender Wirtschaftsprüfer mit einem Faible für Technik.",
    "about": [
        "Ich studiere dual Wirtschaftsprüfung (RSW) an der DHBW. Meine Praxisphasen "
        "verbringe ich bei Deloitte im Bereich Audit & Assurance, Industry.",
        "Besonders interessieren mich Wirtschaftsprüfung, Unternehmenssteuerrecht "
        "und Transaktionen.",
        "Vor dem Studium war ich im IT-Praktikum bei Titanom Technologies und habe dort "
        "meine erste eigene Web-App gebaut. Die Neugier auf Technik ist geblieben – "
        "deshalb ist auch dieser Lebenslauf eine kleine App.",
    ],
}

# Short facts shown next to the "about" text.
QUICK_FACTS = [
    {"label": "Standort", "value": "Großraum München"},
    {"label": "Studium", "value": "B.Sc. Wirtschaftsprüfung (RSW), DHBW"},
    {"label": "Deltaprüfung", "value": "988 / 1000 Punkte"},
    {"label": "Sprachen", "value": "Deutsch (Muttersprache), Englisch (verhandlungssicher)"},
]

SKILLS = [
    {
        "group": "Fachlich",
        "items": [
            "Rechnungslegungsstandards",
            "IFRS",
            "Steuern",
            "Wirtschaftsprüfung",
        ],
    },
    {
        "group": "Tech",
        "items": [
            "TypeScript",
            "React / Next.js",
            "Tailwind CSS",
            "SQL",
            "Python",
            "Git & GitHub",
        ],
    },
]

EXPERIENCE = [
    {
        "title": "Junior Staff – Audit Industry",
        "company": "Deloitte",
        "period": "Okt. 2025 – heute",
        "location": "Großraum München",
        "points": [
            "Praxisphasen des dualen Studiums Wirtschaftsprüfung (RSW)",
            "Audit & Assurance im Bereich Industry",
        ],
    },
    {
        "title": "Praktikum Informationstechnologie",
        "company": "Titanom Technologies",
        "period": "März 2024 – Juli 2024",
        "location": "Großraum München",
        "points": [
            "Eigene Blog-Plattform mit Next.js, TypeScript und Tailwind CSS entwickelt",
            "Datenbank mit Drizzle ORM und PostgreSQL angebunden, inklusive Migrationen",
            "Benutzer-Login, Kommentare und Kategorien umgesetzt",
        ],
    },
    {
        "title": "Praktikum Produktion & Marketing",
        "company": "additive elements GmbH",
        "period": "Sept. 2023 – Feb. 2024",
        "location": "Großraum München",
        "points": [],
    },
]

PROJECTS = [
    {
        "name": "BlogPost",
        "description": "Blog-Plattform mit Accounts, Kategorien und Kommentaren. "
        "Entstanden im Praktikum bei Titanom, später auf eigenes Login und SQLite umgebaut.",
        "stack": ["Next.js", "TypeScript", "Tailwind", "SQLite"],
        "link": "https://github.com/Tristan-sketch/BlogPost",
    },
    {
        "name": "Diese Website",
        "description": "Mein Lebenslauf als Website – gebaut mit Python und Flask, "
        "im Stil eines kleinen Hacker-Gadgets.",
        "stack": ["Python", "Flask", "Jinja", "CSS"],
        "link": "https://github.com/Tristan-sketch/cv-website",
    },
]

EDUCATION = [
    {
        "title": "Bachelor of Science – Wirtschaftsprüfung (RSW)",
        "school": "Duale Hochschule Baden-Württemberg (DHBW)",
        "period": "Okt. 2025 – Okt. 2028",
    },
    {
        "title": "Fachabitur – Wirtschaft und Verwaltung",
        "school": "Staatliche Fachoberschule Germering",
        "period": "Sept. 2023 – Juli 2025",
    },
]

CONTACT = [
    {"label": "E-Mail", "value": "...", "url": "mailto:..."},
    {
        "label": "LinkedIn",
        "value": "tristan-hartenstein",
        "url": "https://www.linkedin.com/in/tristan-hartenstein-7b6a43306",
    },
    {"label": "GitHub", "value": "Tristan-sketch", "url": "https://github.com/Tristan-sketch"},
]
