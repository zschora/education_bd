# database_manager.py
from datetime import date

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from faker import Faker
from src.models import Teacher, Subject, Major, AssociationTeacherSubject, AssociationMajorSubject, Base
from random import randint

fake = Faker()


class DatabaseManager:
    def __init__(self, database_url="postgresql+psycopg2://postgres:12345@localhost/education"):
        self.engine = create_engine(database_url)
        self.engine.connect()
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_teachers(self):
        return self.session.query(Teacher).all()

    def get_subjects(self):
        return self.session.query(Subject).all()

    def get_majors(self):
        return self.session.query(Major).all()

    def add_teacher(self, code, name, lastname, birthday, position, degree):
        teacher = Teacher(
            code=code,
            name=name,
            lastname=lastname,
            birthday=birthday,
            position=position,
            degree=degree
        )
        self.session.add(teacher)
        self.session.commit()

    def add_subject(self, code, title, hours):
        subject = Subject(
            code=code,
            title=title,
            hours=hours
        )
        self.session.add(subject)
        self.session.commit()

    def add_major(self, code, title):
        major = Major(
            code=code,
            title=title
        )
        self.session.add(major)
        self.session.commit()

    def add_association_teacher_subject(self, teacher_code, subject_code):
        association = AssociationTeacherSubject(
            teacher_code=teacher_code,
            subject_code=subject_code
        )
        self.session.add(association)
        self.session.commit()

    def add_association_major_subject(self, major_code, subject_code):
        association = AssociationMajorSubject(
            major_code=major_code,
            subject_code=subject_code
        )
        self.session.add(association)
        self.session.commit()

    def add_random_data(self, teacher_count=5, subject_count=5, major_count=5):
        for i in range(teacher_count):
            self.add_teacher(
                code=i,
                name=fake.first_name()[:30],
                lastname=fake.last_name()[:30],
                birthday=fake.date_of_birth(),
                position=fake.job()[:30],
                degree=fake.random_element(elements=('PhD', 'MSc', 'BSc'))
            )

        for i in range(subject_count):
            self.add_subject(
                code=i,
                title=fake.word(),
                hours=fake.random_int(min=20, max=100)
            )

        for i in range(major_count):
            self.add_major(
                code=i,
                title=fake.word()
            )
            self.add_association_teacher_subject(i, i // 2)
            self.add_association_major_subject(i, i // 2)

        print('database filling completed')

    def change_teacher_position(self, teacher_code, new_position):
        print(teacher_code, new_position)
        try:
            teacher = self.session.query(Teacher).filter_by(code=teacher_code).first()

            if teacher:
                teacher.position = new_position
                self.session.commit()
                print(f"Должность преподавателя {teacher_code} успешно изменена на {new_position}")
            else:
                print(f"Преподаватель с CODE {teacher_code} не найден.")
        except Exception as e:
            print(f"Ошибка при изменении должности преподавателя: {e}")

    def get_courses_by_birth_year(self, birth_year):

        sql_query = text("""
            SELECT distinct subjects.title, subjects.hours
            FROM teachers
            JOIN association_teacher_subject ON teachers.code = association_teacher_subject.teacher_code
            JOIN subjects ON association_teacher_subject.subject_code = subjects.code
            WHERE date_part('year', teachers.birthday) > """ + f'{birth_year}')

        result = self.engine.connect().execute(sql_query)
        print(result)

        return result
