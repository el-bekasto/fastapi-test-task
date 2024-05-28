from fastapi import APIRouter

router = APIRouter(prefix='/student')


@router.post('')
async def create_student():
    pass


@router.get('/{student_id}')
async def get_student():
    pass


@router.patch('/{student_id}')
async def change_student():
    pass


@router.delete('/{student_id}')
async def delete_student():
    pass
