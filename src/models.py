from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Float, Integer, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Table
from datetime import date


class Base(DeclarativeBase):
    pass


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(Integer(), unique=True)
    title: Mapped[str] = mapped_column(String(30))
    hours: Mapped[int] = mapped_column(Integer())

    def __repr__(self) -> str:
        return f"Subject(code={self.code!r}, title={self.title!r}, hours={self.hours!r})"


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(Integer(), unique=True)
    name: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30), nullable=True)
    birthday: Mapped[date] = mapped_column(Date())
    position: Mapped[str] = mapped_column(String(30))
    degree: Mapped[str] = mapped_column(String(30))

    subjects: Mapped[List['Subject']] = relationship(secondary='association_teacher_subject')

    def __repr__(self) -> str:
        return f"Teacher(code={self.code!r}, name={self.name!r}, lastname={self.lastname!r}, " \
               f"birthday={self.birthday!r}, position={self.position!r}, degree={self.degree!r})"


class Major(Base):
    __tablename__ = "majors"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(Integer(), unique=True)
    title: Mapped[str] = mapped_column(String(30))

    subjects: Mapped[List['Subject']] = relationship(secondary='association_major_subject')

    def __repr__(self) -> str:
        return f"Major(code={self.code!r}, title={self.title!r})"


class AssociationTeacherSubject(Base):
    __tablename__ = 'association_teacher_subject'
    teacher_id = Column(Integer, ForeignKey('teachers.code'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.code'), primary_key=True)


class AssociationMajorSubject(Base):
    __tablename__ = 'association_major_subject'
    major_id = Column(Integer, ForeignKey('majors.code'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.code'), primary_key=True)