from pydantic import BaseModel, Field
from datetime import datetime


class CreateStudentSchema(BaseModel):
    """
    Схема создания объекта студента
    """
    first_name: str
    last_name: str


class GetStudentSchema(CreateStudentSchema):
    """
    Схема получения объекта студента. Просто добавляет поля айди и дат изменений в схему создания.
    """
    id: int
    created_at: datetime
    updated_at: datetime | None


class PatchStudentSchema(BaseModel):
    """
    Схема изменения объекта студента.
    """
    first_name: str | None = None
    last_name: str | None = None
