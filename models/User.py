from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from werkzeug.security import generate_password_hash, check_password_hash

from database import Base


class User(Base, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    date_of_birth = Column(Date)
    password_hash = Column(String)
    student = relationship("Student", uselist=False, backref="student")
    instructor = relationship("Instructor", uselist=False, backref="instructor")

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def password(self):
        raise AttributeError('Password is not readable!')

    @property
    def is_instructor(self):
        return self.instructor is not None

    @property
    def is_student(self):
        return self.student is not None

    @property
    def roles(self):
        roles = []
        if self.is_student:
            roles.append('Student')
        if self.is_instructor:
            roles.append('Instructor')

        return roles

    @property
    def enrolled_courses(self):
        if self.student is None:
            return []
        else:
            return self.student.get_grades()

    @property
    def instructed_courses(self):
        if self.instructor is None:
            return []
        else:
            return self.instructor.get_ratings()

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def exists(session, email):
        return session.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user(session, user_id):
        return session.query(User).filter(User.id == int(user_id)).first()
