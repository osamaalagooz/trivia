import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_questions = questions[start:end]

  return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  @app.route('/categories', methods=["GET"])
  def get_categories():

      categories = Category.query.all()
      if len(categories) == 0:
        abort(404)
      data = {}
      for category in categories:
        i = category.id
        t = category.type
        data[str(i)] = t
    
      return jsonify({
        "success" : True,
        "categories" : data
      })
    
  
  @app.route('/questions', methods=["GET"])
  def get_questions():

      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)
      categories = Category.query.all()
      current_category = [category.format() for category in categories]

      if len(current_questions) == 0:
        abort(404)

      total_questions = len(Question.query.all())
      data = {}
      for category in categories:
        ids = category.id
        types = category.type
        data[str(ids)] = types
      return jsonify({
        "success" : True,
        "questions" : current_questions,
        "total_questions" : total_questions,
        "categories" : data,
        "current_category": current_category
      }) 
     
  @app.route('/questions/<int:question_id>', methods=["DELETE"])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'deleted': question_id,
        'question': current_questions,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)

  @app.route('/questions', methods=["POST"])
  def create_question():
    body = request.get_json()
    question = body.get('question', None)
    answer = body.get('answer', None)
    difficulty = body.get('difficulty', None)
    category = body.get('category', None)
    
    try:
      
        question = Question(question=question, answer=answer, difficulty=difficulty,category=category)
        question.insert()

        selection = Question.query.order_by(Question.difficulty).all()
        current_questions = paginate_questions(request,selection)
        return jsonify({
          "success" : True,
          "created" : question.id,
          "questions" : current_questions,
          "total_questions" : len(Question.query.all())
        })
    except:
      abort(500)  

  @app.route('/searchQuestion', methods=['POST'])
  def search_for_question():

        body = request.get_json()
        searchTerm= body.get('searchTerm', None)

        selection = Question.query.order_by(Question.difficulty).filter(Question.question.ilike("%{}%".format(searchTerm))).all()
        current_questions = paginate_questions(request, selection)
        category = []
        for any_question in current_questions:
          current_categories = Category.query.filter(Category.id == any_question.get("category")).all()
          for current_category in current_categories:
            category.append(q.format())

        return jsonify({
          "success" : True,
          "questions" : current_questions,
          "total_questions" : len(Question.query.all()),
          "current_category" : category

        })  
  
  @app.route('/categories/<int:categore_id>/questions', methods=["GET"])
  def get_ques_by_cat(categore_id):

        selection = Question.query.filter(Question.category==categore_id).all()
        current_questions = paginate_questions(request, selection)
        total_questions = len(Question.query.all())
        categories = Category.query.filter(Category.id==categore_id).all()
        formatted_category = [category.format() for category in categories]
        if len(current_questions) == 0:
          abort(404)
        return jsonify({
          "questions" : current_questions,
          "total_questions" : total_questions,
          "current_category" : formatted_category

        })
   
  @app.route('/quizzes', methods=["POST"])
  def play_game():
    body = request.get_json()
    previous_questions = body.get('previous_questions')
    quiz_cat = body.get('quiz_category')
    category_id = quiz_cat.get('id')

    try:
        if category_id:
          ques = Question.query.filter(Question.category==category_id).all()
          
          if len(ques) < 5:
            abort(404)

          questions = [q.format() for q in ques]
          availible_questions = []
          for x in questions :
              if x["id"] in previous_questions:
                continue
              availible_questions.append(x)
          current_question = random.choice(availible_questions)   
          return jsonify({
            "success" : True,
            "question" : current_question,
            "previous_questions" : previous_questions,
            "quizCategory" : quiz_cat
          })
        else:
          
            ques = Question.query.all()

            if len(ques) < 5:
              abort(404)

            questions = [q.format() for q in ques]
            availible_questions = []
            for x in questions :
              if x["id"] in previous_questions:
                continue
              availible_questions.append(x)
            current_question = random.choice(availible_questions)   
            return jsonify({
              "success" : True,
              "question" : current_question, # 5 unique questions (not repeted)
              "previous_questions" : previous_questions, 
              "quizCategory" : quiz_cat
            })
            
    except:
      abort(400)
  
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def bad_req(error):
    return jsonify({
      "success" : False,
      "message" : "bad request",
      "error" : 400
    }), 400
  @app.errorhandler(404)  
  def not_fond(error):
    return jsonify({
      "success" : False,
      "message":"not found resource",
      "error":404}), 404
  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      "seccess" : False,
      "message" : "internal server error",
      "error" : 500
    }), 500
  @app.errorhandler(422)
  def unprocessable_entity_error(error):
    return jsonify({
      "success" : False,
      "message" : "Unprocessable Entity",
      "error" : 422
    }), 422  
 
  return app

    