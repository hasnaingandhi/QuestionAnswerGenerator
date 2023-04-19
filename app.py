from flask import Flask, flash, request, render_template, Response

import pandas as pd
import csv
import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
airbnb = pd.read_csv("https://raw.githubusercontent.com/dev7796/data101_tutorial/main/files/dataset/airbnb.csv")

aggregates = ['min', 'max', 'mean']

attributes = ['price']
cat_attributes = ['room_type', 'neighbourhood', 'neighbourhood_group']

cat_values = {}
for cat_attr in cat_attributes:
    cat_values[cat_attr] = airbnb[cat_attr].unique().tolist()

def generate_questions():
    n = int(request.form['n'])
    
    aggregate = random.choice(aggregates)
    attribute = random.choice(attributes)
    conditions = []
    for cat_attr in cat_attributes:
        cat_value = random.choice(cat_values[cat_attr])
        conditions.append(f"{cat_attr}='{cat_value}'")
    condition = " and ".join(conditions)
    
    question = f"What is the {aggregate} {attribute} when {condition}"
    return question

def generate_csv(n):

    questions = []
    for i in range(n):
        question = generate_questions()
        questions.append(question)
    df = pd.DataFrame({'Question': questions})
    df.to_csv('generated_questions.csv', index=False)
    return questions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET','POST'])
def generate():
    if request.method == 'POST':
        n = int(request.form['n'])
        if n>1000:
            return render_template('index.html')
        questions = generate_csv(n)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)