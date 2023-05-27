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


#class User Answer Data to store

@dataclass
class Answer:
    answer: str
    answer_id: str
    points: int = 0
    
    def __init__self(self, points):
        self.points = points
        
all_answers: Dict[str, Answer] = {}
        
@dataclass        
class Question:
    question: str
    question_id: str
    
    # def __init__self(self, question, question_id):
    #     self.question = question
    #     self.question_id = question_id


question1 = Question
question1.question = "guess whats my favorite animal? lives in forest is very smart, orange white color:"
question1.question_id = 1

question2 = Question
question2.question = "what animal is this: miau?:"
question2.question_id = 2

question3 = Question
question3.question = "what animal is barking?:"
question3.question_id = 3

question4 = Question
question4.question = "guess whats my favorite color?:"
question4.question_id = 4

question5 = Question
question5.question = "do you like this app?:"
question5.question_id = 5


all_questions = [question1, question2, question3, question4, question5]


#load save file on startup

@app.on_event("startup")
def load_all_answers():
    with open("all_answers.txt", "a+") as all_answers_list_file:
        data = all_answers_list_file.read()
        if data:
            all_answers.update(json.loads(data))
            
def load_all_questions():
    with open("all_questions.txt", "a+") as all_questions_list_file:
        data = all_questions_list_file.read()
        if data:
            all_questions.update(json.loads(data))
            

#Greeting Site

@app.get("/")
async def greetings():
    return {"message": "Hey, this is my Final Project Spring2023, hope it works :)"}

@app.get("/Questions")
async def read_all_questions():
    with open("all_questions.txt", "r") as all_questions_list_file:
        data = all_questions_list_file.read()
        if data:
            all_questions.update(json.loads(data))
    
    if all_questions == {} or all_questions == None:
        return {"message": "no answers"}
    
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


#create answer

@app.post("/answers")
async def create_answer(question, answer: Answer):
    for question in all_questions:
        print(question.question)
        # assign answer_id to question_id
        if question.question_id == "1":
            answer.answer_id = "1"
            
        if question.question_id == "2":
            answer.answer_id = "2"
            
        if question.question_id == "3":
            answer.answer_id = "3"
            
        if question.question_id == "4":
            answer.answer_id = "4"
            
        if question.question_id == "5":
            answer.answer_id = "5"
            
        
        if answer.answer_id == "1":
            if answer.answer == "fox" or answer.answer == "Fox":
                answer.points = +100
                
        if answer.answer_id == "2":
            if answer.answer == "cat" or answer.answer == "Cat":
                answer.points = +100
                
        if answer.answer_id == "3":
            if answer.answer == "dog" or answer.answer == "Dog":
                answer.points = +100
                
        if answer.answer_id == "4":
            if answer.answer == "pink" or answer.answer == "Pink":
                answer.points = +100
                
        if answer.answer_id == "5":
            if answer.answer == "yes" or answer.answer == "Yes":
                answer.points = +100
            
        all_answers[answer.answer_id] = answer
    
        with open("all_answers.txt", "w+") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))

    return {"answer_id": answer.answer_id }, answer


#Solution, start Test new

@app.delete("/answers/{}")
async def solution(): 
    # get the sum of all answer points
    sum_points = 0
    for answer in all_answers.values():
        sum_points = sum_points + answer.points
    
    if all_answers:
        if sum_points >= 500:
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