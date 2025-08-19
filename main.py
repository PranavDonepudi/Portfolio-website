from flask import Flask, render_template
import os

app = Flask(__name__)

# Portfolio data
projects = [
    {
        'title': 'MERN Stack Chat App',
        'date': 'Rice University, 2024',
        'description': 'Built with MongoDB, Express.js, React, and Node.js; real-time via Socket.io; secure auth with JWT.',
        'image': 'images/picchatpp.png',
        'github': 'https://github.com/PranavDonepudi/Chat-application',
        'featured': True
    },
    {
        'title': 'Pacman Game using Spark Java',
        'date': 'Rice University, 2023',
        'description': 'Game built with Spark Java to manage state and interactions, with a lightweight UI for gameplay.',
        'image': 'images/picpacman.webp',
        'github': 'https://github.com/RiceGradOOCourse/final-game-team-d',
        'featured': True
    },
    {
        'title': 'URL Shortener (SlimLink)',
        'date': 'Rice University, 2024',
        'description': 'URL shortener with Redis caching for low-latency reads and Google Cloud Bigtable for scalable storage of url mappings and request metadata.',
        'image': 'images/pic02.png',
        'github': 'https://github.com/PranavDonepudi/SlimLink',
        'featured': False
    },
    {
        'title': 'Sentiment Analysis on Textual Data',
        'date': 'April, 2022',
        'description': 'Natural language processing pipeline in Python using Pandas, NLTK, and Matplotlib to classify sentiment and visualize results.',
        'image': 'images/pic03.png',
        'github': 'https://github.com/PranavDonepudi/Sentiment-Analysis',
        'featured': False
    },
    {
        'title': 'RAMBO Filters in Genomic Analysis',
        'date': 'Rice University, 2024',
        'description': 'Explores RAMBO filters to reduce false positives with strong memory efficiency; benchmarks against Bloom and Cuckoo filters for genomic workloads.',
        'image': 'images/pic04.png',
        'github': 'https://github.com/PranavDonepudi/Genomic-Data-FIlter',
        'featured': False
    }
]

experience = [
    {
        'title': 'Master of Computer Science',
        'company': 'Rice University',
        'period': 'Dec 2024',
        'description': 'Graduate degree focusing on software development, data analysis, and machine learning.',
        'skills': ['Python', 'Java', 'JavaScript', 'C#', 'Data Analysis', 'Machine Learning']
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, experience=experience)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/experience')
def experience_page():
    return render_template('experience.html', experience=experience)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)