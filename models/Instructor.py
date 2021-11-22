from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.types import Date

from database import Base
from models.Course import InstructorCourse


class Instructor(Base):
    __tablename__ = "instructor"

    id = Column(Integer, primary_key=True, nullable=False)
    hire_date = Column(Date)
    position = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    courses = relationship('Course', secondary="instructorcourse")

    def get_ratings(self):
        course_ratings = []
        session = Session.object_session(self)
        for course in self.courses:
            instructor_course = session.query(InstructorCourse)\
                .filter(InstructorCourse.instructor_id == self.id)\
                .filter(InstructorCourse.course_id == course.id).first()
            course_ratings.append({"id":course.id, "name":course.name, "rating":instructor_course.rating})

        return course_ratings
