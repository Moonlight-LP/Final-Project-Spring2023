"""
❤ Final Project Spring 2023 ❤
❤ Simple Quiz ❤
"""


#Imports

#import uuid
from fastapi import FastAPI # , HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass
from typing import Dict #, Optional, Union
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


# check start

start = {}
start["is_start"] = "no"


#classes

@dataclass
class Answer:
    question: str
    answer: str

@dataclass        
class Question:
    question: str

@dataclass
class FirstQuestion:
    first_question: str = "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored"


# assign answers Dict

all_answers: Dict[str, Answer] = {}


# assign questions   

all_questions: Dict[str, Question] = {}

all_questions[1] = {
"question" : "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored"
}
all_questions[2] = {
"question" : "What animal makes miau?"
}
all_questions[3] = {
"question" : "What animal is barking?"
}
all_questions[4] = {
"question" : "Guess my favorite color"
}
all_questions[5] = {
"question" : "Do you like this app?"
}


#assign right answers

right_answers: Dict[str, Answer] = {}

right_answers["1"] = {
    "question": "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored",
    "answer": "fox"
}
right_answers["2"] = {
    "question": "What animal makes miau?",
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


#assign right answers capitalized

right_answers_caps: Dict[str, Answer] = {}

right_answers_caps["1"] = {
    "question": "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored",
    "answer": "Fox"
}
right_answers_caps["2"] = {
    "question": "What animal makes miau?",
    "answer": "Cat"
}
right_answers_caps["3"] = {
    "question": "what animal is barking?:",
    "answer": "Dog"
}
right_answers_caps["4"] = {
    "question": "guess whats my favorite color?:",
    "answer": "Pink"
}
right_answers_caps["5"] = {
    "question": "do you like this app?:",
    "answer": "Yes"
}


#assign right answers but doesnt like the app

almost_right_answers: Dict[str, Answer] = {}

almost_right_answers["1"] = {
    "question": "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored",
    "answer": "fox"
}
almost_right_answers["2"] = {
    "question": "What animal makes miau?",
    "answer": "cat"
}
almost_right_answers["3"] = {
    "question": "what animal is barking?:",
    "answer": "dog"
}
right_answers["4"] = {
    "question": "guess whats my favorite color?:",
    "answer": "pink"
}
almost_right_answers["5"] = {
    "question": "do you like this app?:",
    "answer": "no"
}


#assign right answers but doesnt like the app capitalized

almost_right_answers_caps: Dict[str, Answer] = {}

almost_right_answers_caps["1"] = {
    "question": "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored",
    "answer": "fox"
}
almost_right_answers_caps["2"] = {
    "question": "What animal makes miau?",
    "answer": "Cat"
}
almost_right_answers_caps["3"] = {
    "question": "what animal is barking?:",
    "answer": "Dog"
}
right_answers["4"] = {
    "question": "guess whats my favorite color?:",
    "answer": "Pink"
}
almost_right_answers_caps["5"] = {
    "question": "do you like this app?:",
    "answer": "No"
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

def load_right_answers_caps():
    with open("right_answers_caps.txt", "a+") as right_answers_caps_list_file:
        data = right_answers_caps_list_file.read()
        if data:
            right_answers_caps.update(json.loads(data))

def load_almost_right_answers():
    with open("almost_right_answers.txt", "a+") as almost_right_answers_list_file:
        data = almost_right_answers_list_file.read()
        if data:
            almost_right_answers.update(json.loads(data))
            
def load_almost_right_answers_caps():
    with open("almost_right_answers_caps.txt", "a+") as almost_right_answers_caps_list_file:
        data = almost_right_answers_caps_list_file.read()
        if data:
            almost_right_answers_caps.update(json.loads(data))

def load_start():
    with open("start.txt", "a+") as start_list_file:
        data = start_list_file.read()
        if data:
            start.update(json.loads(data))


#Greeting Site

@app.get("/")
async def greetings():
    return "❤ Hey, this is my Final Project Spring2023, hope you like it ❤"


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
async def create_answer(answer: Answer, start_quiz = "start"):
    
    with open("all_answers.txt", "r") as all_answers_list_file:
        data = all_answers_list_file.read()
        if data:
            all_answers.update(json.loads(data))
    with open("all_questions.txt", "r") as all_questions_list_file:
        data = all_questions_list_file.read()
        if data:
            all_questions.update(json.loads(data))
    with open("start.txt", "a+") as start_list_file:
        data = start_list_file.read()
        if data:
            start.update(json.loads(data))
    
    if start_quiz == "start":
        if start["is_start"] == "no":
            start["is_start"] = "start"
            with open("start.txt", "w+") as start_list_file:
                start_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            if len(all_answers) == 1:
                return "2. question: What animal makes miau?"
            if len(all_answers) == 2:
                return "3. What animal is barking?"
            if len(all_answers) == 3:
                return "4. question: Guess my favorite color"
            if len(all_answers) == 4:
                return "5. question: Do you like this app?"
            if len(all_answers) == 5:
                return "no more questions, please check solution"
            return "First question is: Guess my favorite animal, it lives in the forest, is very smart and orange-white colored"

        if start["is_start"] == "start":
            if len(all_answers) == 0:
                answer.question = "Guess my favorite animal, it lives in the forest, is very smart and orange-white colored"
                answer_key = "1"
                all_answers[answer_key] = answer
                with open("all_answers.txt", "w+") as all_answers_list_file:
                    all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                return answer, "next question is:", all_questions[2]
            if len(all_answers) == 1:
                answer.question = "What animal makes miau?"
                answer_key = str(len(all_answers) + 1)
                all_answers[answer_key] = answer
                with open("all_answers.txt", "w+") as all_answers_list_file:
                    all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                return answer,"next question is:", all_questions[3]
            if len(all_answers) == 2:
                answer.question = "What animal is barking?"
                answer_key = str(len(all_answers) + 1)
                all_answers[answer_key] = answer
                with open("all_answers.txt", "w+") as all_answers_list_file:
                    all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                return answer,"next question is:", all_questions[4]    
            if len(all_answers) == 3:
                answer.question = "Guess my favorite color"
                answer_key = str(len(all_answers) + 1)
                all_answers[answer_key] = answer
                with open("all_answers.txt", "w+") as all_answers_list_file:
                    all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                return answer,"next question is:", all_questions[5]
            if len(all_answers) == 4:
                answer.question = "Do you like this app?"
                answer_key = str(len(all_answers) + 1)
                all_answers[answer_key] = answer
                with open("all_answers.txt", "w+") as all_answers_list_file:
                    all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                return answer, "Quiz is done, please click solution in delete request"
            if len(all_answers) == 5:
                return {"message": "no more questions"}
        
        return {"message": "something went wrong"}
    
    return {"message": "start quiz description has to be start to start the quiz"}


@app.post("/hint")
async def get_hint(Need_hint_for_question = "please type question number"):
    if Need_hint_for_question == "1":
        return "Kind of like a dog with a fluffy tail, very smart, orange-white colored, lives in the forest"
    if Need_hint_for_question == "2":
        return "Miau, I am a little tiger, sometimes I try to roar like a Lion but it only comes out meeow"
    if Need_hint_for_question == "3":
        return "I like to go out and play get the ball, sometimes I try to howl like a wolf, but usually its a wuff"
    if Need_hint_for_question == "4":
        return "Very beautiful color, usually for girls"
    if Need_hint_for_question == "5":
        return "Do you like the app? :)"
    return "Please type the question number"


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
    with open("right_answers_caps.txt", "r") as right_answers_caps_list_file:
        data = right_answers_caps_list_file.read()
        if data:
            right_answers_caps.update(json.loads(data))
    with open("almost_right_answers.txt", "r") as almost_right_answers_list_file:
        data = almost_right_answers_list_file.read()
        if data:
            almost_right_answers.update(json.loads(data))
    with open("almost_right_answers_caps.txt", "r") as almost_right_answers_caps_list_file:
        data = almost_right_answers_caps_list_file.read()
        if data:
            almost_right_answers_caps.update(json.loads(data))
    with open("start.txt", "a+") as start_list_file:
        data = start_list_file.read()
        if data:
            start.update(json.loads(data))        
    
    if all_answers:
        if len(all_answers) >= 1 and len(all_answers) < 5:
            all_answers.clear()
            start["is_start"] = "no"
            with open("all_answers.txt", "w") as all_answers_list_file:
                all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))             
            with open("start.txt", "w+") as start_list_file:
                start_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            return {"message": "List was not finished. Try again"}
        
        if all_answers == right_answers or all_answers == right_answers_caps:
            all_answers.clear()
            start["is_start"] = "no"
            with open("all_answers.txt", "w") as all_answers_list_file:
                all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            with open("start.txt", "w+") as start_list_file:
                start_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            return {"message":"You won! ♡⸜(ˆᗜˆ˵ )⸝♡"}
        
        if all_answers == almost_right_answers or almost_right_answers_caps:
            all_answers.clear()
            start["is_start"] = "no"
            with open("all_answers.txt", "w") as all_answers_list_file:
                all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            with open("start.txt", "w+") as start_list_file:
                start_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
            return {"message":"Do you have any suggestions for improvement?"}
        
        all_answers.clear()
        start["is_start"] = "no"
        with open("all_answers.txt", "w") as all_answers_list_file:
            all_answers_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        with open("start.txt", "w+") as start_list_file:
            start_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                
        return {"message": "You loose this time. Try again"}
    
    start["is_start"] = "no"
    with open("start.txt", "w+") as start_list_file:
        start_list_file.write(json.dumps(all_answers, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    
    return {"message": "List is empty. Try again"}


#Standard App Execution

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=4557,
                reload=True,
                log_level="info")