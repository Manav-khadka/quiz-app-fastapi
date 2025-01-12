from typing import Annotated, List
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
import models.model as model
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session
from routes.routes import router

app = FastAPI()
model.Base.metadata.create_all(bind=engine)
app.include_router(router)

