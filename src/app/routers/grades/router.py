from fastapi import APIRouter, Depends

from .schemas import (
    CreateGradeSchema,
    GetGradeSchema,
    PatchGradeSchema)
from .services import (
    create_grade_service,
    get_grade_service,
    patch_grade_service,
    delete_grade_service)

from src.app.dependencies import get_session

router = APIRouter(prefix='/grade')


@router.post('', response_model=GetGradeSchema, status_code=201)
async def create_grade(grade: CreateGradeSchema, session=Depends(get_session)):
    """
    Эндпоинт создания оценки.
    """
    return create_grade_service(grade, session)


@router.get('/{grade_id}', response_model=GetGradeSchema)
async def get_grade(grade_id: int, session=Depends(get_session)):
    """
    Эндпоинт получения оценки.
    """
    return get_grade_service(grade_id, session)


@router.patch('/{grade_id}', response_model=GetGradeSchema)
async def change_grade(grade_id: int, updated_grade: PatchGradeSchema, session=Depends(get_session)):
    """
    Эндпоинт изменения оценки.
    """
    return patch_grade_service(grade_id, updated_grade, session)


@router.delete('/{grade_id}')
async def delete_grade(grade_id: int, session=Depends(get_session)):
    """
    Эндпоинт удаления оценки.
    """
    return delete_grade_service(grade_id, session)
