from flask import *
from app import app, db
from flask_login import login_user, logout_user, login_required
from app.models import *
from app.forms import LoginForm, RegistrationForm



@app.route('/')
@app.route('/index')
def mainPage():
    return render_template('index.html', title="Welcome")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.email.data == 'cat@test.com':
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you signed up successfully!')
            return redirect(url_for('login'))
        else:
            flash('email should be an admin email')
    return render_template('signup.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('mainPage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('mainPage'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('mainPage'))

@app.route('/displayQuiz', methods=['GET', 'POST'])
@login_required
def displayQuiz():
    all_questions = Questions.query.all()
    return render_template('displayQuiz.html', questions=all_questions)


@app.route('/postQuiz', methods=['POST'])
def postQuiz():
    if request.method == "POST":
        score = 0
        maxscore = Questions.query.count()
        rightques=[]
        for q_id in range(1, maxscore + 1):
            # print(str(Questions.query.get(q_id).answer), request.form["question_" + str(q_id)], sep="\t")
            if str(Questions.query.get(q_id).answer) == request.form["question_" + str(q_id)]:
                score += 1
                rightques.append(q_id)

    return render_template('result.html', score=score, maxScore=maxscore, rightques=rightques)


@app.route('/adminEdit', methods=['POST'])
def edit():
    return render_template('AdminIndex.html')


