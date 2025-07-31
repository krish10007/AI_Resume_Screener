from flask import Flask, render_template, request
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    doc = Document(resume_file)
    resume_text = '\n'.join([para.text for para in doc.paragraphs])

    job_description = request.form['job_desc']

    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    match_score = round(similarity * 100, 2)

    # After calculating match_score...
    job_words = set(re.findall(r'\b\w+\b', job_description.lower()))
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))

    # Remove stopwords and short words (1-2 letters)
    filtered_job_words = {word for word in job_words if word not in ENGLISH_STOP_WORDS and len(word) > 2}
    filtered_resume_words = {word for word in resume_words if word not in ENGLISH_STOP_WORDS and len(word) > 2}

    matched_keywords = list(filtered_job_words & filtered_resume_words)
    missing_keywords = list(filtered_job_words - filtered_resume_words)

    return render_template(
        'result.html',
        score=match_score,
        keywords=matched_keywords,
        missing=missing_keywords
    )

if __name__ == '__main__':
    app.run(debug=True)
