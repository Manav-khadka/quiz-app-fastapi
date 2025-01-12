from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from config.database import Base

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)

class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice = Column(String, index=True)
    is_correct = Column(Boolean, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))