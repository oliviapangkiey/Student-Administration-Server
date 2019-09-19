#! /usr/bin/env python3
from sqlalchemy import Column, Integer, String, DateTime
from abstract_student import AbstractStudent

class GraduateStudent(AbstractStudent):
    """This is a class for Graduate Student"""
    TYPE = 'Graduate'

    supervisor = Column(String(250))
    undergrad_degree = Column(String(300))

    def __init__(self, first_name, last_name, program, classification, enroll_status, enroll_date, type, supervisor, undergrad_degree):
        """Constructor - Initializes variables for graduate student"""
        super().__init__(first_name, last_name, program, classification, enroll_status, enroll_date, type)

        self.type = GraduateStudent.TYPE

        AbstractStudent._validate_parameter("Supervisor", supervisor, 250)
        self.supervisor = supervisor

        AbstractStudent._validate_parameter("Undergraduate degree", undergrad_degree, 300)
        self.undergrad_degree = undergrad_degree

    def to_dict(self):
        ''' returns dictionary of graduate students details '''
        dict = super().to_dict()
        dict['supervisor'] = self.supervisor
        dict['undergraduate_degree'] = self.undergrad_degree
        dict['type']=self.type

        return dict


    def get_details(self):
        """Return the details of graduate student"""
        detail = 'Name: {} \nProgram: {} \nClassification: {} \nSupervisor: {}\nEnroll status: {}\nEnroll period: {} years'.format(self.first_name + self.last_name,
                                                                                            self.program(),
                                                                                            self.classification(),
                                                                                            self.supervisor(),
                                                                                            self.enroll_status(),
                                                                                            self.get_enroll_length_in_years())
        return detail


    def copy(self, object):
        """Copies data from a Student object to this Student object"""
        if isinstance(object, GraduateStudent):
            self.first_name=object.first_name
            self.last_name=object.last_name
            self.program = object.program
            self.classification = object.classification
            self.enroll_status = object.enroll_status
            self.enroll_date = object.enroll_date
            self.type = object.type
            self.supervisor = object.supervisor
            self.undergrad_degree = object.undergrad_degree
