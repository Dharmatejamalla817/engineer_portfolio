import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Your real engineering profile credentials
    profile = {
        "name": "Malla Dharma Teja",
        "email": "dharmatej817@gmail.com",
        "phone": "+91 8179015198",
        "linkedin": "https://www.linkedin.com/in/dharmatejamalla",
        "github": "https://github.com/Dharmatejamalla817",
        "college": "Gayatri Vidya Parishad College of Engineering",
        "degree": "B.Tech in Electronics & Communication Engineering (2022 – 2026)",
        "cgpa": "7.13",
        "training": "Full-Stack Web Development Trainee at NxtWave Academy"
    }
    
    # Complete updated project portfolio matrix with correct Swetha Parlour repository
    projects = [
        {
            "title": "Swetha Beauty Parlor Platform",
            "category": "Commercial Full-Stack Application",
            "desc": "Designed and developed a dynamic web application to automate the appointment booking pipeline for a local business, completely replacing manual physical scheduling with a resilient digital workflow engine.",
            "tech": ["Python", "Flask", "HTML5", "CSS3", "Bootstrap", "Render"],
            "link": "https://github.com/Dharmatejamalla817/swetha-parlour-webb"
        },
        {
            "title": "Terranova Land Asset Portal",
            "category": "Full-Stack Software Architecture",
            "desc": "A high-ticket, minimalist spatial asset deployment system featuring client-side session caching to isolate guest state and automated situational UI morphing based on background time parameters.",
            "tech": ["Python", "Flask", "SQLite", "JavaScript ES6", "Git"],
            "link": "https://github.com/Dharmatejamalla817/terranova-land-asset-portal"
        },
        {
            "title": "Gourmet Hub Dispatch Console",
            "category": "Logistics & Operational Systems",
            "desc": "A high-velocity ghost-kitchen fulfillment interface equipped with an automated backend surge protection engine that dynamically handles order velocity spikes by scaling delivery safety windows.",
            "tech": ["Python", "Flask", "SQLAlchemy", "SessionStorage", "Git"],
            "link": "https://github.com/Dharmatejamalla817/gourmet-hub-dispatch-console"
        }
    ]
    
    # Certified Metrics to grab recruiter attention immediately
    metrics = [
        {"label": "TCS iON NQT Python Coding", "score": "75%"},
        {"label": "Advanced Quantitative & Reasoning", "score": "74%"},
        {"label": "Cognitive Aptitude & Analytics", "score": "68%"}
    ]

    return render_template('index.html', profile=profile, projects=projects, metrics=metrics)

if __name__ == '__main__':
    app.run(port=8000, debug=True)