from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# rest of your code...
@app.route("/")
def home():
    skills = [
        {
            "name": "Django",
            "level": 90,
            "image": "django.png",
            "color": "#2ba977",
            "score": 9,
        },
        {
            "name": "React.JS",
            "level": 90,
            "image": "reactjs.png",
            "color": "#61dafb",
            "score": 9,
        },
        {
            "name": "Next.JS",
            "level": 60,
            "image": "nextjs.svg",
            "color": "#f0f0f0",
            "score": 6,
        },
        {
            "name": "Android Studio",
            "level": 60,
            "image": "android-studio.png",
            "color": "#eeeeee",
            "score": 6,
        },
        {
            "name": "Firebase",
            "level": 70,
            "image": "firebase.png",
            "color": "#fcca3f",
            "score": 7,
        },
        {
            "name": "PostgreSQL",
            "level": 80,
            "image": "postgresql.png",
            "color": "#336791",
            "score": 8,
        },
        {
            "name": "SQLite",
            "level": 70,
            "image": "sqlite.png",
            "color": "#6cbde9",
            "score": 7,
        },
        {
            "name": "Davinci Resolve",
            "level": 80,
            "image": "davinci-resolve.png",
            "color": "#383838",
            "score": 8,
        },
        {
            "name": "Figma",
            "level": 50,
            "image": "figma.png",
            "color": "#a259ff",
            "score": 5,
        },
        {
            "name": "Canva",
            "level": 80,
            "image": "canva.png",
            "color": "#3675d9",
            "score": 8,
        },
    ]

    languages = [
        {
            "name": "HTML/CSS",
            "level": 80,
            "image": "htmlcss.png",
            "color": "#f5622d",
            "score": 8,
        },
        {
            "name": "Python",
            "level": 80,
            "image": "python.png",
            "color": "#ffe161",
            "score": 8,
        },
        {
            "name": "Javascript",
            "level": 80,
            "image": "javascript.svg",
            "color": "#ffde25",
            "score": 8,
        },
        {
            "name": "Typescript",
            "level": 60,
            "image": "typescript.png",
            "color": "#007acd",
            "score": 6,
        },
        {
            "name": "C",
            "level": 60,
            "image": "clang.png",
            "color": "#004482",
            "score": 6,
        },
        {
            "name": "C++",
            "level": 70,
            "image": "cpp.png",
            "color": "#00599c",
            "score": 7,
        },
        
    ]
    
    education = [
        {
            "name": "B.Tech",
            "course": "CSE",
            "year": "2023-2027",
            "institute": "SRM Institute of Science and Technology",
            "image": "srmrmp.webp",
            "location": "Ramapuram, Chennai",
            "score": "GPA: 9.72",
        },
        {
            "name": "Higher Secondary",
            "course": "CS Stream",
            "year": "2021-2023",
            "institute": "SBOA Mat. & Hr. Sec. School",
            "image": "sboa.webp",
            "location": "Anna Nagar, Chennai",
            "score": "HSC +2: 89.17% <br>HSC +1: 84%",
        },
    ]

    themes = ["Full Stack Development", "Video Editing", "Graphic Design"]

    portfolio = [
        {
            "name": "Diddle (Skill Exchange)",
            "stream": themes[0],
            "src": "https://github.com/kalpithasv/Diddle",
            "tech": "Next.js, Django REST API, PostgreSQL",
            "image": "diddle.png",
            "desc": "Created a platform integrating skill exchange with freelancing projects, allowing users to learn, teach, and earn.",
        },
        {
            "name": "Simplicook (Recipe Book)",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/Simplicook",
            "tech": "ReactJS, Tailwind CSS, Django REST API",
            "image": "simplicook.png",
            "desc": "A comprehensive recipe book application with enhanced features and basic CRUD operations.",
        },
        {
            "name": "Vendor Management System",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/Vendor-Management-System",
            "tech": "Django REST (Python)",
            "desc": "Provides API for tracking vendor performance metrics. ",
        },
        {
            "name": "Cryck",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/Cryck",
            "tech": "React JS, Solidity",
            "image": "Cryck.jpeg",
            "desc": "Revolutionizing cricket fandom with spatial predictions and immersive engagement with blockchain touch!",
        },
        {
            "name": "Thought Capsule",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/ThoughtCapsule",
            "tech": "Django (Python)",
            "image": "ThoughtCapsule.jpg",
            "desc": "Thought Capsule is a minimalist web platform, enhanced with AI capabilities, designed for capturing, storing, and interpreting personal thoughts, ideas, and moments. ",
        },
        {
            "name": "Synectt",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/SynecttWeb",
            "tech": "Django (Python)",
            "desc": "An event management app for Universities, Colleges and Schools. This project is used to integrate the Participant, Organiser, Sponsor, Control authorities in a single platform. Its right now just a prototype.",
        },
        {
            "name": "Djangy Bay",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/DjangoBay",
            "tech": "Django (Python)",
            "image": "DjangoBay.jpg",
            "desc": "eBay-like e-commerce auction site.",
        },
        {
            "name": "Wiki Online Encyclopedia",
            "stream": themes[0],
            "src": "https://github.com/JeyasuryaUR/WikiOnlineEncyclopedia",
            "image": "wiki.png",
            "tech": "Django (Python)",
            "desc": "A Minimal Wikipedia Clone.",
        },
    ]

    certifications = [
        {
            "name": "Introduction to AI with Python",
            "issuer": "CS50, EdX",
            "date": "Sep 2024",
            "cred": ""
        },
        {
            "name": "Scrape the Web with Python",
            "issuer": "Le Wagon",
            "date": "Jul 2024",
            "cred": ""
        },
        {
            "name": "Prompt Design in Vertex AI",
            "issuer": "Google Cloud Skills Boost",
            "date": "Jul 2024",
            "cred": ""
        },
        {
            "name": "The Basics of Google Cloud Compute",
            "issuer": "Google Cloud Skills Boost",
            "date": "Jul 2024",
            "cred": ""
        },
        {
            "name": "Data Science with Python ",
            "issuer": "Simplilearn",
            "date": "Apr 2024",
            "cred": ""
        },
        {
            "name": "Web Programming with Python & Javascript",
            "issuer": "CS50, EdX",
            "date": "Jan 2024",
            "cred": ""
        },
        {
            "name": "Blockchain Guide for Beginners",
            "issuer": "Codies Alert",
            "date": "Jan 2024",
            "cred": ""
        },
        {
            "name": "Python Essentials 1 (PCAP)",
            "issuer": "Cisco, Netacad",
            "date": "Nov 2023",
            "cred": ""
        },
        {
            "name": "Python (English)",
            "issuer": "GUVI",
            "date": "Jul 2023",
            "cred": ""
        },
        {
            "name": "Python, SQL, Java",
            "issuer": "HackerRank",
            "date": "Basic Skill Tests",
            "cred": ""
        },
    ]
    
    return render_template(
        "index.html", skills=skills, education=education, portfolio=portfolio, certifications=certifications, languages=languages
    )

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Here you can handle the form data, e.g., send an email or store in a database.
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
