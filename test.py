from src.db.database import SessionLocal
from src.db.models import Student, Grade

from sqlalchemy.sql.selectable import Select

session = SessionLocal()
# session.add(Grade(value=5, student_id=1))
# session.commit()
# beka = session.query(Student).where(Student.rating == 5).first()
print(session)
# Select.as_scalar