from fastapi import APIRouter, Depends

from .schemas import CreateStudentSchema, GetStudentSchema, PatchStudentSchema
from .services import create_student_service, get_student_service, patch_student_service, delete_student_service

from src.app.dependencies import get_session

router = APIRouter(prefix='/student')


@router.post('', response_model=GetStudentSchema, status_code=201)
async def create_student(student: CreateStudentSchema, session=Depends(get_session)):
    """
    Эндпоинт создания студента.
    """
    return create_student_service(student, session)


@router.get('/{student_id}', response_model=GetStudentSchema)
async def get_student(student_id: int, session=Depends(get_session)):
    """
    Эндпоинт получения студента.
    """
    return get_student_service(student_id, session)


@router.patch('/{student_id}', response_model=GetStudentSchema)
async def change_student(student_id, updated_student: PatchStudentSchema, session=Depends(get_session)):
    """
    Эндпоинт изменения студента.
    """
    return patch_student_service(student_id, updated_student, session)


@router.delete('/{student_id}')
async def delete_student(student_id: int, session=Depends(get_session)):
    """
    Эндпоинт удаления студента.
    """
    return delete_student_service(student_id, session)
