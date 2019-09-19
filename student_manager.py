#! /usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from undergrad_student import UndergraduateStudent
from grad_student import GraduateStudent
from abstract_student import AbstractStudent


class StudentManager:
    """This is a class to hold instances of AbstractStudent class"""
    LAST_INDEX = -1

    def __init__(self, db_filename):
        """Constructor - Initializes variables for student manager class"""
        # self._students = []
        StudentManager._validate_parameter("JSON file", db_filename)

        engine = create_engine('sqlite:///' + db_filename)

        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)

    def add(self, student):
        """add new student """
        StudentManager._validate_parameter("Student object", student)
        StudentManager._validate_object("Student object", student)

        session = self._db_session()

        session.add(student)

        session.commit()

        student_id = student.id

        session.close()

        return student_id

    def get(self, id):
        """Take in ID and return the corresponding object"""
        StudentManager._validate_parameter("ID", id)
        StudentManager._validate_int("ID", id)

        session = self._db_session()

        existing_student = session.query(GraduateStudent).filter(GraduateStudent.id == id).first()
        if existing_student is None:
            session.close()
            raise ValueError("Student does not exist")

        if not existing_student.supervisor:
            existing_student = session.query(UndergraduateStudent).filter(UndergraduateStudent.id == id).first()

        session.close()

        return existing_student

    def get_all(self):
        """Return all student objects"""
        session = self._db_session()

        existing_students_g = session.query(GraduateStudent).filter(GraduateStudent.type == 'Graduate').all()

        existing_students_ug = session.query(UndergraduateStudent).filter(UndergraduateStudent.type == 'Undergraduate').all()

        session.close()

        return existing_students_g + existing_students_ug

    def get_all_by_type(self, type):
        """Take in a type and return the list of corresponding objects"""
        StudentManager._validate_parameter("Type", type)

        existing_students = []

        session = self._db_session()

        if type == "Graduate":
            existing_students = session.query(GraduateStudent).filter(GraduateStudent.type == type).all()
        elif type == "Undergraduate":
            existing_students = session.query(UndergraduateStudent).filter(UndergraduateStudent.type==type).all()

        session.close()

        return existing_students

    def update(self, student):
        """Updates student obejct """
        StudentManager._validate_parameter("Student object", student)
        StudentManager._validate_object("Student object", student)

        session = self._db_session()

        if isinstance(student, GraduateStudent):
            existing_student = session.query(GraduateStudent).filter(GraduateStudent.id == student.id).first()
        elif isinstance(student, UndergraduateStudent):
            existing_student = session.query(UndergraduateStudent).filter(UndergraduateStudent.id == student.id).first()

        if existing_student is None:
            session.close()
            raise ValueError("Student does not exist")

        existing_student.copy(student)

        session.commit()
        session.close()

    def delete(self, id):
        """Take in ID and remove the corresponding student object"""
        StudentManager._validate_parameter("ID", id)
        StudentManager._validate_int("ID", id)

        session = self._db_session()

        existing_student = session.query(GraduateStudent).filter(GraduateStudent.id == id).first()
        if not existing_student:
            existing_student = session.query(UndergraduateStudent).filter(UndergraduateStudent.id == id).first()

        if existing_student is None:
            session.close()
            raise ValueError("Student does not exist")

        session.delete(existing_student)
        session.commit()

        session.close()

    @staticmethod
    def _validate_parameter(display_name, parameter_value):
        """ Private helper to validate parameter value """

        if parameter_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if parameter_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_object(display_name, parameter_value):
        """ Private helper to validate an object """

        if isinstance(parameter_value, AbstractStudent) is False:
            raise ValueError(display_name + " must be an object.")

    @staticmethod
    def _validate_int(display_name, input_value):
        """ Private helper to validate the input value is int type"""

        if input_value != int(input_value):
            raise ValueError(display_name + " must be an integer type.")
