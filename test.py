from app import app, db
import unittest, os
from app.models import User, Questions

class FlaskTestCase(unittest.TestCase):
    # ensure flask set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/index',content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Sign In' in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', data = dict(username="admin", password
        ="admin"), follow_redirects=True)
        self.assertTrue(b'Welcome' in response.data)


class UserModel(unittest.TestCase):
    def setUp(self) -> None:
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
    def appendQues(self):

        q = Questions(id=50, question=" in fog, you should use your: ", optionA=" lights only.",
                       optionB="High beams.",
                       optionC="Low .", optionD="Fog lights and Low beams.", answer="C")
        db.session.add(q)
        db.session.commit()
        q1 = Questions.query.filter_by(id=50).first()
        self.assertIsNotNone(q1)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
