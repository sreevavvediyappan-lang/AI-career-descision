
import re
from flask import Flask, render_template, request

app = Flask(__name__)


# =========================================================
# CAREER LIST
# =========================================================

CAREERS = [
    "Software Developer",
    "AI/ML Engineer",
    "Data Scientist",
    "Data Analyst",
    "Web Developer",
    "Cybersecurity Analyst",
    "Cloud Engineer",
    "UI/UX Designer",
]


# =========================================================
# INTEREST KEYWORDS
# =========================================================

INTEREST_KEYWORDS = {

    "Software Developer": [
        "software",
        "developer",
        "programming",
        "coding",
        "backend"
    ],

    "AI/ML Engineer": [
        "ai",
        "artificial intelligence",
        "machine learning",
        "ml",
        "deep learning"
    ],

    "Data Scientist": [
        "data scientist",
        "data science",
        "statistics",
        "data"
    ],

    "Data Analyst": [
        "data analyst",
        "analytics",
        "analyst",
        "data"
    ],

    "Web Developer": [
        "web",
        "frontend",
        "website",
        "full stack"
    ],

    "Cybersecurity Analyst": [
        "security",
        "cybersecurity",
        "cyber",
        "hacking",
        "network"
    ],

    "Cloud Engineer": [
        "cloud",
        "devops",
        "aws",
        "azure"
    ],

    "UI/UX Designer": [
        "design",
        "designer",
        "ui",
        "ux",
        "figma"
    ],
}


# =========================================================
# SKILL KEYWORDS
# =========================================================

SKILL_KEYWORDS = {

    "Software Developer": [
        "java",
        "c",
        "c++",
        "oop",
        "git"
    ],

    "AI/ML Engineer": [
        "python",
        "machine learning",
        "tensorflow",
        "deep learning",
        "ml"
    ],

    "Data Scientist": [
        "python",
        "statistics",
        "machine learning",
        "pandas"
    ],

    "Data Analyst": [
        "sql",
        "excel",
        "power bi",
        "tableau"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "flask"
    ],

    "Cybersecurity Analyst": [
        "networking",
        "linux",
        "security",
        "kali"
    ],

    "Cloud Engineer": [
        "aws",
        "azure",
        "docker",
        "cloud computing",
        "linux"
    ],

    "UI/UX Designer": [
        "figma",
        "photoshop",
        "canva",
        "communication"
    ],
}


# =========================================================
# FIELD → CAREER
# =========================================================

FIELD_CAREERS = {

    "IT": [
        "Software Developer",
        "Web Developer"
    ],

    "Artificial Intelligence": [
        "AI/ML Engineer"
    ],

    "Data Science": [
        "Data Scientist",
        "Data Analyst"
    ],

    "Cybersecurity": [
        "Cybersecurity Analyst"
    ],

    "Cloud Computing": [
        "Cloud Engineer"
    ],

    "Web Development": [
        "Web Developer"
    ],
}


# =========================================================
# MINIMUM MARKS
# =========================================================

CAREER_MIN_MARKS = {

    "Software Developer": 60,
    "AI/ML Engineer": 75,
    "Data Scientist": 75,
    "Data Analyst": 60,
    "Web Developer": 50,
    "Cybersecurity Analyst": 65,
    "Cloud Engineer": 60,
    "UI/UX Designer": 50,
}


# =========================================================
# CAREER FOCUS
# =========================================================

CAREER_FOCUS = {

    "Software Developer": [
        "Java / Python",
        "Object-Oriented Programming",
        "Data Structures and Algorithms",
        "SQL and Database Concepts",
        "Problem Solving and Coding",
        "Git and GitHub"
    ],

    "AI/ML Engineer": [
        "Python",
        "Machine Learning",
        "Statistics",
        "Data Preprocessing",
        "Deep Learning",
        "SQL"
    ],

    "Data Scientist": [
        "Python",
        "Statistics",
        "Machine Learning",
        "Pandas and NumPy",
        "Data Visualization",
        "SQL"
    ],

    "Data Analyst": [
        "SQL",
        "Excel",
        "Power BI / Tableau",
        "Data Cleaning",
        "Data Visualization",
        "Basic Statistics"
    ],

    "Web Developer": [
        "HTML and CSS",
        "JavaScript",
        "React / Frontend",
        "Flask / Backend",
        "SQL",
        "Git and GitHub"
    ],

    "Cybersecurity Analyst": [
        "Networking",
        "Linux",
        "Cybersecurity Fundamentals",
        "Security Tools",
        "Ethical Hacking Basics",
        "Operating Systems"
    ],

    "Cloud Engineer": [
        "AWS / Azure",
        "Linux",
        "Networking",
        "Docker",
        "Cloud Computing",
        "DevOps Fundamentals"
    ],

    "UI/UX Designer": [
        "UI Design",
        "UX Principles",
        "Figma",
        "Wireframing",
        "Prototyping",
        "Communication"
    ],
}


