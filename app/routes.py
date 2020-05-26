from flask import *
from app import app, db
from app.forms import SetQuizForm, DisplayQuizForm
from app.models import *

@app.route('/')
def mainPage():
    return render_template('index.html', title="Welcome")


@app.route('/displayQuiz', methods=['GET', 'POST'])
def displayQuiz():
    all_questions = Questions.query.all()
    return render_template('displayQuiz.html', questions=all_questions)


@app.route('/postQuiz', methods=['POST'])
def postQuiz():
    if request.method == "POST":
        score = 0
        maxScore = Questions.query.count()
        for q_id in range(1, maxScore + 1):
            # print(str(Questions.query.get(q_id).answer), request.form["question_" + str(q_id)], sep="\t")
            if str(Questions.query.get(q_id).answer) == request.form["question_" + str(q_id)]:
                score += 1
    return render_template('result.html', score=score, maxScore=maxScore)