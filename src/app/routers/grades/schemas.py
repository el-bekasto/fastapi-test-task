from pydantic import BaseModel, Field
from datetime import datetime


class CreateGradeSchema(BaseModel):
    value: int = Field(ge=1, le=5)
    student_id: int
    description: str | None = Field(None, max_length=1000)


class GetGradeSchema(CreateGradeSchema):
    id: int
    created_at: datetime
    updated_at: datetime | None


class PatchGradeSchema(BaseModel):
    value: int | None = Field(None, ge=1, le=5)
    description: str | None = Field(None, max_length=1000)
