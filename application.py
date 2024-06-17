from fastapi import FastAPI, HTTPException
from models.curriculum import Curriculum
from json_db import JsonDB
from pydantic import BaseModel

app = FastAPI()
db = JsonDB('./data/curriculum.json')


@app.get("/curriculum")
def get_Curriculum():
    try:
        Curriculum = db.read()
        return {"Curriculum": Curriculum['curriculum']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/add_curriculum")
def create_curriculum(curriculum: Curriculum):
    try:
        db.insert(curriculum)
        return {"message": "Curriculum added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))