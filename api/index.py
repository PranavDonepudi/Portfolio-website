# api/index.py
from flask import Flask, render_template
import os

# NOTE: templates/ and static/ are one level above /api
app = Flask(__name__, static_folder="../static", template_folder="../templates")

# ---- Your data (same as in your main.py) ----
projects = [
    {
        "title": "MERN Stack Chat App",
        "date": "Rice University, 2024",
        "description": "Built with MongoDB, Express.js, React, and Node.js; real-time via Socket.io; secure auth with JWT.",
        "image": "images/picchatpp.png",
        "github": "https://github.com/PranavDonepudi/Chat-application",
        "featured": True,
    },
    {
        "title": "Pacman Game using Spark Java",
        "date": "Rice University, 2023",
        "description": "Game built with Spark Java to manage state and interactions, with a lightweight UI for gameplay.",
        "image": "images/picpacman.webp",
        "github": "https://github.com/RiceGradOOCourse/final-game-team-d",
        "featured": True,
    },
    {
        "title": "URL Shortener (SlimLink)",
        "date": "Rice University, 2024",
        "description": "URL shortener with Redis caching for low-latency reads and Google Cloud Bigtable for scalable storage.",
        "image": "images/pic02.png",
        "github": "https://github.com/PranavDonepudi/SlimLink",
        "featured": False,
    },
    {
        "title": "Sentiment Analysis on Textual Data",
        "date": "April, 2022",
        "description": "NLP pipeline in Python using Pandas, NLTK, and Matplotlib to classify sentiment and visualize results.",
        "image": "images/pic03.png",
        "github": "https://github.com/PranavDonepudi/Sentiment-Analysis",
        "featured": False,
    },
    {
        "title": "RAMBO Filters in Genomic Analysis",
        "date": "Rice University, 2024",
        "description": "Explores RAMBO filters to reduce false positives with strong memory efficiency; compared to Bloom/Cuckoo filters.",
        "image": "images/pic04.png",
        "github": "https://github.com/PranavDonepudi/Genomic-Data-FIlter",
        "featured": False,
    },
]

experience = [
    {
        "title": "Master of Computer Science",
        "company": "Rice University",
        "period": "Aug 2023 - Dec 2024",
        "description": "Graduate degree focusing on software development, data analysis, and machine learning.",
        "skills": [
            "Python",
            "Java",
            "JavaScript",
            "C#",
            "Data Analysis",
            "Machine Learning",
        ],
    },
    {
        "title": "Bachelor of Technology in Computer Science",
        "company": "University",
        "period": "Aug 2017 - Jun 2021",
        "description": "Undergraduate degree in CS with strong foundations.",
        "skills": [
            "Programming Fundamentals",
            "Data Structures",
            "Algorithms",
            "Software Engineering",
        ],
    },
    {
        "title": "Backend Developer Intern",
        "company": "Technogen Inc. - Chantilly, VA",
        "period": "May 2025 - Present",
        "description": "WhatsApp recruitment chatbot with GPT-4, SQS, DynamoDB, Celery; deployed on AWS.",
        "skills": [
            "Python",
            "Flask",
            "OpenAI GPT-4",
            "AWS SQS",
            "DynamoDB",
            "Celery",
            "AWS App Runner",
            "AWS Fargate",
            "Lambda",
            "RESTful API",
        ],
    },
    {
        "title": "Software Engineer Intern",
        "company": "SBS Corps - Houston, TX",
        "period": "May 2024 - Jul 2024",
        "description": "Backend services with gRPC/Kafka/Celery, Docker/Kubernetes, and cloud deployments.",
        "skills": [
            "gRPC",
            "Kafka",
            "Celery",
            "AWS",
            "GCP",
            "Docker",
            "Kubernetes",
            "API Development",
            "Backend Services",
        ],
    },
    {
        "title": "Associate Software Engineer",
        "company": "DXC Technology - Bangalore, KA",
        "period": "Sept 2021 - Dec 2022",
        "description": "Data orchestration with Airflow/Prefect; React/Angular UIs; CI/CD & testing.",
        "skills": [
            "Apache Airflow",
            "Prefect",
            "React",
            "TypeScript",
            "Angular",
            "CI/CD",
            "Automated Testing",
            "Data Integration",
            "Agile/Scrum",
            "Jira",
        ],
    },
]


@app.route("/")
def home():
    return render_template("index.html", projects=projects, experience=experience)


@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)


@app.route("/experience")
def experience_page():
    return render_template("experience.html", experience=experience)


# IMPORTANT: No app.run() here. Vercel imports `app`.
