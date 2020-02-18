import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
import random

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'robot9000','localhost:5432',self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            "question" : "What is the large continental?",
            "answer" : "Asia",
            "category" : 7,
            "difficulty" : 2
        }
        self.previous_questions = [{
            "question" : "Which country won the first ever soccer World Cup in 1930?",
            "id" : 11,
            "category" : 4,
            "difficulty" : 4,
            "answer" : "Uruguay"
        }]
        self.questionCat = {
            "type" : "Sports",
            "id" : 4
        } 

    def tearDown(self):
        """Executed after reach test"""
        pass
    

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
    def test_404_error(self):
        res = self.client().get('/questions?page=200') 
        data = json.loads(res.data) 
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "not found resource") 

    def test_get_catagories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["categories"]))

    def test_delete_question(self):
        res = self.client().delete('/questions/14')
        data = json.loads(res.data)
        question = Question.query.filter(Question.id==6).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["question"]))
        self.assertEqual(data["deleted"],6) 
        self.assertEqual(question, None)

    def test_422_ques_Unprocessable(self):
        res = self.client().delete('/questions/10000') 
        data = json.loads(res.data) 
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "Unprocessable Entity")

    def test_searchQues(self):
        res = self.client().post('/searchQuestion', json={"searchTerm":"title"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 1)

    def test_searchQues_without_result(self):
        res = self.client().post('/searchQuestion', json={"searchTerm":"titleoorrp"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 0)
    

    def test_get_ques_by_category(self):
        res = self.client().get('/categories/4/questions')
        data = json.loads(res.data)
        question = Question.query.filter(Question.category==4).all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"])) 
        self.assertEqual(data["questions"], question)
         
    def test_404_ques_not_found_in_category(self):
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "not found resource")

    def test_create_ques(self):
        res = self.client().post('/questions',json= self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"])) 
        self.assertTrue(data["created"])

    def test_create_ques_with_wrong_data(self):
        res = self.client().post('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "internal server error")  

    def test_play_game(self):
        res = self.client().post('/quizzes',json= {"previous_questions" : self.previous_questions,"quiz_category" : self.questionCat})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["previous_questions"])
        self.assertEqual(len(data["question"]), 5)

    def test_play_game_500_error(self):
        res = self.client().post('/quizzes')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "internal server error")

    def test_play_game_400_error(self):
        res = self.client().post('/quizzes',json= {"previous_questions" : [], "quiz_category" : {"id":1000}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "bad request")      
    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()