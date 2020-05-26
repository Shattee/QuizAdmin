from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)    # Database
migrate = Migrate(app, db)    # Migration Engine
admin = Admin(app)

from app import routes, models
from app.models import Questions, qSet

admin.add_view(ModelView(Questions, db.session))
admin.add_view(ModelView(qSet, db.session))
db.drop_all()
db.create_all()

s1 = qSet(id=1, name="Set1")
s2 = qSet(id=2, name="Set2")
db.session.add_all([s1, s2])
db.session.commit()

q1 = Questions(id=1, question="How old are you?", optionA="3", optionB="13", optionC="11",
               optionD="20", answer="D", setId=1)
q2 = Questions(id=2, question="How tall are you?", optionA="163", optionB="1323", optionC="110",
               optionD="150", answer="A", setId=2)
db.session.add_all([q1, q2])
db.session.commit()