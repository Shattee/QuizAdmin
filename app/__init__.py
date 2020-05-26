from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,current_user
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)    # Database
migrate = Migrate(app, db)    # Migration Engine
admin = Admin(app)
login = LoginManager(app)

from app import routes, models
from app.models import Questions, User


db.drop_all()
db.create_all()

u = User(id=1, username="Cat")

q1 = Questions(id=1, question="How old are you?", optionA="3", optionB="13", optionC="11",
               optionD="20", answer="D", setId=1)
q2 = Questions(id=2, question="How tall are you?", optionA="163", optionB="1323", optionC="110",
               optionD="150", answer="A", setId=2)
db.session.add_all([u, q1, q2])
db.session.commit()