from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        }
        questions.append(new_question)
        return redirect(url_for('index'))
    return render_template('ask1.html')

if __name__ == '__main__':
    app.run(debug=True)
