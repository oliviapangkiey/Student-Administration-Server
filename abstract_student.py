#! /usr/bin/env python3
from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime

class AbstractStudent(Base):
    """This is an abstract class for student"""

    DAYS_IN_YEAR = 365

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    program = Column(String(300), nullable = False)
    classification = Column(String(20), nullable = False)
    enroll_status = Column(String(10), nullable = False)
    enroll_date = Column(String(50), nullable = False)
    type = Column(String(30), nullable = False)

    def __init__(self, first_name, last_name, program, classification, enroll_status, enroll_date, type):
        """Constructor - Initializes variables for abstract student"""

        AbstractStudent._validate_parameter("First Name", first_name, 250)
        self.first_name = first_name

        AbstractStudent._validate_parameter("Last Name", last_name, 250)
        self.last_name = last_name

        AbstractStudent._validate_parameter("Program", program, 300)
        self.program = program

        AbstractStudent._validate_parameter("Classification", classification, 20)
        self.classification = classification

        AbstractStudent._validate_parameter("Enrollment Status", enroll_status, 10)
        self.enroll_status = enroll_status

        AbstractStudent._validate_parameter("Enrollment Date", enroll_date, 50)
        self.enroll_date = enroll_date

        AbstractStudent._validate_parameter("Type", type, 30)
        self.type = type

    def get_enroll_length_in_years(self):
        """Calculate the length in year from student enrollment date"""
        now = datetime.datetime.today()
        enroll_date = datetime.datetime.strptime(self.enroll_date, "%Y-%m-%d")
        diff = now - enroll_date
        length_in_year = round(diff.days/AbstractStudent.DAYS_IN_YEAR,2)
        return length_in_year

    def to_dict(self):
        """Define the structure that the subclasses must have"""
        dict = {}
        dict['id'] = self.id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['program'] = self.program
        dict['classification'] = self.classification
        dict['enroll_status'] = self.enroll_status
        dict['enroll_date'] = self.enroll_date
        dict['type'] = self.type

        return dict

    def get_details(self):
        """Define the structure that the subclasses must have"""
        raise NotImplementedError("Subclass must implement abstract method.")

    @staticmethod
    def _validate_parameter(display_name, parameter_value, length):
        """ Private helper to validate parameter value and length"""

        if parameter_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if parameter_value == "":
            raise ValueError(display_name + " cannot be empty.")

        if len(parameter_value) > length:
            raise ValueError (display_name + " exceeds maximum length.")

    @staticmethod
    def _validate_int(display_name, input_value):
        """ Private helper to validate the input value is int type"""

        if input_value != int(input_value):
            raise ValueError(display_name + " must be a integer type.")