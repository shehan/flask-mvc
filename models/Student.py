from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session

from database import Base
from models.Course import StudentCourse


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, nullable=False)
    major = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    courses = relationship('Course', secondary="studentcourse")

    def get_grades(self):
        enrolled_course_grades = []
        session = Session.object_session(self)
        for course in self.courses:
            student_course = session.query(StudentCourse)\
                .filter(StudentCourse.student_id == self.id)\
                .filter(StudentCourse.course_id == course.id).first()
            enrolled_course_grades.append({"id":course.id, "name":course.name, "grade":student_course.grade})

        return enrolled_course_grades
