import grpc
import school_pb2
import school_pb2_grpc
from google.protobuf import empty_pb2

def run():
    channel = grpc.insecure_channel('localhost:50051')
    student_stub = school_pb2_grpc.StudentServiceStub(channel)
    teacher_stub = school_pb2_grpc.TeacherServiceStub(channel)
    enrollment_stub = school_pb2_grpc.EnrollmentServiceStub(channel)
    course_stub = school_pb2_grpc.CourseServiceStub(channel)

    print("Adding a new student...")
    add_student_request = school_pb2.AddStudentRequest(
        student_id=20210000,
        first_name="Anya",
        last_name="Forger",
        school_email="Anya.Forger@efrei.fr",
        phone="0123456789",
    )
    add_student_response = student_stub.AddStudent(add_student_request)
    print("AddStudent Response:")
    print(add_student_response)

    # Test GetStudent
    print("\nGetting student with ID 20210000...")
    get_student_request = school_pb2.GetStudentRequest(student_id=20210000)
    try:
        get_student_response = student_stub.GetStudent(get_student_request)
        print("GetStudent Response:")
        print(get_student_response)
    except grpc.RpcError as e:
        print(f"Error getting student: {e.details()} (Code: {e.code()})")

    # Test GetStudents
    print("\nGetting all students...")
    get_students_response = student_stub.GetStudents(empty_pb2.Empty())
    print("GetStudents Response:")
    for student in get_students_response.students:
        print(student)

    # Test AddTeacher
    print("\nAdding a new teacher...")
    add_teacher_request = school_pb2.AddTeacherRequest(
        teacher_id="lforger",
        first_name="Loid",
        last_name="Forger",
        school_email="loid.forger@efrei.fr",
        phone="0987654321",
        speciality="Psychiatry",
    )
    add_teacher_response = teacher_stub.AddTeacher(add_teacher_request)
    print("AddTeacher Response:")
    print(add_teacher_response)

    # Test GetTeacher
    print("\nGetting teacher with ID 'lforger'...")
    get_teacher_request = school_pb2.GetTeacherRequest(teacher_id="lforger")
    try:
        get_teacher_response = teacher_stub.GetTeacher(get_teacher_request)
        print("GetTeacher Response:")
        print(get_teacher_response)
    except grpc.RpcError as e:
        print(f"Error getting teacher: {e.details()} (Code: {e.code()})")

if __name__ == '__main__':
    run()