# =========================================================
# COMPANY INTERVIEW ROUNDS
# =========================================================

COMPANY_ROUNDS = {

    "TCS": [
        "Round 1 – Aptitude / Cognitive Assessment",
        "Round 2 – Technical Assessment",
        "Round 3 – Technical Interview",
        "Round 4 – Managerial / HR Interview",
        "Round 5 – Final HR Discussion"
    ],

    "Wipro": [
        "Round 1 – Online Assessment",
        "Round 2 – Coding / Technical Assessment",
        "Round 3 – Technical Interview",
        "Round 4 – HR Interview"
    ],

    "HCL": [
        "Round 1 – Online Aptitude Assessment",
        "Round 2 – Technical / Coding Assessment",
        "Round 3 – Technical Interview",
        "Round 4 – HR Interview"
    ],

    "Zoho": [
        "Round 1 – Written / Aptitude Round",
        "Round 2 – Programming / Technical Round",
        "Round 3 – Advanced Technical Rounds",
        "Round 4 – Technical Interview",
        "Round 5 – HR / Final Discussion"
    ],

    "Infosys": [
        "Round 1 – Online Assessment",
        "Round 2 – Technical Interview",
        "Round 3 – HR Interview"
    ],

    "Accenture": [
        "Round 1 – Cognitive / Technical Assessment",
        "Round 2 – Coding Assessment",
        "Round 3 – Communication / Interview",
        "Round 4 – HR / Final Discussion"
    ],
}


# =========================================================
# COMPANY PHASE-WISE FOCUS
# =========================================================

COMPANY_PHASE_FOCUS = {

    "TCS": [
        {
            "phase": "Aptitude Phase",
            "focus": "Quantitative aptitude, logical reasoning and verbal ability."
        },
        {
            "phase": "Technical Assessment",
            "focus": "Java / Python, SQL, OOP, DBMS and basic coding problems."
        },
        {
            "phase": "Technical Interview",
            "focus": "Programming concepts, OOP, SQL, projects and problem solving."
        },
        {
            "phase": "Managerial / HR Phase",
            "focus": "Communication, teamwork, strengths, weaknesses and career goals."
        },
        {
            "phase": "Final HR Phase",
            "focus": "Confidence, company knowledge and understanding of the job role."
        }
    ],

    "Wipro": [
        {
            "phase": "Online Assessment",
            "focus": "Quantitative aptitude, logical reasoning, verbal ability and basic technical questions."
        },
        {
            "phase": "Coding / Technical Assessment",
            "focus": "Programming fundamentals, coding problems, OOP, SQL and DBMS."
        },
        {
            "phase": "Technical Interview",
            "focus": "Programming, projects, database concepts and problem solving."
        },
        {
            "phase": "HR Interview",
            "focus": "Communication, teamwork, strengths, career goals and company awareness."
        }
    ],

    "HCL": [
        {
            "phase": "Aptitude Assessment",
            "focus": "Quantitative aptitude, logical reasoning and verbal ability."
        },
        {
            "phase": "Technical / Coding Assessment",
            "focus": "Programming, OOP, SQL, DBMS and coding practice."
        },
        {
            "phase": "Technical Interview",
            "focus": "Programming concepts, projects, SQL and technical problem solving."
        },
        {
            "phase": "HR Interview",
            "focus": "Communication, confidence, teamwork and career goals."
        }
    ],

    "Zoho": [
        {
            "phase": "Written / Aptitude Round",
            "focus": "Logical reasoning, aptitude and problem-solving questions."
        },
        {
            "phase": "Programming / Technical Round",
            "focus": "Programming fundamentals, Java / Python, OOP and coding."
        },
        {
            "phase": "Advanced Technical Rounds",
            "focus": "Data Structures, Algorithms, problem solving and advanced coding."
        },
        {
            "phase": "Technical Interview",
            "focus": "Projects, programming concepts, databases and technical depth."
        },
        {
            "phase": "HR / Final Discussion",
            "focus": "Communication, confidence, career goals and company knowledge."
        }
    ],

    "Infosys": [
        {
            "phase": "Online Assessment",
            "focus": "Quantitative aptitude, logical reasoning, verbal ability and technical basics."
        },
        {
            "phase": "Technical Interview",
            "focus": "Programming, OOP, SQL, DBMS, projects and problem solving."
        },
        {
            "phase": "HR Interview",
            "focus": "Communication, teamwork, strengths, weaknesses and career goals."
        }
    ],

    "Accenture": [
        {
            "phase": "Cognitive / Technical Assessment",
            "focus": "Logical reasoning, aptitude, verbal ability and technical fundamentals."
        },
        {
            "phase": "Coding Assessment",
            "focus": "Programming logic, coding and problem solving."
        },
        {
            "phase": "Communication / Interview",
            "focus": "Communication, technical knowledge and project explanation."
        },
        {
            "phase": "HR / Final Discussion",
            "focus": "Confidence, teamwork, career goals and company awareness."
        }
    ],
}


