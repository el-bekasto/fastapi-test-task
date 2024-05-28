from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    CheckConstraint,
    ForeignKey,
    case,
    select,
    func
)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

from .database import Base


# модуль с моделями нашего приложения

class Student(Base):
    """
    Модель таблицы с данными об учениках.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    @hybrid_property
    def full_name(self):
        """
        Получение полного имени ученика.
        """
        return self.first_name + ' ' + self.last_name

    @hybrid_property
    def rating(self):
        """
        Получение средней оценки ученика. Имплементация уровня объекта
        """
        try:
            return sum([g.value for g in self.my_grades]) / len(self.my_grades)
        except ZeroDivisionError:
            return None

    @rating.expression
    def rating(cls):
        """
        Получение средней оценки ученика. Имплементация уровная класса для использования в запросах, например
        """
        return case(
            (
                cls.my_grades.any(),
                select(func.avg(Grade.value)).where(Grade.student_id == cls.id).scalar_subquery()
            ),
            else_=None
        )


class Grade(Base):
    """
    Модель таблицы с данными оценок учеников. student_id указывает какому именно ученику поставили оценку.
    """
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', backref='my_grades', foreign_keys=[student_id])
    description = Column(String(1000), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    @validates('value')
    def validate_value(self, key, value):
        """
        Валидируем значение оценки, чтобы она была между 1 и 5.
        """
        if not 0 < value < 6:
            raise ValueError('Invalid value. It should be between 1 and 5.')
        return value
