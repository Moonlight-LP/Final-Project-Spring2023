import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_greetings():
    response = client.get("/")
    assert response.json() == {"message": "❤ Hey, this is my Final Project Spring2023, hope you like it ❤"}
    assert response.status_code == 200
    
def test_questions():
    response = client.get("/questions")
    assert response.json() == {
    "1": {
        "question": "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored"
    },
    "2": {
        "question": "What animal makes miau?"
    },
    "3": {
        "question": "What animal is barking?"
    },
    "4": {
        "question": "Guess my favorite color"
    },
    "5": {
        "question": "Do you like this app?"
    }                
}
    assert response.status_code == 200

def test_read_all_answers():
    response = client.get("/answers")
    assert response.status_code == 200
#    assert response == {"message": "no answers"}
    

# def test_create_answer():
#     create_answer_data = {"answer": "fox"}
#     #do something like user input
#     response = client.post("/answers", create_answer_data)
#     #expected result
#     assert response == {"fox"}

# def test_get_hint():
#     question_no = "1"
#     response = client.post("/hint", question_no)
#     assert response.json() == "Kind of like a dog with a fluffy tail, very smart, orange-white colored, lives in the forest"
    
def test_create_answer():
    answer_test_data = "start"
    response = client.post("/answers", answer_test_data)
    assert response.json() == "start"
    
def test_get_hint():
    question_no = "please type question number"
    response = client.post("/hint", question_no)
    assert response.json() =="Please type the question number"
    
def test_solution():
    response = client.delete("/answers/{}")
    assert response.status_code == 200
    assert response.json() == {"message": "List is empty. Try again"}