# =========================================================
# COMPANY SKILLS
# =========================================================

COMPANY_SKILLS = {

    "TCS": [
        "Java / Python",
        "SQL",
        "Object-Oriented Programming",
        "DBMS",
        "Data Structures and Algorithms",
        "Problem Solving",
        "Communication"
    ],

    "Wipro": [
        "Java / Python",
        "SQL",
        "OOP",
        "DBMS",
        "Coding",
        "Problem Solving",
        "Communication"
    ],

    "HCL": [
        "Java / Python",
        "SQL",
        "OOP",
        "DBMS",
        "Coding",
        "Data Structures",
        "Communication"
    ],

    "Zoho": [
        "Java / Python",
        "Data Structures",
        "Algorithms",
        "Problem Solving",
        "OOP",
        "SQL",
        "Advanced Coding"
    ],

    "Infosys": [
        "Java / Python",
        "SQL",
        "OOP",
        "DBMS",
        "Problem Solving",
        "Communication"
    ],

    "Accenture": [
        "Programming",
        "SQL",
        "OOP",
        "Coding",
        "Problem Solving",
        "Communication",
        "Technical Fundamentals"
    ],
}


# =========================================================
# SKILLS TO DEVELOP
# =========================================================

SKILLS_TO_DEVELOP = {

    "Software Developer": [
        "Data Structures and Algorithms",
        "Advanced Java / Python",
        "Problem Solving",
        "Coding Speed",
        "Technical Interview Skills",
        "Aptitude and Logical Reasoning",
        "Communication"
    ],

    "AI/ML Engineer": [
        "Machine Learning",
        "Statistics",
        "Python",
        "Data Structures",
        "Deep Learning",
        "SQL",
        "Problem Solving"
    ],

    "Data Scientist": [
        "Python",
        "Statistics",
        "Machine Learning",
        "Pandas and NumPy",
        "SQL",
        "Data Visualization",
        "Problem Solving"
    ],

    "Data Analyst": [
        "Advanced SQL",
        "Excel",
        "Power BI / Tableau",
        "Statistics",
        "Data Visualization",
        "Data Cleaning",
        "Communication"
    ],

    "Web Developer": [
        "Advanced JavaScript",
        "React",
        "Backend Development",
        "REST APIs",
        "SQL",
        "Git",
        "Problem Solving"
    ],

    "Cybersecurity Analyst": [
        "Networking",
        "Linux",
        "Cybersecurity Tools",
        "Ethical Hacking",
        "Operating Systems",
        "Security Concepts",
        "Problem Solving"
    ],

    "Cloud Engineer": [
        "AWS / Azure",
        "Linux",
        "Docker",
        "Networking",
        "DevOps",
        "Cloud Security",
        "Problem Solving"
    ],

    "UI/UX Designer": [
        "Figma",
        "UX Research",
        "Wireframing",
        "Prototyping",
        "Design Principles",
        "Portfolio Development",
        "Communication"
    ],
}


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def has_word(text, word):
    return (
        re.search(
            r"(?<![a-z0-9+])"
            + re.escape(word)
            + r"(?![a-z0-9+])",
            text
        ) is not None
    )


def to_percentage(value):
    """
    Accept 7.9 as CGPA or 79 as percentage.
    """

    try:
        number = float(value)
    except (TypeError, ValueError):
        return 0

    return number * 10 if number <= 10 else number


