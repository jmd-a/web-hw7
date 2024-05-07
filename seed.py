from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Student, Group, Teacher, Subject, Grade, Base
import random

fake = Faker()

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def create_students(num_students):
    for _ in range(num_students):
        student = Student(name=fake.name())
        session.add(student)


def create_groups(num_groups):
    for i in range(num_groups):
        group = Group(name=f'Group {i + 1}')
        session.add(group)


def create_teachers(num_teachers):
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        session.add(teacher)


def create_subjects(num_subjects):
    teachers = session.query(Teacher).all()
    for _ in range(num_subjects):
        teacher = random.choice(teachers)
        subject = Subject(name=fake.word(), teacher_id=teacher.id)
        session.add(subject)


def create_grades(num_grades):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(num_grades):
        student = random.choice(students)
        subject = random.choice(subjects)
        grade = random.randint(1, 100)
        date = fake.date_between(start_date='-1y', end_date='today')
        grade_entry = Grade(student_id=student.id, subject_id=subject.id, grade=grade, date=date)
        session.add(grade_entry)


if __name__ == '__main__':
    create_students(50)
    create_groups(3)
    create_teachers(5)
    create_subjects(8)
    create_grades(20)

    session.commit()
