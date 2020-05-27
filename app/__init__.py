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

#insert default questions
q1 = Questions(id=1, question=" To avoid last minute moves, you should be looking down the road to "
                              "where your vehicle will be in about ______________.", optionA="5 to 10 seconds",
               optionB="10 to 15 seconds", optionC="15 to 20 seconds", optionD="10 to 20 seconds", answer="C")

q2 = Questions(id=2, question="A white painted curb means: ", optionA="Loading zone for freight or passengers.",
               optionB="Loading zone for passengers or mail only.", optionC="Loading zone for freight only.",
               optionD="Loading zone only for mail", answer="B")

q3 = Questions(id=3, question="When driving in fog, you should use your: ", optionA="Fog lights only.",
               optionB="High beams.",
               optionC="Low beams.", optionD="Fog lights and Low beams.", answer="C")

q4 = Questions(id=4, question="You may drive off of the paved roadway to pass another vehicle:",
               optionA="If the shoulder is wide enough to accommodate your vehicle.",
               optionB="If the vehicle ahead of you is turning left.",
               optionC="Under no circumstances.", optionD="If the vehicle ahead of you not so far", answer="C")

q5 = Questions(id=5, question="When you are merging onto the freeway, you should be driving:",
               optionA="At or near the same speed as the traffic on the freeway.",
               optionB="5 to 10 MPH slower than the traffic on the freeway.",
               optionC="The posted speed limit for traffic on the freeway.",
               optionD="Slow down the speed at the traffic", answer="A")

q6 = Questions(id=6, question="A pre-trip inspection should be completed:", optionA="before operating the vehicle.",
               optionB="if any problems occurred the last the time the vehicle was operated.",
               optionC="at least once a week.", optionD="at least twice a week", answer="A")

q7 = Questions(id=7, question="Roadways are the most slippery: ",
               optionA="During a heavy downpour.", optionB="After it has been raining for awhile.",
               optionC="The first rain after a dry spell.", optionD="After a heavy downpour",
               answer="C")

q8 = Questions(id=8, question="You may legally block an intersection: ",
               optionA="When you entered the intersection on the green light.", optionB="Under no circumstances.",
               optionC="During rush hour traffic.", optionD="After officer's permission", answer="B")


db.session.add_all([q1, q2, q3, q4, q5, q6, q7, q8])
db.session.commit()