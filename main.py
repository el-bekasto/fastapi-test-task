from fastapi import FastAPI

from src.app.routers.grades import grade_router
from src.app.routers.students import student_router


openapi_tags = [
    {'name': 'student'},
    {'name': 'grade'}
]
app = FastAPI(openapi_tags=openapi_tags)

app.include_router(student_router, tags=['student'])
app.include_router(grade_router, tags=['grade'])
