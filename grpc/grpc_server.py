from concurrent import futures
import grpc
import pymongo
import school_pb2
import school_pb2_grpc
import os

# MongoDB connection details with corrected authSource
mongo_client = pymongo.MongoClient(
    f"mongodb://{os.getenv('GRPC_MONGODB_USER')}:{os.getenv('GRPC_MONGODB_PASSWORD')}@"
    f"{os.getenv('GRPC_MONGODB_HOST')}:{os.getenv('GRPC_MONGODB_PORT')}/"
    f"{os.getenv('GRPC_MONGODB_DATABASE')}?authSource={os.getenv('GRPC_MONGODB_DATABASE')}"
)
db = mongo_client[os.getenv('GRPC_MONGODB_DATABASE')]

print(f"Connected to MongoDB at {os.getenv('GRPC_MONGODB_HOST')}:{os.getenv('GRPC_MONGODB_PORT')}")
"""print(f"Connection URI: mongodb://{os.getenv('GRPC_MONGODB_USER')}:{os.getenv('GRPC_MONGODB_PASSWORD')}@"
      f"{os.getenv('GRPC_MONGODB_HOST')}:{os.getenv('GRPC_MONGODB_PORT')}/"
      f"{os.getenv('GRPC_MONGODB_DATABASE')}?authSource={os.getenv('GRPC_MONGODB_DATABASE')}")"""
print(f"Database: {os.getenv('GRPC_MONGODB_DATABASE')}")

class StudentService(school_pb2_grpc.StudentServiceServicer):
    def AddStudent(self, request, context):
        student = {
            "student_id": request.student_id,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "school_email": request.school_email,
            "phone": request.phone
        }
        db.students.insert_one(student)
        return school_pb2.AddStudentResponse(
            student_id=student["student_id"],
            first_name=student["first_name"],
            last_name=student["last_name"],
            school_email=student["school_email"],
            phone=student["phone"]
        )

    def GetStudent(self, request, context):
        student = db.students.find_one({"student_id": request.student_id})
        if not student:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Student not found")
            return school_pb2.GetStudentResponse()

        return school_pb2.GetStudentResponse(
            student_id=student["student_id"],
            first_name=student["first_name"],
            last_name=student["last_name"],
            school_email=student["school_email"],
            phone=student.get("phone", "")
        )

    def GetStudents(self, request, context):
        students = db.students.find()
        student_list = [
            school_pb2.GetStudentResponse(
                student_id=student["student_id"],
                first_name=student["first_name"],
                last_name=student["last_name"],
                school_email=student["school_email"],
                phone=student.get("phone", "")
            )
            for student in students
        ]
        return school_pb2.GetStudentsResponse(students=student_list)

class TeacherService(school_pb2_grpc.TeacherServiceServicer):
    def AddTeacher(self, request, context):
        teacher = {
            "teacher_id": request.teacher_id,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "school_email": request.school_email,
            "phone": request.phone,
            "speciality": request.speciality
        }
        db.teachers.insert_one(teacher)
        return school_pb2.AddTeacherResponse(
            teacher_id=teacher["teacher_id"],
            first_name=teacher["first_name"],
            last_name=teacher["last_name"],
            school_email=teacher["school_email"],
            phone=teacher["phone"],
            speciality=teacher["speciality"]
        )

    def GetTeacher(self, request, context):
        teacher = db.teachers.find_one({"teacher_id": request.teacher_id})
        if not teacher:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Teacher not found")
            return school_pb2.GetTeacherResponse()

        return school_pb2.GetTeacherResponse(
            teacher_id=teacher["teacher_id"],
            first_name=teacher["first_name"],
            last_name=teacher["last_name"],
            school_email=teacher["school_email"],
            phone=teacher.get("phone", ""),
            speciality=teacher.get("speciality", "")
        )

    def GetTeachers(self, request, context):
        teachers = db.teachers.find()
        teacher_list = [
            school_pb2.GetTeacherResponse(
                teacher_id=teacher["teacher_id"],
                first_name=teacher["first_name"],
                last_name=teacher["last_name"],
                school_email=teacher["school_email"],
                phone=teacher.get("phone", ""),
                speciality=teacher.get("speciality", "")
            )
            for teacher in teachers
        ]
        return school_pb2.GetTeachersResponse(teachers=teacher_list)

class EnrollmentService(school_pb2_grpc.EnrollmentServiceServicer):
    def EnrollStudent(self, request, context):
        enrollment = {
            "student_id": request.student_id,
            "course_id": request.course_id,
            "grade": request.grade if request.grade != 0 else None
        }
        db.enrollments.insert_one(enrollment)
        return school_pb2.EnrollStudentResponse(
            student_id=enrollment["student_id"],
            course_id=enrollment["course_id"],
            grade=enrollment["grade"] if enrollment["grade"] is not None else 0
        )

    def GetEnrollmentsOfStudent(self, request, context):
        enrollments = db.enrollments.find({"student_id": request.student_id})
        enrollment_list = [
            school_pb2.EnrollStudentResponse(
                student_id=enrollment["student_id"],
                course_id=enrollment["course_id"],
                grade=enrollment.get("grade", 0)
            )
            for enrollment in enrollments
        ]
        return school_pb2.GetEnrollmentsOfStudentResponse(enrollments=enrollment_list)

    def GetEnrollments(self, request, context):
        enrollments = db.enrollments.find()
        enrollment_list = [
            school_pb2.EnrollStudentResponse(
                student_id=enrollment["student_id"],
                course_id=enrollment["course_id"],
                grade=enrollment.get("grade", 0)
            )
            for enrollment in enrollments
        ]
        return school_pb2.GetEnrollmentsResponse(enrollments=enrollment_list)

class CourseService(school_pb2_grpc.CourseServiceServicer):
    def AddCourse(self, request, context):
        course = {
            "course_id": request.course_id,
            "course_name": request.course_name,
            "teacher_id": request.teacher_id
        }
        db.courses.insert_one(course)
        return school_pb2.AddCourseResponse(
            course_id=course["course_id"],
            course_name=course["course_name"],
            teacher_id=course["teacher_id"]
        )

    def GetCourse(self, request, context):
        course = db.courses.find_one({"course_id": request.course_id})
        if not course:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Course not found")
            return school_pb2.GetCourseResponse()
        return school_pb2.GetCourseResponse(
            course_id=course["course_id"],
            course_name=course["course_name"],
            teacher_id=course["teacher_id"]
        )

    def GetCourses(self, request, context):
        courses = db.courses.find()
        course_list = [
            school_pb2.GetCourseResponse(
                course_id=course["course_id"],
                course_name=course["course_name"],
                teacher_id=course["teacher_id"]
            )
            for course in courses
        ]
        return school_pb2.GetCoursesResponse(courses=course_list)

# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    school_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    school_pb2_grpc.add_TeacherServiceServicer_to_server(TeacherService(), server)
    school_pb2_grpc.add_EnrollmentServiceServicer_to_server(EnrollmentService(), server)
    school_pb2_grpc.add_CourseServiceServicer_to_server(CourseService(), server)

    print(f"Starting gRPC server. Listening on port {os.getenv('GRPC_PORT', '50051')}...")
    server.add_insecure_port("[::]:" + os.getenv("GRPC_PORT", "50051"))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
