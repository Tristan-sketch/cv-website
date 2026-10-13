"""All content of the CV website.

Edit this file to change what the website shows. Values in [square brackets]
are placeholders that still need your real information.
"""

PROFILE = {
    "name": "Tristan Hartenstein",
    "short_name": "Tristan",
    "role": "Web Developer",
    "location": "[Stadt, Land]",
    "tagline": "Ich baue Web-Apps von der Datenbank bis zum Pixel.",
    "about": [
        "Hi! Ich bin Tristan. Programmieren habe ich während meines Praktikums bei Titanom "
        "richtig angefangen – mit einer kompletten Blog-Plattform inklusive Datenbank und Login.",
        "[Ein, zwei Sätze über dich: Was dich antreibt, was du lernen willst, wonach du suchst.]",
    ],
}

# Shown as "apps" in a grid. level: 1 to 5.
SKILLS = [
    {"name": "TypeScript", "level": 3},
    {"name": "React / Next.js", "level": 3},
    {"name": "Tailwind CSS", "level": 3},
    {"name": "SQL & Datenbanken", "level": 2},
    {"name": "Python", "level": 2},
    {"name": "Git & GitHub", "level": 2},
]

EXPERIENCE = [
    {
        "title": "Praktikum Softwareentwicklung",
        "company": "Titanom",
        "period": "[Monat Jahr] – [Monat Jahr]",
        "points": [
            "Eigene Blog-Plattform mit Next.js, TypeScript und Tailwind CSS entwickelt",
            "Datenbank mit Drizzle ORM und PostgreSQL angebunden, inklusive Migrationen",
            "Benutzer-Login, Kommentare und Kategorien umgesetzt",
        ],
    },
]

PROJECTS = [
    {
        "name": "BlogPost",
        "description": "Blog-Plattform mit Accounts, Kategorien und Kommentaren. "
        "Entstanden im Praktikum, später auf eigenes Login und SQLite umgebaut.",
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
        "title": "[Abschluss, z. B. Mittlere Reife / Abitur]",
        "school": "[Name der Schule]",
        "period": "[Jahr] – [Jahr]",
    },
]

# Small facts that give the page some personality.
FUN_FACTS = [
    "Erste Website gebaut: [Jahr]",
    "[Hobby, z. B. Gaming, Sport, Musik]",
    "[Etwas Überraschendes über dich]",
]

CONTACT = [
    {"label": "GitHub", "value": "Tristan-sketch", "url": "https://github.com/Tristan-sketch"},
    {"label": "Instagram", "value": "@tr_istan2034", "url": "https://www.instagram.com/tr_istan2034/"},
    {"label": "E-Mail", "value": "[deine@email.de]", "url": "mailto:[deine@email.de]"},
]
