from flask import Flask, render_template, request, redirect, url_for
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import pickle
import numpy as np
from app2 import *


app = Flask(__name__)

# Text preprocessing functions
def preprocess_text(text):
    # Tokenization
    words = word_tokenize(text.lower())  # Convert to lowercase and tokenize
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(words)


# Load the vectorizer
with open('model/classes.pkl', 'rb') as file:
    classes = pickle.load(file)
with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('model/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

st1 = '''I always thought Java was pass-by-reference; however I\'ve seen a couple of blog posts (for example, this blog) that claim it\'s not. I don\'t think I understand the distinction they\'re making. \n\nWhat is the explanation?\n Is Java "pass-by-reference" or "pass-by-value"?'''

def get_tag(st1):
    return classes[np.where(model.predict(vectorizer.transform([preprocess_text(st1)])).flatten() == 1)]

# Sample data - replace this with your actual data
questions = [
    {
        'id': 1,
        'title': 'How to create a Flask app?',
        'content': 'I am new to Flask and want to learn how to create a basic app.',
        'tags': ['flask', 'python'],
    },
    # Add more questions
]


@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    recognize_from_microphone()
    return ("nothing")


@app.route('/')

def index():
    return render_template('index1.html', questions=questions)

@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        return render_template('question1.html', question=question)
    return "Question not found"

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        # Process the submitted question
        new_question = {
            'id': len(questions) + 1,
            'title': request.form['title'],
            'content': request.form['content'],
            "tags" : get_tag(request.form['content'] + request.form['title'])
        }
        if request.form['butt'] == 1:
            recognize_from_microphone()
        questions.append(new_question)
        return redirect(url_for('index'))
    return render_template('ask1.html')

if __name__ == '__main__':
    app.run(debug=True)