# =========================================================
# CAREER RECOMMENDATION
# =========================================================

def recommend_career(marks, field, interests_text, skills_text):

    interests_text = interests_text.lower()
    skills_text = skills_text.lower()

    scores = {
        career: 0
        for career in CAREERS
    }

    # Preferred field
    for career in FIELD_CAREERS.get(field, []):
        scores[career] += 3

    # Interests
    for career in CAREERS:

        if any(
            has_word(interests_text, keyword)
            for keyword in INTEREST_KEYWORDS[career]
        ):
            scores[career] += 5

        # Skills
        scores[career] += 2 * sum(
            has_word(skills_text, keyword)
            for keyword in SKILL_KEYWORDS[career]
        )

        # Academic performance
        if marks >= CAREER_MIN_MARKS[career]:
            scores[career] += 2
        else:
            scores[career] -= 1

    best = max(
        scores,
        key=scores.get
    )

    return best, scores[best]


# =========================================================
# SCORE OUT OF 20
# =========================================================

def get_score_out_of_20(raw_score):

    score = max(
        0,
        min(raw_score, 20)
    )

    return score


# =========================================================
# MAIN PAGE
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =========================================================
# STUDENT FORM
# =========================================================

@app.route(
    "/student",
    methods=["GET", "POST"]
)
def student():

    if request.method == "GET":

        return render_template(
            "index.html"
        )

    print(
        "DEBUG - Form received:",
        dict(request.form)
    )

    # -----------------------------
    # Get form values
    # -----------------------------

    name = request.form.get(
        "name",
        ""
    ).strip()

    email = request.form.get(
        "email",
        ""
    ).strip()

    marks = to_percentage(
        request.form.get(
            "academic_score"
        )
    )

    field = request.form.get(
        "field",
        ""
    ).strip()

    skills = request.form.get(
        "skills",
        ""
    ).strip()

    interests = request.form.get(
        "interests",
        ""
    ).strip()

    dream_company = request.form.get(
        "dream_company",
        ""
    ).strip()


    # -----------------------------
    # Career recommendation
    # -----------------------------

    career, raw_score = recommend_career(
        marks,
        field,
        interests,
        skills
    )

    score = get_score_out_of_20(
        raw_score
    )


    # -----------------------------
    # Career focus
    # -----------------------------

    focus_areas = CAREER_FOCUS.get(
        career,
        []
    )


    # -----------------------------
    # Company rounds
    # -----------------------------

    company_rounds = COMPANY_ROUNDS.get(
        dream_company,
        [
            "Round 1 – Aptitude / Online Assessment",
            "Round 2 – Technical / Coding Assessment",
            "Round 3 – Technical Interview",
            "Round 4 – HR Interview"
        ]
    )


    # -----------------------------
    # Phase-wise company focus
    # -----------------------------

    phase_focus = COMPANY_PHASE_FOCUS.get(
        dream_company,
        [
            {
                "phase": "Aptitude Phase",
                "focus": "Quantitative aptitude, logical reasoning and verbal ability."
            },
            {
                "phase": "Technical Phase",
                "focus": "Programming, SQL, OOP, DBMS and coding."
            },
            {
                "phase": "Interview Phase",
                "focus": "Projects, technical concepts and problem solving."
            },
            {
                "phase": "HR Phase",
                "focus": "Communication, confidence and career goals."
            }
        ]
    )


    # -----------------------------
    # Company skills
    # -----------------------------

    company_skills = COMPANY_SKILLS.get(
        dream_company,
        [
            "Programming",
            "SQL",
            "OOP",
            "DBMS",
            "Problem Solving",
            "Communication"
        ]
    )


    # -----------------------------
    # Skills to develop
    # -----------------------------

    skills_to_develop = SKILLS_TO_DEVELOP.get(
        career,
        [
            "Problem Solving",
            "Communication",
            "Technical Interview Skills"
        ]
    )


    print(
        "DEBUG - Career:",
        career,
        "| Score:",
        score,
        "/ 20",
        "| Company:",
        dream_company
    )


    # -----------------------------
    # Send everything to result page
    # -----------------------------

    return render_template(
        "result.html",

        name=name,
        email=email,

        career=career,
        score=score,

        interest=interests,
        skill=skills,

        dream_company=dream_company,

        focus_areas=focus_areas,

        company_rounds=company_rounds,

        phase_focus=phase_focus,

        company_skills=company_skills,

        skills_to_develop=skills_to_develop
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(
        debug=True
    )
