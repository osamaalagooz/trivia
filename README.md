# Trivia App

this my project for Udacity to prove that I have understood all subjects in APIs lesson for an example:
I can write a good APIs to handle the database by taking a specific request and return a response over an endpoint 
which I had been learned how to implement it with a good structure also, then I can test 
all my endpoints to ensure they work well    and do what I ask from them correctly.
now this project ready to show in it's home some of the questions with the ability to show them under a specific 
category or delete any one of them or search about any question by some keywords, 
you can add a new question or play a game by choosing from your favorite category or from 
all the questions and answering 5 questions get your final score.
    
all backend codes follow `PEP8 guideline`

## User guideline :
 
To play the game should be at least 6 questions at the chosen category.

## Getting Started:

### Pre-requisites and Local Development.
    
Developers using the project should have python3, PiP, node installed on thier machiens.

### Backend:

From the backend folder `../backend` run ```pip install -r requirements.txt```
all requered packeges included in the file

### To run the application run the following commends :

```bash
export FLASK_APP=flaskr
export FLASK_ENV=Development
flask run
```

this commends put the application in development and directes the application to use the `__init__.py` file in our flaskr
folder . working in development mode shows an interactive debugger in the console and restarts the server whenever
changes are made. if running locally on windows, look for the commends in the flask docs.

the application is run on http://127.0.0.1:500/ by default

### Frontend :

From the fronend folder `../frontend` run the following commends.

  ``` bash
  npm install // only once
  npm start
  ```

  by default the front end will run on localhost:3000.

## Tests:

From the backend folder `../backend` run the following commends.

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
the first time you run the tests, omit the dropdb commend

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

## Author:

### Osama (for the Back-End)
### Udacity Team (for the Front-End)


                   
