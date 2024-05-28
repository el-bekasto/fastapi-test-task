from fastapi import HTTPException

from .schemas import CreateStudentSchema, PatchStudentSchema

from src.db.models import Student


def create_student_service(student: CreateStudentSchema, session):
    """
    Логика создания студента
    """
    student = Student(**dict(student))
    session.add(student)
    session.commit()
    return student


def get_student_service(student_id: int, session):
    """
    Логика получения студента
    """
    student = session.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail=f'Student with id {student} not found.')
    return student


def patch_student_service(student_id: int, updated_student: PatchStudentSchema, session):
    """
    Логика изменения существующего студента
    """
    student = session.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail=f'Student with id {student_id} not found.')
    for k, v in updated_student.model_dump(exclude_unset=True).items():
        setattr(student, k, v)
    session.commit()
    return student


def delete_student_service(student_id: int, session):
    """
    Логика удаления студента
    """
    student = session.query(Student).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail=f'Student with id {student_id} not found.')
    session.delete(student)
    session.commit()
    return {'success': 'Student deleted.'}
