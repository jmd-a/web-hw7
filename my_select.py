from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from database import Student, Grade, Group, Teacher, Subject, engine

Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    query = session.query(Student, func.avg(Grade.grade).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .limit(5)
    return query.all()


def select_2(subject_name):
    query = session.query(Student, func.avg(Grade.grade).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Subject.id == Grade.subject_id) \
        .filter(Subject.name == subject_name) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .first()
    return query


def select_3(subject_name):
    query = session.query(Group.name, func.avg(Grade.grade).label('avg_grade')) \
        .join(Student) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Subject.id == Grade.subject_id) \
        .filter(Subject.name == subject_name) \
        .group_by(Group.name)
    return query.all()


def select_4():
    query = session.query(func.avg(Grade.grade).label('avg_grade')).scalar()
    return query


def select_5(teacher_name):
    query = session.query(Subject.name) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.name == teacher_name)
    return query.all()


def select_6(group_name):
    query = session.query(Student.name) \
        .join(Group, Student.group_id == Group.id) \
        .filter(Group.name == group_name)
    return query.all()


def select_7(group_name, subject_name):
    query = session.query(Student.name, Grade.grade) \
        .join(Group, Student.group_id == Group.id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Subject.id == Grade.subject_id) \
        .filter(Group.name == group_name) \
        .filter(Subject.name == subject_name)
    return query.all()


def select_8(teacher_name):
    query = session.query(func.avg(Grade.grade).label('avg_grade')) \
        .join(Subject, Subject.id == Grade.subject_id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Teacher.name == teacher_name) \
        .scalar()
    return query


def select_9(student_name):
    query = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Student.id == Grade.student_id) \
        .filter(Student.name == student_name)
    return query.all()


def select_10(student_name, teacher_name):
    query = session.query(Subject.name) \
        .join(Grade, Grade.subject_id == Subject.id) \
        .join(Student, Student.id == Grade.student_id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Student.name == student_name) \
        .filter(Teacher.name == teacher_name)
    return query.all()
