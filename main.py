from fastapi import FastAPI

from src.app.routers.grades import grade_router
from src.app.routers.students import student_router


# теги для разделения документации эндпоинтов в OpenAPI
openapi_tags = [
    {'name': 'student', 'description': 'Эндпоинты для манипуляций над студентами.'},
    {'name': 'grade', 'description': 'Эндпоинты для манипуляций над оценками.'}
]
app = FastAPI(openapi_tags=openapi_tags)

# добавляем в приложение роутеры
app.include_router(student_router, tags=['student'])
app.include_router(grade_router, tags=['grade'])
