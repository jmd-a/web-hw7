import argparse
from sqlalchemy.orm import sessionmaker
from database import engine, Teacher, Student, Group, Subject, Grade

Session = sessionmaker(bind=engine)
session = Session()


def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' successfully created.")


def list_teachers():
    teachers = session.query(Teacher).all()
    print("Teachers:")
    for teacher in teachers:
        print(f"- {teacher.id}: {teacher.name}")


def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher with ID {teacher_id} successfully updated.")
    else:
        print(f"Teacher with ID {teacher_id} does not exist.")


def remove_teacher(teacher_id):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher with ID {teacher_id} successfully deleted.")
    else:
        print(f"Teacher with ID {teacher_id} does not exist.")


def create_student(name, group_id):
    student = Student(name=name, group_id=group_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' successfully created.")


def list_students():
    students = session.query(Student).all()
    print("Students:")
    for student in students:
        print(f"- {student.id}: {student.name}")


def update_student(student_id, name, group_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = name
        student.group_id = group_id
        session.commit()
        print(f"Student with ID {student_id} successfully updated.")
    else:
        print(f"Student with ID {student_id} does not exist.")


def remove_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student with ID {student_id} successfully deleted.")
    else:
        print(f"Student with ID {student_id} does not exist.")


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"Group '{name}' successfully created.")


def list_groups():
    groups = session.query(Group).all()
    print("Groups:")
    for group in groups:
        print(f"- {group.id}: {group.name}")


def update_group(group_id, name):
    group = session.query(Group).filter_by(id=group_id).first()
    if group:
        group.name = name
        session.commit()
        print(f"Group with ID {group_id} successfully updated.")
    else:
        print(f"Group with ID {group_id} does not exist.")


def remove_group(group_id):
    group = session.query(Group).filter_by(id=group_id).first()
    if group:
        session.delete(group)
        session.commit()
        print(f"Group with ID {group_id} successfully deleted.")
    else:
        print(f"Group with ID {group_id} does not exist.")


def create_subject(name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f"Subject '{name}' successfully created.")


def list_subjects():
    subjects = session.query(Subject).all()
    print("Subjects:")
    for subject in subjects:
        print(f"- {subject.id}: {subject.name}")


def update_subject(subject_id, name, teacher_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        subject.name = name
        subject.teacher_id = teacher_id
        session.commit()
        print(f"Subject with ID {subject_id} successfully updated.")
    else:
        print(f"Subject with ID {subject_id} does not exist.")


def remove_subject(subject_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    if subject:
        session.delete(subject)
        session.commit()
        print(f"Subject with ID {subject_id} successfully deleted.")
    else:
        print(f"Subject with ID {subject_id} does not exist.")


def create_grade(student_id, subject_id, grade):
    grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade)
    session.add(grade)
    session.commit()
    print("Grade successfully created.")


def list_grades():
    grades = session.query(Grade).all()
    print("Grades:")
    for grade in grades:
        print(f"- ID: {grade.id}, Student ID: {grade.student_id}, Subject ID: {grade.subject_id}, Grade: {grade.grade}")


def update_grade(grade_id, student_id, subject_id, grade):
    grade = session.query(Grade).filter_by(id=grade_id).first()
    if grade:
        grade.student_id = student_id
        grade.subject_id = subject_id
        grade.grade = grade
        session.commit()
        print(f"Grade with ID {grade_id} successfully updated.")
    else:
        print(f"Grade with ID {grade_id} does not exist.")


def remove_grade(grade_id):
    grade = session.query(Grade).filter_by(id=grade_id).first()
    if grade:
        session.delete(grade)
        session.commit()
        print(f"Grade with ID {grade_id} successfully deleted.")
    else:
        print(f"Grade with ID {grade_id} does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform CRUD operations on the database.")
    parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"], help="Action to perform")
    parser.add_argument("--model", "-m", choices=["Teacher", "Student", "Group", "Subject", "Grade"],
                        help="Model to operate on")
    parser.add_argument("--id", type=int, help="ID of the record to update or remove")
    parser.add_argument("--name", "-n", help="Name of the record to create or update")
    parser.add_argument("--group_id", type=int, help="Group ID for creating a student")

    args = parser.parse_args()

    if args.action == "create":
        if args.model == "Teacher":
            create_teacher(args.name)
        elif args.model == "Student":
            create_student(args.name, args.group_id)
        elif args.model == "Group":
            create_group(args.name)
        elif args.model == "Subject":
            create_subject(args.name, args.teacher_id)
        elif args.model == "Grade":
            create_grade(args.student_id, args.subject_id, args.grade)

    elif args.action == "list":
        if args.model == "Teacher":
            list_teachers()
        elif args.model == "Student":
            list_students()
        elif args.model == "Group":
            list_groups()
        elif args.model == "Subject":
            list_subjects()
        elif args.model == "Grade":
            list_grades()

    elif args.action == "update":
        if args.model == "Teacher":
            update_teacher(args.id, args.name)
        elif args.model == "Student":
            update_student(args.id, args.name, args.group_id)
        elif args.model == "Group":
            update_group(args.id, args.name)
        elif args.model == "Subject":
            update_subject(args.id, args.name, args.teacher_id)
        elif args.model == "Grade":
            update_grade(args.id, args.student_id, args.subject_id, args.grade)

    elif args.action == "remove":
        if args.model == "Teacher":
            remove_teacher(args.id)
        elif args.model == "Student":
            remove_student(args.id)
        elif args.model == "Group":
            remove_group(args.id)
        elif args.model == "Subject":
            remove_subject(args.id)
        elif args.model == "Grade":
            remove_grade(args.id)
