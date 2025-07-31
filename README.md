# 📝 AI Resume Screener

A Flask-based web application that helps job seekers **analyze their resumes** against a job description.  
It uses **Natural Language Processing (TF-IDF + Cosine Similarity)** to calculate a **match score** and highlight **matched & missing keywords**.

---

## 🚀 Features

- 📂 **Upload Resume** in `.docx` format
- 📋 **Paste Job Description** directly in the text area
- 📊 **Get Resume Match Score** (0–100%)
- 🔑 **Analyze Keywords**:
  - Matched keywords present in your resume
  - Missing keywords you can add to improve your resume
- 🎨 **Clean and Minimal UI**

---

## 📸 Screenshots

*(Add your screenshots here)*

Example:

**Home Page (Upload & Paste Job Description)**  
![Home Page](screenshot-home.png)

**Results Page (Match Score & Keyword Analysis)**  
![Results Page](screenshot-results.png)

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/krish10007/AI_Resume_Screener.git
cd AI_Resume_Screener
2️⃣ Create & Activate Virtual Environment
Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
python app.py
5️⃣ Open in Browser
Go to:

cpp
Copy
Edit
http://127.0.0.1:5000
📂 Project Structure
php
Copy
Edit
AI_Resume_Screener/
│
├── static/                # CSS files
│   └── style.css
│
├── templates/             # HTML templates
│   ├── index.html         # Upload resume & paste JD
│   └── result.html        # Show match score & keywords
│
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
🧠 How It Works
Extract Resume Text from the uploaded .docx file.

Vectorize Resume & Job Description using TF-IDF.

Compute Similarity using Cosine Similarity.

Analyze Keywords:

Matched keywords → present in both

Missing keywords → in job description but not in resume

Return Results as a clean web page with:

Match Score (percentage)

Keyword lists

💡 Future Improvements
📄 Support PDF resumes

🌐 Deploy on Heroku or AWS for public access

📊 Advanced scoring with word weighting and synonym matching

🏆 Author
Krish Jakhar
🎓 Computer Science Undergrad | 💻 Aspiring Software Engineer
📌 GitHub Profile