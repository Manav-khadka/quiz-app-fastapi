# schemas.py
from pydantic import BaseModel
from typing import List

class ChoicesBase(BaseModel):
    choice: str
    is_correct: bool

class QuestionBase(BaseModel):
    question: str
    choices: List[ChoicesBase]
