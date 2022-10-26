from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Login(BaseModel):
    name: str
    password: str

class Register(BaseModel):
    name: str
    password: str
    account_type: str

class EditAccount(BaseModel):
    name: str
    password: str

class CreateClassroom(BaseModel):
    title: str
    description: str
    teacher_id: str

class DeleteClassroom(BaseModel):
    teacher_id: str

class AddClass(BaseModel):
    student_id: str
    class_id: str