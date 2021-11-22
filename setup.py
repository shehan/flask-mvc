from datetime import date

from sqlalchemy_utils import database_exists, create_database, drop_database

from models import User
from models.Course import InstructorCourse, StudentCourse, Course
from models.Instructor import Instructor
from models.Student import Student


def provision_database(engine):
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

    User.Base.metadata.create_all(bind=engine)
    # Student.Base.metadata.create_all(bind=engine)
    # Instructor.Base.metadata.create_all(bind=engine)
    # Course.Base.metadata.create_all(bind=engine)


def populate_tables(session):
    user_list = [
        User.User(first_name='Alice', last_name='Black', date_of_birth=date.fromisoformat('2000-08-01'), password='hello', email='alice@school.com'),
        User.User(first_name='Peter', last_name='Brown', date_of_birth=date.fromisoformat('1998-07-28'), password='goodbye', email='peter@school.com'),
        User.User(first_name='Fred', last_name='Green', date_of_birth=date.fromisoformat('2001-04-13'), password='cheers', email='fred@school.com'),
        User.User(first_name='Sarah', last_name='Silver', date_of_birth=date.fromisoformat('2000-02-23'), password='smile', email='sarah@school.com'),
        User.User(first_name='Jack', last_name='White', date_of_birth=date.fromisoformat('2000-07-12'), password='fun', email='jack@school.com'),
        User.User(first_name='Charles', last_name='Westley', date_of_birth=date.fromisoformat('1960-02-07'), password='dog', email='charles@prof.com'),
        User.User(first_name='Maryanne', last_name='Ristau', date_of_birth=date.fromisoformat('1980-09-09'), password='cat', email='maryanne@prof.com'),
        User.User(first_name='Michael', last_name='Spitzer', date_of_birth=date.fromisoformat('1954-03-17'), password='fish', email='michael@prof.com'),
        User.User(first_name='Jennifer', last_name='Hummel', date_of_birth=date.fromisoformat('1990-04-12'), password='bird', email='jennifer@prof.com'),
        User.User(first_name='William', last_name='Rhodes', date_of_birth=date.fromisoformat('1985-08-22'),  password='dog', email='william@prof.com')

    ]
    session.bulk_save_objects(user_list, return_defaults=True)

    student_list = [
        Student(user_id=1, major='SE'),
        Student(user_id=2, major='SE'),
        Student(user_id=3, major='CS'),
        Student(user_id=4, major='CS'),
        Student(user_id=5, major='SE')
    ]
    session.bulk_save_objects(student_list, return_defaults=True)

    instructor_list = [
        Instructor(user_id=6, hire_date=date.fromisoformat('1998-02-07'), position='Professor'),
        Instructor(user_id=7, hire_date=date.fromisoformat('2009-09-09'), position='Associate Professor'),
        Instructor(user_id=8,  hire_date=date.fromisoformat('1995-03-17'), position='Professor'),
        Instructor(user_id=9,  hire_date=date.fromisoformat('2020-08-12'), position='Assistant Professor'),
        Instructor(user_id=10,  hire_date=date.fromisoformat('2020-08-12'), position='Assistant Professor')
    ]
    session.bulk_save_objects(instructor_list, return_defaults=True)

    course_list = [
        Course(name='Software Quality'),
        Course(name='Web Engineering'),
        Course(name='Algorithms'),
        Course(name='Intro to Python'),
        Course(name='Advanced Python'),
        Course(name='Intro to Database')
    ]
    session.bulk_save_objects(course_list, return_defaults=True)

    course_instructor_list = [
        InstructorCourse(instructor_id=1, course_id=1, rating=3.0),
        InstructorCourse(instructor_id=2, course_id=2, rating=1.0),
        InstructorCourse(instructor_id=4, course_id=4, rating=2.76)
    ]
    session.bulk_save_objects(course_instructor_list, return_defaults=True)

    student_instructor_list = [
        StudentCourse(student_id=1, course_id=1, grade=40),
        StudentCourse(student_id=1, course_id=2, grade=81),
        StudentCourse(student_id=2, course_id=2, grade=78),
        StudentCourse(student_id=3, course_id=1, grade=94),
        StudentCourse(student_id=4, course_id=1, grade=100),
        StudentCourse(student_id=4, course_id=3, grade=100),
        StudentCourse(student_id=5, course_id=3, grade=0),
    ]
    session.bulk_save_objects(student_instructor_list, return_defaults=True)

    session.commit()
