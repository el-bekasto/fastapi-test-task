from fastapi import HTTPException

from .schemas import CreateGradeSchema, PatchGradeSchema

from src.db.models import Grade, Student


def create_grade_service(grade: CreateGradeSchema, session):
    """
    Логика создания оценки.
    """
    student = session.query(Student).get(grade.student_id)
    if not student:
        raise HTTPException(status_code=404, detail=f'Student with id {grade.student_id} not found.')
    grade = Grade(**dict(grade))
    session.add(grade)
    session.commit()
    return grade


def get_grade_service(grade_id: int, session):
    """
    Логика получения оценки.
    """
    grade = session.query(Grade).get(grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail=f'Grade with id {grade_id} not found.')
    return grade


def patch_grade_service(grade_id: int, updated_grade: PatchGradeSchema, session):
    """
    Логика изменения существующей оценки.
    """
    grade = session.query(Grade).get(grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail=f'Grade with id {grade_id} not found.')
    for k, v in updated_grade.model_dump(exclude_unset=True).items():
        setattr(grade, k, v)
    session.commit()
    return grade


def delete_grade_service(grade_id: int, session):
    """
    Логика удаления существующей оценки.
    """
    grade = session.query(Grade).get(grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail=f'Grade with id {grade_id} not found.')
    session.delete(grade)
    session.commit()
    return {'success': 'Grade deleted.'}
