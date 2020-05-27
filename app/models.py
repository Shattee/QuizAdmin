from app import db,login, admin
from flask import abort
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password= db.Column(db.String(20))
    email = db.Column(db.String(120))
    isAdmin = db.Column(db.Boolean, default= True)
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        if str(self.password) == str(password):
            return True

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1200), unique=True)
    optionA = db.Column(db.String(200))
    optionB = db.Column(db.String(200))
    optionC = db.Column(db.String(200))
    optionD = db.Column(db.String(200))
    answer = db.Column(db.String(200))

    def __repr__(self):
        return f"Questions('{self.question}', '{self.optionA}', '{self.optionB}', '{self.optionC}', '{self.optionD}'," \
               f" '{self.answer}') "

class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.isAdmin == True:
            return current_user.is_authenticated
        else:
            return abort(404)
admin.add_view(MyModelView(Questions, db.session))
admin.add_view(MyModelView(User, db.session))


