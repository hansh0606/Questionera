import requests
from flask import Flask, render_template, request
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')

RAPIDAPI_KEY = "35bc8b28a5msh9bf870297aaf73fp1388e3jsnce146f0722a7"
RAPIDAPI_HOST = "open-ai21.p.rapidapi.com"

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

def extract_technical_keywords(text):
    punctuations = ['(', ')', ';', ':', '[', ']', ',', '...', '.', '']
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    technical_keywords = []
    technical_keyword_list = [
        'programming', 'coding', 'software', 'development', 'algorithm', 'database', 
        'system design', 'data structure', 'object-oriented', 'java', 'python', 'c++', 
        'javascript', 'html', 'css', 'backend', 'frontend', 'full-stack', 'git', 
        'version control', 'agile', 'testing', 'debugging', 'framework', 'library', 
        'api', 'restful', 'http', 'server', 'client', 'routing', 'authentication', 
        'authorization', 'security', 'scalability', 'performance', 'optimization'
    ]
    additional_technical_keywords = [
        'ruby', 'php', 'swift', 'kotlin', 'typescript', 'scala', 'go', 'rust', 'perl', 
        'shell', 'bash', 'r', 'matlab', 'assembly', 'haskell', 'lua', 'dart', 'groovy', 
        'clojure', 'elixir', 'mongodb', 'mysql', 'postgresql', 'sqlite', 'oracle', 
        'sql server', 'redis', 'cassandra', 'firebase', 'docker', 'kubernetes', 'jenkins', 
        'ansible', 'terraform', 'aws', 'azure', 'google cloud', 'heroku', 'apache', 'nginx', 
        'spring', 'django', 'flask', 'express', 'react', 'angular', 'vue', 'jquery', 'bootstrap', 
        'tailwind css', 'sass', 'less', 'redux', 'mobx', 'webpack', 'babel', 'npm', 'yarn', 
        'storybook', 'jest', 'mocha', 'chai', 'enzyme', 'selenium', 'junit', 'pytest', 'cypress', 
        'gitlab', 'bitbucket', 'svn', 'mercurial', 'jira', 'trello', 'confluence', 'slack', 'discord'
    ]
    technical_keyword_list.extend(additional_technical_keywords)
    
    for word in tokens:
        word = word.lower()
        if word not in stop_words and word not in punctuations:
            if word in technical_keyword_list:
                technical_keywords.append(word)
            elif word.isdigit():
                technical_keywords.append(word)
    return technical_keywords

def generate_interview_questions(resume_text):
    url = "https://open-ai21.p.rapidapi.com/conversationgpt35"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "generate technical interview questions based on these keywords :" + resume_text
            }
        ],
        "web_access": False,
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        if file:
            resume_text = extract_text_from_pdf(file)
            keywords = extract_technical_keywords(resume_text)
            questions = generate_interview_questions(resume_text)
            return render_template('index.html', keywords=keywords, questions=questions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
