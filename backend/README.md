# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Reference

### Getting Started:

- Base URL: At present this app can only be run locally and is not hosted as a base URL. 
           The backend app is hosted at the default, http://127.0.0.1:5000/, 
           which is set as a proxy in the frontend configuration.

- Authentication: This version of the application does not require authentication or API keys.    

### Error Handling:
         
Errors are returned as JSON objects in the following format:


            {
                "success": False, 
                "error": 400,
                "message": "bad request"
            }
        
The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 500: internal server error
      
## Endpoints

###GET /questions
 - General:

Returns a list of question objects,categories object, success value, and total number of questions
Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample: `curl http://127.0.0.1:5000/questions`
   
                 "categories": {
                    "1": "Art",
                    "3": "Science",
                    "4": "Sports",
                    "5": "History",
                    "6": "Entertainment",
                    "7": "Geography"
                },
                "current_category": null,
                "questions": [
                    {
                    "answer": "mo salah",
                    "category": 4,
                    "difficulty": 2,
                    "id": 29,
                    "question": "who is the best player in EGY"
                    },
                    {
                    "answer": "Russia",
                    "category": 7,
                    "difficulty": 3,
                    "id": 30,
                    "question": "What is the biggest country?"
                    },
                    {
                    "answer": "Tom Cruise",
                    "category": 6,
                    "difficulty": 4,
                    "id": 32,
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                    },
                    {
                    "answer": "Edward Scissorhands",
                    "category": 6,
                    "difficulty": 3,
                    "id": 33,
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                    },
                    {
                    "answer": "Jackson Pollock",
                    "category": 6,
                    "difficulty": 3,
                    "id": 34,
                    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
                    },
                    {
                    "answer": "Blood",
                    "category": 3,
                    "difficulty": 2,
                    "id": 35,
                    "question": "Hematology is a branch of medicine involving the study of what?"
                    },
                    {
                    "answer": "Adel Emam",
                    "category": 6,
                    "difficulty": 3,
                    "id": 36,
                    "question": "Who is the  best actress in egy"
                    },
                    {
                    "answer": "80",
                    "category": 6,
                    "difficulty": 3,
                    "id": 37,
                    "question": "What is the age of Adel Emam?"
                    },
                    {
                    "answer": "Mounir",
                    "category": 6,
                    "difficulty": 2,
                    "id": 38,
                    "question": "what is name of the king?"
                    },
                    {
                    "answer": "11",
                    "category": 4,
                    "difficulty": 2,
                    "id": 39,
                    "question": "What is the number of football team?"
                    }
                ],
                "success": true,
                "total_questions": 36
                }
### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.

-Sample: `curl http://127.0.0.1:5000/categories`
        
                    "categories": {
                        "1": "Art",
                        "3": "Science",
                        "4": "Sports",
                        "5": "History",
                        "6": "Entertainment",
                        "7": "Geography"
                    },
                    "success": true
                    }
                    
### DELETE /questions/{question_id}
- General:
        Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, 
        total questions, and question list based on current page number to update the frontend.
- sample :
`curl -X DELETE http://127.0.0.1:5000/questions/38`
            
                "deleted": 38,
                "question": [
                    {
                    "answer": "mo salah",
                    "category": 4,
                    "difficulty": 2,
                    "id": 29,
                    "question": "who is the best player in EGY"
                    },
                    {
                    "answer": "Russia",
                    "category": 7,
                    "difficulty": 3,
                    "id": 30,
                    "question": "What is the biggest country?"
                    },
                    {
                    "answer": "Tom Cruise",
                    "category": 6,
                    "difficulty": 4,
                    "id": 32,
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                    },
                    {
                    "answer": "Edward Scissorhands",
                    "category": 6,
                    "difficulty": 3,
                    "id": 33,
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                    },
                    {
                    "answer": "Jackson Pollock",
                    "category": 6,
                    "difficulty": 3,
                    "id": 34,
                    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
                    },
                    {
                    "answer": "Blood",
                    "category": 3,
                    "difficulty": 2,
                    "id": 35,
                    "question": "Hematology is a branch of medicine involving the study of what?"
                    },
                    {
                    "answer": "Adel Emam",
                    "category": 6,
                    "difficulty": 3,
                    "id": 36,
                    "question": "Who is the  best actress in egy"
                    },
                    {
                    "answer": "80",
                    "category": 6,
                    "difficulty": 3,
                    "id": 37,
                    "question": "What is the age of Adel Emam?"
                    },
                    {
                    "answer": "11",
                    "category": 4,
                    "difficulty": 2,
                    "id": 39,
                    "question": "What is the number of football team?"
                    },
                    {
                    "answer": "Brazil",
                    "category": 4,
                    "difficulty": 4,
                    "id": 41,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                    }
                ],
                "success": true,
                "total_questions": 35
                }
### POST /questions
- General:
If provided, creates a new question. Returns the success value and id of the created question,
a list of objects questions and the number of total_questions.

