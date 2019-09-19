import unittest
from grad_student import GraduateStudent
from undergrad_student import UndergraduateStudent
from student_manager import StudentManager
import inspect
import os

from sqlalchemy import create_engine
from base import Base


class TestStudentManager(unittest.TestCase):
    """ Tests StudentManager Class """

    def setUp(self):
        engine = create_engine('sqlite:///test_students.sqlite')

        # Creates all the tables
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.students_mgr = StudentManager('test_students.sqlite')
        self.test_grad = GraduateStudent("Johnny", "Smith", "CIT", "Domestic", "Enrolled", "2017-11-20","Graduate", "Joe Smith","CIT")
        self.test_undergrad = UndergraduateStudent("Amy", "Johnson", "CIT", "Intl", "Enrolled", "2017-2-13","Undergraduate","Business Administration", 64)

        self.logPoint()

    def test_parameter_valid(self):
        """Test the validity of parameters"""
        self.assertIsNotNone(self.students_mgr)

    def test_parameter_invalid(self):
        """Test invalid parameters: empty and undefined"""
        self.assertRaisesRegex(ValueError, "JSON file cannot be undefined.", StudentManager, None)
        self.assertRaisesRegex(ValueError, "JSON file cannot be empty.", StudentManager, "")

    def test_valid_constructor(self):
        """Test valid constructor for StudentManager"""
        self.assertEqual(len(self.students_mgr.get_all()), 0, "The list of student objects must be empty.")

    def test_add_student(self):
        """Valid add student object"""
        self.students_mgr.add(self.test_grad)
        self.assertEqual(self.students_mgr.get(1).first_name, "Johnny", "The student first name should be Johnny")

        self.students_mgr.add(self.test_undergrad)
        self.assertEqual(self.students_mgr.get(2).first_name, "Amy", "The first name should be Amy.")

    def test_add_student_invalid(self):
        """Test invalid parameters: empty and undefined"""
        self.assertRaisesRegex(ValueError, "Student object cannot be undefined.", self.students_mgr.add, None)
        self.assertRaisesRegex(ValueError, "Student object must be an object.", self.students_mgr.add, [])


    def test_get(self):
        """Test validity of get_id"""
        self.students_mgr.add(self.test_grad)
        self.students_mgr.add(self.test_undergrad)

        self.assertEqual(self.students_mgr.get(1).id, 1,
                         "Student ID must be 1")
        self.assertEqual(self.students_mgr.get(2).id, 2,
                         "Student ID must be 2")

    def test_get_invalid(self):
        """Test invalid parameters: empty, undefined, student not exist"""
        self.assertRaisesRegex(ValueError, "ID cannot be undefined.", self.students_mgr.get, None)
        self.assertRaisesRegex(ValueError, "ID must be an integer type.", self.students_mgr.get, "1")
        self.assertRaisesRegex(ValueError, "Student does not exist", self.students_mgr.get, 10)

    def test_get_all_by_type(self):
        """Test validity of get all by type"""
        self.students_mgr.add(self.test_grad)
        self.assertEqual(len(self.students_mgr.get_all_by_type('Graduate')), 1)
        self.assertEqual(len(self.students_mgr.get_all_by_type('Undergraduate')), 0)

    def test_get_all_by_type_invalid(self):
        """Test invalid parameters: empty"""
        self.assertRaisesRegex(ValueError, "Type cannot be undefined.", self.students_mgr.get_all_by_type, None)


    def test_get_all(self):
        """Test validity of get_all"""
        all_students = self.students_mgr.get_all()
        self.assertEqual(len(all_students), 0)

        self.students_mgr.add(self.test_grad)
        self.students_mgr.add(self.test_undergrad)

        all_students = self.students_mgr.get_all()
        self.assertEqual(len(all_students), 2)

    def test_update(self):
        """Test validity of update"""
        student1_id = self.students_mgr.add(self.test_grad)

        retrieved_student = self.students_mgr.get(student1_id)
        self.assertEqual(retrieved_student.first_name, "Johnny")

        retrieved_student.first_name = "Alex"
        self.students_mgr.update(retrieved_student)

        retrieved_updated_student = self.students_mgr.get(student1_id)
        self.assertEqual(retrieved_updated_student.first_name, "Alex")

        retrieved_student.first_name = "Alex"

    def test_update_invalid(self):
        """Test invalid parameters: empty, undefined, student not exist"""
        test_invalid = GraduateStudent("Alexa", "Croft", "CIT", "Domestic", "Enrolled", "2017-11-20","Graduate", "Joe Smith","CIT")
        self.assertRaisesRegex(ValueError, "Student object cannot be undefined.", self.students_mgr.update, None)
        self.assertRaisesRegex(ValueError, "Student object must be an object.", self.students_mgr.update, [])
        self.assertRaisesRegex(ValueError, "Student does not exist", self.students_mgr.update, test_invalid)

    def test_delete_student(self):
        """Test the validity of delete"""
        self.students_mgr.add(self.test_grad)
        self.assertTrue(len(self.students_mgr.get_all()) == 1)

        self.students_mgr.delete(1)
        self.assertTrue(len(self.students_mgr.get_all()) == 0)

    def test_delete_student_invalid(self):
        """Test invalid parameters: empty, undefined, student not exist"""
        self.assertRaisesRegex(ValueError, "ID cannot be undefined.", self.students_mgr.delete, None)
        self.assertRaisesRegex(ValueError, "ID must be an integer type.", self.students_mgr.delete, "1")
        self.assertRaisesRegex(ValueError, "Student does not exist", self.students_mgr.delete, 10)


    def tearDown(self):
        os.remove('test_students.sqlite')
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

if __name__=="__main__":
    unittest.main()
