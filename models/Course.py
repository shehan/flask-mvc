from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from database import Base


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    students = relationship("Student", secondary="studentcourse", viewonly=True)
    instructor = relationship("Instructor", secondary="instructorcourse", viewonly=True)


class StudentCourse(Base):
    __tablename__ = "studentcourse"
    id = Column(Integer, primary_key=True, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    grade = Column(Float)


class InstructorCourse(Base):
    __tablename__ = "instructorcourse"
    id = Column(Integer, primary_key=True, nullable=False)
    instructor_id = Column(Integer, ForeignKey('instructor.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    rating = Column(Float)
