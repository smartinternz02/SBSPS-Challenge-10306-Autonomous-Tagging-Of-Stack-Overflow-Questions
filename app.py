from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined list of tags
tags_list = ['python', 'flask', 'web development', 'machine learning', 'data science', 'javascript', 'html', 'css']
relevant_tag = ["python" , "beginner"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        selected_tags = request.form.getlist('tags')

        # Process the selected tags here (you can customize this part)
        relevant_tags = [tag for tag in selected_tags if tag in tags_list]

        return render_template('result.html', question=question, relevant_tags=relevant_tag)

    return render_template('index.html', tags_list=tags_list)

if __name__ == '__main__':
    app.run(debug=True)
