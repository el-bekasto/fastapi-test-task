from pydantic import BaseModel, Field
from datetime import datetime


class CreateStudentSchema(BaseModel):
    first_name: str
    last_name: str


class GetStudentSchema(CreateStudentSchema):
    id: int
    created_at: datetime
    updated_at: datetime | None


class PatchStudentSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
