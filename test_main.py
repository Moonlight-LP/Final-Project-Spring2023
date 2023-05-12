import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_greetings():
    response = client.get("/")
    assert response.json() == {"message": "Hey, this is my Final Project Spring2023, hope it works :)"}
    assert response.status_code == 200
    
def test_questions():
    response = client.get("/questions")
    assert response.status_code == 200

def test_read_all_answers():
    response = client.get("/answers")
    assert response.status_code == 200
    #assert response
    

# def test_create_answer():
#     create_answer_data = {"answer": "fox"}
#     #do something like user input
#     response = client.post("/answers", create_answer_data)
#     #expected result
#     assert response == {"fox"}
    
def test_create_answer():
    answer_test_data = {"answer_id": "fox"}
    response = client.post("/answers", answer_test_data)
    assert response == {"answer_id": "1"}, {
    "answer": "fox",
    "points": 100
    }
    
def test_solution():
    response = client.delete("/answers/{}")
    assert response.status_code == 200
    assert response.json() == {"message": "List is empty. Try again"}