#Final Project Spring 2023



#Imports

#import uuid
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass
from typing import Optional, Dict #/, Union
import json
import uvicorn
from tkinter import *
from pymongo import MongoClient


#setup MongoDB

CONNECTION_STRING = "mongodb+srv://moonlight:feelinara@atlascluster.z2gjoit.mongodb.net"

connection = MongoClient(CONNECTION_STRING)
db = connection.finalprojectspring2023


#Use FastApi

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


#classes

@dataclass
class Answer:
    question: str
    answer: str
    # answer_id: str
        
all_answers: Dict[str, Answer] = {}
        
@dataclass        
class Question:
    question: str
    
@dataclass
class FirstQuestion:
    first_question: str = "guess whats my favorite animal, lives in forest is very smart, orange white color:"
    

# assign questions   

all_questions: Dict[str, Question] = {}

all_questions[1] = {
"question" : "guess whats my favorite animal? lives in forest is very smart, orange white color:"
}
all_questions[2] = {
"question" : "what animal is this: miau?:"
}
all_questions[3] = {
"question" : "what animal is barking?:"
}
all_questions[4] = {
"question" : "guess whats my favorite color?:"
}
all_questions[5] = {
"question" : "do you like this app?:"
}


#assign right answers

right_answers: Dict[str, Answer] = {}

right_answers["1"] = {
    "question": "guess whats my favorite animal? lives in forest is very smart, orange white color:",
    "answer": "fox"
}
right_answers["2"] = {
    "question": "what animal is this: miau?:",
    "answer": "cat"
}
right_answers["3"] = {
    "question": "what animal is barking?:",
    "answer": "dog"
}
right_answers["4"] = {
    "question": "guess whats my favorite color?:",
    "answer": "pink"
}
right_answers["5"] = {
    "question": "do you like this app?:",
    "answer": "yes"
}


#load save files on startup

@app.on_event("startup")
def load_all_answers():
    with open("all_answers.txt", "a+") as all_answers_list_file:
        data = all_answers_list_file.read()
        if data:
            all_answers.update(json.loads(data))
            
def load_all_questions():
    with open("all_questions.txt", "r") as all_questions_list_file:
        data = all_questions_list_file.read()
        if data:
            all_questions.update(json.loads(data))
            
def load_right_answers():
    with open("right_answers.txt", "a+") as right_answers_list_file:
        data = right_answers_list_file.read()
        if data:
            right_answers.update(json.loads(data))


#Greeting Site

@app.get("/")
async def greetings():
    return {"message": "Hey, this is my Final Project Spring2023, hope it works :)"}


#list all questions

@app.get("/questions")
async def read_all_questions():
    with open("all_questions.txt", "r") as all_questions_list_file:
        data = all_questions_list_file.read()
        if data:
            all_questions.update(json.loads(data))
    
    return all_questions


#list all given answers

@app.get("/answers")
async def read_all_answers():
    with open("all_answers.txt", "r") as all_answers_list_file:
        data = all_answers_list_file.read()
        if data:
            all_answers.update(json.loads(data))
    
    if all_answers == {} or all_answers == None:
        return {"message": "no answers"}
    
    return all_answers


# posting answers

@app.post("/answers")
async def create_answer(answer: Answer, first_question: FirstQuestion):
    
    with open("all_answers.txt", "r") as all_answers_list_file:
        data = all_answers_list_file.read()
        if data:
            all_answers.update(json.loads(data))
    with open("all_questions.txt", "r") as all_questions_list_file:
        data = all_questions_list_file.read()
        if data:
            all_questions.update(json.loads(data))
    
    if len(all_answers) == 0:
        answer.question = "guess whats my favorite animal? lives in forest is very smart, orange white color:"
        answer_key = str(len(all_answers) + 1)
        all_answers[answer_key] = answer
        with open("all_answers.txt", "w+") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return answer, "next question is:", all_questions[2] #"guess whats my favorite animal? lives in forest is very smart, orange white color:"
        # answer.answer_id = question.question_id
    if len(all_answers) == 1:
        answer.question = "what animal is this: miau?:"
        answer_key = str(len(all_answers) + 1)
        all_answers[answer_key] = answer
        with open("all_answers.txt", "w+") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return answer,"next question is:", all_questions[3] # "what animal is this: miau?:"
        # answer.answer_id = question.question_id
    if len(all_answers) == 2:
        answer.question = "what animal is barking?:"
        answer_key = str(len(all_answers) + 1)
        all_answers[answer_key] = answer
        with open("all_answers.txt", "w+") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return answer,"next question is:", all_questions[4] # "what animal is barking?:"    
        # answer.answer_id = question.question_id
    if len(all_answers) == 3:
        answer.question = "guess whats my favorite color?:"
        answer_key = str(len(all_answers) + 1)
        all_answers[answer_key] = answer
        with open("all_answers.txt", "w+") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return answer,"next question is:", all_questions[5] #"guess whats my favorite color?:"
        # answer.answer_id = question.question_id
    if len(all_answers) == 4:
        answer.question = "do you like this app?:"
        answer_key = str(len(all_answers) + 1)
        all_answers[answer_key] = answer
        with open("all_answers.txt", "w+") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return answer, "Quiz is done, please click solution in delete request" #"do you like this app?:"
        # answer.answer_id = question.question_id
    if len(all_answers) == 5:
        return {"message": "no more questions"}
    
    return {"message": "something went wrong"}


#Solution, start Test new

@app.delete("/answers/{}")
async def solution():
    with open("all_answers.txt", "r") as all_answers_list_file:
        data = all_answers_list_file.read()
        if data:
            all_answers.update(json.loads(data))
    with open("right_answers.txt", "r") as right_answers_list_file:
        data = right_answers_list_file.read()
        if data:
            right_answers.update(json.loads(data))
    
    if all_answers:
        if len(all_answers) >= 1 and len(all_answers) < 5:
            all_answers.clear()
            with open("all_answers.txt", "w") as all_answers_list_file:
                all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            return {"message": "List was not finished. Try again"}
        
        if all_answers == right_answers:
            all_answers.clear()
            with open("all_answers.txt", "w") as all_answers_list_file:
                all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            return {"message":"You won!"}
        
        all_answers.clear()
        with open("all_answers.txt", "w") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))  
            
        return {"message": "You loose this time. Try again"}
    
    return {"message": "List is empty. Try again"}


#Standard App Execution

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=4557,
                reload=True,
                log_level="info")