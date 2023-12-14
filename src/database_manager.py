# database_manager.py
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from src.models import Teacher, Subject, Major, AssociationTeacherSubject, AssociationMajorSubject, Base

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

    def add_teacher(self, name, lastname, birthday, position, degree):
        teacher = Teacher(
            name=name,
            lastname=lastname,
            birthday=birthday,
            position=position,
            degree=degree
        )
        self.session.add(teacher)
        self.session.commit()

    def add_subject(self, title, hours):
        subject = Subject(
            title=title,
            hours=hours
        )
        self.session.add(subject)
        self.session.commit()

    def add_major(self, title):
        major = Major(
            title=title
        )
        self.session.add(major)
        self.session.commit()

    def add_association_teacher_subject(self, teacher_id, subject_id):
        association = AssociationTeacherSubject(
            teacher_id=teacher_id,
            subject_id=subject_id
        )
        self.session.add(association)
        self.session.commit()

    def add_association_major_subject(self, major_id, subject_id):
        association = AssociationMajorSubject(
            major_id=major_id,
            subject_id=subject_id
        )
        self.session.add(association)
        self.session.commit()

    def add_random_data(self, teacher_count=5, subject_count=5, major_count=5):
        for _ in range(teacher_count):
            self.add_teacher(
                name=fake.first_name(),
                lastname=fake.last_name(),
                birthday=fake.date_of_birth(),
                position=fake.job(),
                degree=fake.random_element(elements=('PhD', 'MSc', 'BSc'))
            )

        for _ in range(subject_count):
            self.add_subject(
                title=fake.word(),
                hours=fake.random_int(min=20, max=100)
            )

        for _ in range(major_count):
            self.add_major(
                title=fake.word()
            )

        teachers = self.session.query(Teacher).all()
        subjects = self.session.query(Subject).all()

        for teacher in teachers:
            for subject in subjects:
                self.add_association_teacher_subject(teacher.id, subject.id)

        majors = self.session.query(Major).all()

        for major in majors:
            for subject in subjects:
                self.add_association_major_subject(major.id, subject.id)


