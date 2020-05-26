from app import db

class qSet(db.Model):
    __tablename__ = "qset"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    def __repr__(self):
        return '<qSet{}>'.format(self.id)

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1200), unique=True)
    optionA = db.Column(db.String(200))
    optionB = db.Column(db.String(200))
    optionC = db.Column(db.String(200))
    optionD = db.Column(db.String(200))
    answer = db.Column(db.String(200))
    setId = db.Column(db.Integer, db.ForeignKey('qset.id'))

    def __repr__(self):
        return f"Questions('{self.question}', '{self.optionA}', '{self.optionB}', '{self.optionC}', '{self.optionD}'," \
               f" '{self.answer}', '{self.setId}') "


