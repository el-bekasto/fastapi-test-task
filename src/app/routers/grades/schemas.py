from pydantic import BaseModel, Field
from datetime import datetime


class CreateGradeSchema(BaseModel):
    """
    Схема создания объекта оценки
    """
    value: int = Field(ge=1, le=5)
    student_id: int
    description: str | None = Field(None, max_length=1000)


class GetGradeSchema(CreateGradeSchema):
    """
    Схема получения объекта оценки. Просто добавляет поля айди и дат изменений в схему создания.
    """
    id: int
    created_at: datetime
    updated_at: datetime | None


class PatchGradeSchema(BaseModel):
    """
    Схема изменения объекта оценки.
    """
    value: int | None = Field(None, ge=1, le=5)
    description: str | None = Field(None, max_length=1000)
