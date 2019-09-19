from student_manager import StudentManager
from undergrad_student import UndergraduateStudent
from grad_student import GraduateStudent
from flask import Flask, request
import json

app = Flask(__name__)

STUDENTS_DB = 'students.sqlite'

student_manager = StudentManager(STUDENTS_DB)

@app.route('/studentmanager/students', methods=['POST'])
def add_student():
    ''' add students '''
    content = request.json
    
    try: 
        if content['type']=='Graduate':
            student = GraduateStudent(content['first_name'],
                                        content['last_name'],
                                        content['program'],
                                        content['classification'],
                                        content['enroll_status'],
                                        content['enroll_date'],
                                        content['type'],
                                        content['supervisor'],
                                        content['undergraduate_degree'])
        elif content['type']=='Undergraduate':
            student = UndergraduateStudent(content['first_name'],
                                        content['last_name'],
                                        content['program'],
                                        content['classification'],
                                        content['enroll_status'],
                                        content['enroll_date'],
                                        content['type'],
                                        content['minor'],
                                        content['minimum_credit'])

        response = app.response_class(
            status=200,
            response=str(student_manager.add(student))

        )

    except ValueError as e:
        response = app.response_class(
            response='Stundet is invalid',
            status=400
        )
    except KeyError as e:
        response = app.response_class(
            response='Stundet is invalid',
            status=400
        )
    return response

@app.route('/studentmanager/students/<entity_id>', methods=['PUT'])
def update_student(entity_id):
    """Update an existing student"""
    content = request.json

    try:
        student_id = int(entity_id)

        if content['type']=='Graduate':
            student = GraduateStudent(content['first_name'],
                                        content['last_name'],
                                        content['program'],
                                        content['classification'],
                                        content['enroll_status'],
                                        content['enroll_date'],
                                        content['type'],
                                        content['supervisor'],
                                        content['undergraduate_degree'])
        elif content['type']=='Undergraduate':
            student = UndergraduateStudent(content['first_name'],
                                        content['last_name'],
                                        content['program'],
                                        content['classification'],
                                        content['enroll_status'],
                                        content['enroll_date'],
                                        content['type'],
                                        content['minor'],
                                        content['minimum_credit'])

        student.id = student_id
        student_manager.update(student)

        response = app.response_class(
            status=200,
        )

    except ValueError as e:
        if str(e) == "Student does not exist.":
            response = app.response_class(
                response='Student does not exist',
                status=404
            )
        else:
            response = app.response_class(
                response='Student is invalid',
                status=400
            )
    except KeyError as e:
        response = app.response_class(
            response='Stundet is invalid',
            status=400
        )
    return response

@app.route('/studentmanager/students/<entity_id>', methods=['DELETE'])
def delete_student(entity_id):
    """Delete existing student"""
    try:
        student_id = int(entity_id)
        student_manager.delete(student_id)
        response = app.response_class(
            status=200,
        )

    except ValueError as e:
        if str(e) == "Student does not exist":
            response = app.response_class(
                response='Student does not exist',
                status=404
            )
        else:
            response = app.response_class(
                response='Student is invalid',
                status=400
            )

    return response

@app.route('/studentmanager/students/<entity_id>', methods=['GET'])
def get_student_by_id(entity_id):
    """Get student by student id"""

    try:
        student_id = int(entity_id)

        student = student_manager.get(student_id)
        # if student object exist, return response

        response = app.response_class(
            status=200,
            response=json.dumps(student.to_dict()),
            mimetype='application/json'
        )

    except ValueError as e:
            response = app.response_class(
                response=str(e),
                status=400
            )
    return response


@app.route('/studentmanager/students/all', methods=['GET'])
def get_all_students():
    """Get the list of all students"""
    students = student_manager.get_all()

    student_list = []

    for student in students:
        student_list.append(student.to_dict())

    response=app.response_class(
        status = 200,
        response = json.dumps(student_list),
        mimetype='application/json'
    )
    return response

@app.route('/studentmanager/students/all/<type>', methods = ['GET'])
def get_all_by_type(type):
    """Get the list of all students by type"""
    students = student_manager.get_all_by_type(type)

    student_list = []

    try:
        for student in students:
            if student.type==type:
                student_list.append(student.to_dict())

        response = app.response_class(
            status=200,
            response=json.dumps(student_list),
            mimetype='application/json'
        )

    except ValueError as e:
        response = app.response_class(
            response='Type is invalid',
            status=400
        )
    return response

if __name__ == '__main__':
    app.run()