- sample: 
    ```curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" 
    -d {"id":38,"question":"what is name of the king?", "answer" : "Mounir", "difficulty":2,"category":6}```

                "created": 38,
                "question": [
                    {
                    "answer": "mo salah",
                    "category": 4,
                    "difficulty": 2,
                    "id": 29,
                    "question": "who is the best player in EGY"
                    },
                    {
                    "answer": "Russia",
                    "category": 7,
                    "difficulty": 3,
                    "id": 30,
                    "question": "What is the biggest country?"
                    },
                    {
                    "answer": "Tom Cruise",
                    "category": 6,
                    "difficulty": 4,
                    "id": 32,
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                    },
                    {
                    "answer": "Edward Scissorhands",
                    "category": 6,
                    "difficulty": 3,
                    "id": 33,
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                    },
                    {
                    "answer": "Jackson Pollock",
                    "category": 6,
                    "difficulty": 3,
                    "id": 34,
                    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
                    },
                    {
                    "answer": "Blood",
                    "category": 3,
                    "difficulty": 2,
                    "id": 35,
                    "question": "Hematology is a branch of medicine involving the study of what?"
                    },
                    {
                    "answer": "Adel Emam",
                    "category": 6,
                    "difficulty": 3,
                    "id": 36,
                    "question": "Who is the  best actress in egy"
                    },
                    {
                    "answer": "80",
                    "category": 6,
                    "difficulty": 3,
                    "id": 37,
                    "question": "What is the age of Adel Emam?"
                    },
                    {
                    "answer": "11",
                    "category": 4,
                    "difficulty": 2,
                    "id": 39,
                    "question": "What is the number of football team?"
                    },
                    {
                    "answer": "Brazil",
                    "category": 4,
                    "difficulty": 4,
                    "id": 41,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                    }
                ],
                "success": true,
                "total_questions": 36
                }

### GET categories/<int:categore_id>/questions
- General:
Returns a list of question objects under specific category(category_id), success value, and total number of questions, 
current_category, Results are paginated in groups of 10.

- Sample: `curl http://127.0.0.1:5000/categories/3/questions`
      
            "current_category":{
                     "type" : "Science",
                     "id" : "3"
                     }          
            "questions": [
                {
                "answer": "Blood",
                "category": 3,
                "difficulty": 2,
                "id": 35,
                "question": "Hematology is a branch of medicine involving the study of what?"
                },
                {
                "answer": "Liver",
                "category": 3,
                "difficulty": 4,
                "id": 46,
                "question": "What is the heaviest organ in the human body?"
                },
                {
                "answer": "Alexander Fleming",
                "category": 3,
                "difficulty": 4,
                "id": 51,
                "question": "Who discovered penicillin?"
                },
                {
                "answer": "3Ib",
                "category": 3,
                "difficulty": 3,
                "id": 60,
                "question": "How much is the brain weight?"
                },
                {
                "answer": "Masseter",
                "category": 3,
                "difficulty": 5,
                "id": 61,
                "question": "What is the strongest muscle in the human body?"
                },
                {
                "answer": "5liters",
                "category": 3,
                "difficulty": 3,
                "id": 62,
                "question": "How much is Blood in the body"
                }
            ],
            "total_questions": 35
            }
### POST /searchQuestion 

- General:
It provides a keywords for questions and return a list of questions objects,
and the chosen category

- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d {"searchTerm":"title"}`

       "current_category":
                {
                 "type" : "Entertainment",
                 "id" : "6"
                 }          
       "questions": [{
            "answer": "Edward Scissorhands",
            "category": 6,
            "difficulty": 3,
            "id": 33,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?" 
           }]
           "success": True,
           "total_questions": 35

### POST /quizzes

- General:

   It provides a list of previous_questions objects and specific category (not necessary) and return a list of questions objects,
   success value, and list of previous_questions objects and quizCategory
   Results are paginated in groups of 10.

- Sample: 
      ```curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" 
         -d {"previous_questions" : [{"answer": "Blood",
                                    "category": 3,
                                    "difficulty": 3,
                                    "id": 35,
                                    "question": "Hematology is a branch of medicine involving the study of what?"}],
                                    {"type": "Science", "id": 3}
                                    }```     
                    
                    "questions": [
                        {
                        "answer": "Liver",
                        "category": 3,
                        "difficulty": 4,
                        "id": 46,
                        "question": "What is the heaviest organ in the human body?"
                        },
                        {
                        "answer": "Alexander Fleming",
                        "category": 3,
                        "difficulty": 4,
                        "id": 51,
                        "question": "Who discovered penicillin?"
                        },
                        {
                        "answer": "3Ib",
                        "category": 3,
                        "difficulty": 3,
                        "id": 60,
                        "question": "How much is the brain weight?"
                        },
                        {
                        "answer": "Masseter",
                        "category": 3,
                        "difficulty": 5,
                        "id": 61,
                        "question": "What is the strongest muscle in the human body?"
                        },
                        {
                        "answer": "5liters",
                        "category": 3,
                        "difficulty": 3,
                        "id": 62,
                        "question": "How much is Blood in the body"
                        }
                    ],
                    "previous_questions": [
                         {
                        "answer": "Blood",
                        "category": 3,
                        "difficulty": 2,
                        "id": 35,
                        "question": "Hematology is a branch of medicine involving the study of what?"
                        }
                    ],
                    "success" : True,
                    "quizCategory" : {
                        "type": "Science", 
                        "id": 3
                    }


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```