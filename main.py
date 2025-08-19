from flask import Flask, render_template
import os

app = Flask(__name__)

# Portfolio data
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
        "description": "URL shortener with Redis caching for low-latency reads and Google Cloud Bigtable for scalable storage of url mappings and request metadata.",
        "image": "images/pic02.png",
        "github": "https://github.com/PranavDonepudi/SlimLink",
        "featured": False,
    },
    {
        "title": "Sentiment Analysis on Textual Data",
        "date": "April, 2022",
        "description": "Natural language processing pipeline in Python using Pandas, NLTK, and Matplotlib to classify sentiment and visualize results.",
        "image": "images/pic03.png",
        "github": "https://github.com/PranavDonepudi/Sentiment-Analysis",
        "featured": False,
    },
    {
        "title": "RAMBO Filters in Genomic Analysis",
        "date": "Rice University, 2024",
        "description": "Explores RAMBO filters to reduce false positives with strong memory efficiency; benchmarks against Bloom and Cuckoo filters for genomic workloads.",
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
        "description": "Undergraduate degree in Computer Science with strong foundation in programming and software engineering.",
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
        "description": "Built a WhatsApp-based recruitment chatbot integrated with OpenAI GPT-4, AWS SQS, and DynamoDB, automating candidate engagement, reducing initial response time by 80%, and handling up to 500 candidate interactions daily. Implemented Celery task queues with AWS SQS and Flask, optimizing resume uploads and database updates, achieving 70% faster chatbot response times and 99.9% uptime on AWS App Runner.",
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
        "description": "Built and maintained high-performance backend services using RPC frameworks (gRPC) and messaging systems (Kafka, Celery), ensuring efficient asynchronous communication and task processing. Deployed applications on cloud platforms (AWS, GCP) using Docker and Kubernetes, improving deployment speed and scalability. Enhanced API security, scalability, and performance, handling over 10,000 requests per day reliably.",
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
        "description": "Designed and implemented end-to-end data orchestration workflows using tools like Apache Airflow and Prefect, enabling seamless data integration and transformation across 10+ data sources, reducing processing time by 30%. Designed intuitive frontend interfaces using React (with TypeScript) and Angular, enhancing user satisfaction by 30%. Implemented comprehensive automated testing and set up CI/CD pipelines, increasing code coverage by 40%.",
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
