from fastapi import APIRouter, Depends, HTTPException
from common.common_response import CommonResponse
from models import model
from schemas.schemas import QuestionBase
from config.dependency import db_dependency

router = APIRouter()

@router.get("/questions")
def read_questions():
    return {"questions": "This is a list of questions"}

@router.post("/questions")
async def create_questions(question: QuestionBase, db: db_dependency):
    try:
        db_question = model.Questions(question=question.question)
        db_question = model.Questions(question=question.question)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        for choice in question.choices:
            db_choice = model.Choices(choice=choice.choice, is_correct=choice.is_correct, question_id=db_question.id)
            db.add(db_choice)
            db.commit()
            db.refresh(db_choice)
        
    except Exception as e:
        db.rollback()
        return CommonResponse.create_response(400, "An error occurred", {"error":str(e)})
    return CommonResponse.create_response(200, "Question created successfully", {"question":question})   

@router.get("/questions/{question_id}")
def read_question(question_id: int, db: db_dependency):
    try:
        question = db.query(model.Questions).filter(model.Questions.id == question_id).first()
        if question is None:
            return CommonResponse.create_response(404, "Question not found")
        return CommonResponse.create_response(200, "Question retrieved successfully", {"question":question})
    except Exception as e:
        return CommonResponse.create_response(400, "An error occurred", {"error":str(e)})

