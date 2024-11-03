import pytest
import grpc
from concurrent import futures

import school_pb2
import school_pb2_grpc
from grpc_server import (
    StudentService,
    TeacherService,
    EnrollmentService,
    CourseService,
    db
)

from google.protobuf import empty_pb2

@pytest.fixture(scope='module')
def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add services to the server
    school_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    school_pb2_grpc.add_TeacherServiceServicer_to_server(TeacherService(), server)
    school_pb2_grpc.add_EnrollmentServiceServicer_to_server(EnrollmentService(), server)
    school_pb2_grpc.add_CourseServiceServicer_to_server(CourseService(), server)

    port = server.add_insecure_port('localhost:0')  # Bind to a free port provided by the OS
    server.start()
    yield server, port
    server.stop(None)

@pytest.fixture(scope='module')
def grpc_channel(grpc_server):
    _, port = grpc_server
    channel = grpc.insecure_channel(f'localhost:{port}')
    yield channel
    channel.close()

@pytest.fixture(autouse=True)
def clear_db():
    # Clear the collections before each test
    db.students.delete_many({})
    db.teachers.delete_many({})
    db.enrollments.delete_many({})
    db.courses.delete_many({})
    yield

# Test functions
def test_add_and_get_student(grpc_channel):
    stub = school_pb2_grpc.StudentServiceStub(grpc_channel)
    add_response = stub.AddStudent(school_pb2.AddStudentRequest(
        student_id=20210001,
        first_name="Martin",
        last_name="Benjamin",
        school_email="Martin.Benjamin@efrei.fr",
        phone="06845345"
    ))
    assert add_response.student_id == 20210001
    assert add_response.first_name == "Martin"
    assert add_response.last_name == "Benjamin"

    get_response = stub.GetStudent(school_pb2.GetStudentRequest(student_id=20210001))
    assert get_response.student_id == 20210001
    assert get_response.first_name == "Martin"
    assert get_response.last_name == "Benjamin"

def test_get_nonexistent_student(grpc_channel):
    stub = school_pb2_grpc.StudentServiceStub(grpc_channel)
    with pytest.raises(grpc.RpcError) as exc_info:
        stub.GetStudent(school_pb2.GetStudentRequest(student_id=3212))
    assert exc_info.value.code() == grpc.StatusCode.NOT_FOUND
    assert exc_info.value.details() == "Student not found"

def test_add_and_get_teacher(grpc_channel):
    stub = school_pb2_grpc.TeacherServiceStub(grpc_channel)
    add_response = stub.AddTeacher(school_pb2.AddTeacherRequest(
        teacher_id="lforger",
        first_name="Loid",
        last_name="Forger",
        school_email="lforger.Forger@westalis.be",
        phone="06541321213",
        speciality="Psychatry"
    ))
    assert add_response.teacher_id == "lforger"
    assert add_response.first_name == "Loid"
    assert add_response.last_name == "Forger"

    get_response = stub.GetTeacher(school_pb2.GetTeacherRequest(teacher_id="lforger"))
    assert get_response.teacher_id == "lforger"
    assert get_response.first_name == "Loid"
    assert get_response.last_name == "Forger"

def test_enroll_student(grpc_channel):
    student_stub = school_pb2_grpc.StudentServiceStub(grpc_channel)
    course_stub = school_pb2_grpc.CourseServiceStub(grpc_channel)
    enrollment_stub = school_pb2_grpc.EnrollmentServiceStub(grpc_channel)

    student_stub.AddStudent(school_pb2.AddStudentRequest(
        student_id=220132054,
        first_name="Anya",
        last_name="Forger",
        school_email="Anya.Forger@westalis.com",
        phone=None
    ))
    course_stub.AddCourse(school_pb2.AddCourseRequest(
        course_id="P001",
        course_name="Introduction to Psychology",
        teacher_id="lforger"
    ))

    # Enroll the student
    enroll_response = enrollment_stub.EnrollStudent(school_pb2.EnrollStudentRequest(
        student_id=220132054,
        course_id="P001",
        grade=1
    ))
    assert enroll_response.student_id == 220132054
    assert enroll_response.course_id == "P001"
    assert enroll_response.grade == 1

    # Get enrollments of the student
    enrollments_response = enrollment_stub.GetEnrollmentsOfStudent(school_pb2.GetEnrollmentsOfStudentRequest(
        student_id=220132054
    ))
    assert len(enrollments_response.enrollments) == 1
    enrollment = enrollments_response.enrollments[0]
    assert enrollment.student_id == 220132054
    assert enrollment.course_id == "P001"
    assert enrollment.grade == 1

def test_get_all_students(grpc_channel):
    stub = school_pb2_grpc.StudentServiceStub(grpc_channel)
    # Add multiple students
    students = [
        school_pb2.AddStudentRequest(
            student_id=i,
            first_name=f"qsdfqsdfqsdfqsdf{i}",
            last_name="qsdfqsdfsqdfsqdfsqdfsqdqs",
            school_email=f"qsdfqsdfqsdfqsdf.qsdfqsdfsqdfsqdfsqdfsqdqs{i}@efrei.fr",
            phone=f"06406513{i}"
        ) for i in range(7, 10)
    ]
    for student in students:
        stub.AddStudent(student)

    # Get all students
    response = stub.GetStudents(empty_pb2.Empty())
    assert len(response.students) == 3
    student_ids = {student.student_id for student in response.students}
    assert student_ids == {7, 8, 9}

def test_get_all_teachers(grpc_channel):
    stub = school_pb2_grpc.TeacherServiceStub(grpc_channel)
    # Add multiple teachers
    teachers = [
        school_pb2.AddTeacherRequest(
            teacher_id=f"4sd3cfsq3d2f1qsdf{i}",
            first_name=f"qsdfqsdfsqdfsqdfsqd{i}",
            last_name="qsdfqsdfqsdfqsfsqdfqs",
            school_email=f"qsdfqsdfsqdfsqdfsqd{i}.qsdfqsdfqsdfqsfsqdfqs@qsdfdsqfdsfsqd.dfqsdffsd",
            phone=f"06505545064{i}",
            speciality="Mastery"
        ) for i in range(2, 5)
    ]
    for teacher in teachers:
        stub.AddTeacher(teacher)

    # Get all teachers
    response = stub.GetTeachers(empty_pb2.Empty())
    assert len(response.teachers) == 3
    teacher_ids = {teacher.teacher_id for teacher in response.teachers}
    assert teacher_ids == {"4sd3cfsq3d2f1qsdf2", "4sd3cfsq3d2f1qsdf3", "4sd3cfsq3d2f1qsdf4"}

def test_get_all_enrollments(grpc_channel):
    enrollment_stub = school_pb2_grpc.EnrollmentServiceStub(grpc_channel)
    # Enroll multiple students in multiple courses
    enrollments = [
        school_pb2.EnrollStudentRequest(student_id=7, course_id="P001", grade=4),
        school_pb2.EnrollStudentRequest(student_id=8, course_id="P001", grade=65),
        school_pb2.EnrollStudentRequest(student_id=9, course_id="P001", grade=42),
    ]
    for enrollment in enrollments:
        enrollment_stub.EnrollStudent(enrollment)

    # Get all enrollments
    response = enrollment_stub.GetEnrollments(empty_pb2.Empty())
    assert len(response.enrollments) == 3
    enrollment_keys = {(e.student_id, e.course_id) for e in response.enrollments}
    expected_keys = {(7, "P001"), (8, "P001"), (9, "P001")}
    assert enrollment_keys == expected_keys
