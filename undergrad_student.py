#! /usr/bin/env python3
from sqlalchemy import Column, Integer, String, DateTime
from abstract_student import AbstractStudent

class UndergraduateStudent(AbstractStudent):
    """This is a class for Undergraduate Student"""
    TYPE = 'Undergraduate'

    minor = Column(String(300))
    min_credit = Column(Integer)

    def __init__(self, first_name, last_name, program, classification, enroll_status, enroll_date, type, minor, min_credit_graduation):
        """Constructor - Initializes variables for undergraduate student"""
        super().__init__(first_name, last_name, program, classification, enroll_status, enroll_date, type)

        self.type = UndergraduateStudent.TYPE

        AbstractStudent._validate_parameter("Minor program", minor,300)
        self.minor = minor

        AbstractStudent._validate_parameter("Min credits to graduate", str(min_credit_graduation),3)
        AbstractStudent._validate_int("Min credits to graduate", min_credit_graduation)
        self.min_credit = min_credit_graduation

    def to_dict(self):
        ''' returns dictionary of undergraduate students details '''

        dict = super().to_dict()
        dict['type'] = self.type
        dict['minor'] = self.minor
        dict['minimum_credit'] = self.min_credit

        return dict

    def get_details(self):
        """Return the details of undergraduate student"""
        detail = 'Name: {} \nProgram: {} \nMinor: {} \nClassification: {} \nEnroll status: {}\nEnroll period: {} years'.format(self.first_name + self.last_name,
                                                                                            self.program,
                                                                                            self.minor,
                                                                                            self.classification,
                                                                                            self.enroll_status,
                                                                                            self.get_enroll_length_in_years())
        return detail

    def copy(self, object):
        """Copies data from a Student object to this Student object"""
        if isinstance(object, UndergraduateStudent):
            self.first_name=object.first_name
            self.last_name=object.last_name
            self.program = object.program
            self.classification = object.classification
            self.enroll_status = object.enroll_status
            self.enroll_date = object.enroll_date
            self.type = object.type
            self.minor = object.minor
            self.min_credit = object.min_credit