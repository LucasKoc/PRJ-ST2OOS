# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import school_pb2 as school__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in school_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StudentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddStudent = channel.unary_unary(
                '/school.StudentService/AddStudent',
                request_serializer=school__pb2.AddStudentRequest.SerializeToString,
                response_deserializer=school__pb2.AddStudentResponse.FromString,
                _registered_method=True)
        self.GetStudent = channel.unary_unary(
                '/school.StudentService/GetStudent',
                request_serializer=school__pb2.GetStudentRequest.SerializeToString,
                response_deserializer=school__pb2.GetStudentResponse.FromString,
                _registered_method=True)
        self.GetStudents = channel.unary_unary(
                '/school.StudentService/GetStudents',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=school__pb2.GetStudentsResponse.FromString,
                _registered_method=True)


class StudentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StudentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.AddStudent,
                    request_deserializer=school__pb2.AddStudentRequest.FromString,
                    response_serializer=school__pb2.AddStudentResponse.SerializeToString,
            ),
            'GetStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudent,
                    request_deserializer=school__pb2.GetStudentRequest.FromString,
                    response_serializer=school__pb2.GetStudentResponse.SerializeToString,
            ),
            'GetStudents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudents,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=school__pb2.GetStudentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'school.StudentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('school.StudentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StudentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.StudentService/AddStudent',
            school__pb2.AddStudentRequest.SerializeToString,
            school__pb2.AddStudentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.StudentService/GetStudent',
            school__pb2.GetStudentRequest.SerializeToString,
            school__pb2.GetStudentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.StudentService/GetStudents',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            school__pb2.GetStudentsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TeacherServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTeacher = channel.unary_unary(
                '/school.TeacherService/AddTeacher',
                request_serializer=school__pb2.AddTeacherRequest.SerializeToString,
                response_deserializer=school__pb2.AddTeacherResponse.FromString,
                _registered_method=True)
        self.GetTeacher = channel.unary_unary(
                '/school.TeacherService/GetTeacher',
                request_serializer=school__pb2.GetTeacherRequest.SerializeToString,
                response_deserializer=school__pb2.GetTeacherResponse.FromString,
                _registered_method=True)
        self.GetTeachers = channel.unary_unary(
                '/school.TeacherService/GetTeachers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=school__pb2.GetTeachersResponse.FromString,
                _registered_method=True)


class TeacherServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTeacher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTeacher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTeachers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TeacherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTeacher': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTeacher,
                    request_deserializer=school__pb2.AddTeacherRequest.FromString,
                    response_serializer=school__pb2.AddTeacherResponse.SerializeToString,
            ),
            'GetTeacher': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTeacher,
                    request_deserializer=school__pb2.GetTeacherRequest.FromString,
                    response_serializer=school__pb2.GetTeacherResponse.SerializeToString,
            ),
            'GetTeachers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTeachers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=school__pb2.GetTeachersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'school.TeacherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('school.TeacherService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TeacherService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTeacher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.TeacherService/AddTeacher',
            school__pb2.AddTeacherRequest.SerializeToString,
            school__pb2.AddTeacherResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTeacher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.TeacherService/GetTeacher',
            school__pb2.GetTeacherRequest.SerializeToString,
            school__pb2.GetTeacherResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTeachers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.TeacherService/GetTeachers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            school__pb2.GetTeachersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class CourseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddCourse = channel.unary_unary(
                '/school.CourseService/AddCourse',
                request_serializer=school__pb2.AddCourseRequest.SerializeToString,
                response_deserializer=school__pb2.AddCourseResponse.FromString,
                _registered_method=True)
        self.GetCourse = channel.unary_unary(
                '/school.CourseService/GetCourse',
                request_serializer=school__pb2.GetCourseRequest.SerializeToString,
                response_deserializer=school__pb2.GetCourseResponse.FromString,
                _registered_method=True)
        self.GetCourses = channel.unary_unary(
                '/school.CourseService/GetCourses',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=school__pb2.GetCoursesResponse.FromString,
                _registered_method=True)


class CourseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddCourse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCourse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCourses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CourseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddCourse': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCourse,
                    request_deserializer=school__pb2.AddCourseRequest.FromString,
                    response_serializer=school__pb2.AddCourseResponse.SerializeToString,
            ),
            'GetCourse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCourse,
                    request_deserializer=school__pb2.GetCourseRequest.FromString,
                    response_serializer=school__pb2.GetCourseResponse.SerializeToString,
            ),
            'GetCourses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCourses,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=school__pb2.GetCoursesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'school.CourseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('school.CourseService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CourseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddCourse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.CourseService/AddCourse',
            school__pb2.AddCourseRequest.SerializeToString,
            school__pb2.AddCourseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCourse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.CourseService/GetCourse',
            school__pb2.GetCourseRequest.SerializeToString,
            school__pb2.GetCourseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCourses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.CourseService/GetCourses',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            school__pb2.GetCoursesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class EnrollmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EnrollStudent = channel.unary_unary(
                '/school.EnrollmentService/EnrollStudent',
                request_serializer=school__pb2.EnrollStudentRequest.SerializeToString,
                response_deserializer=school__pb2.EnrollStudentResponse.FromString,
                _registered_method=True)
        self.GetEnrollmentsOfStudent = channel.unary_unary(
                '/school.EnrollmentService/GetEnrollmentsOfStudent',
                request_serializer=school__pb2.GetEnrollmentsOfStudentRequest.SerializeToString,
                response_deserializer=school__pb2.GetEnrollmentsOfStudentResponse.FromString,
                _registered_method=True)
        self.GetEnrollments = channel.unary_unary(
                '/school.EnrollmentService/GetEnrollments',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=school__pb2.GetEnrollmentsResponse.FromString,
                _registered_method=True)


class EnrollmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EnrollStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnrollmentsOfStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnrollments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnrollmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EnrollStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.EnrollStudent,
                    request_deserializer=school__pb2.EnrollStudentRequest.FromString,
                    response_serializer=school__pb2.EnrollStudentResponse.SerializeToString,
            ),
            'GetEnrollmentsOfStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEnrollmentsOfStudent,
                    request_deserializer=school__pb2.GetEnrollmentsOfStudentRequest.FromString,
                    response_serializer=school__pb2.GetEnrollmentsOfStudentResponse.SerializeToString,
            ),
            'GetEnrollments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEnrollments,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=school__pb2.GetEnrollmentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'school.EnrollmentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('school.EnrollmentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EnrollmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EnrollStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.EnrollmentService/EnrollStudent',
            school__pb2.EnrollStudentRequest.SerializeToString,
            school__pb2.EnrollStudentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetEnrollmentsOfStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.EnrollmentService/GetEnrollmentsOfStudent',
            school__pb2.GetEnrollmentsOfStudentRequest.SerializeToString,
            school__pb2.GetEnrollmentsOfStudentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetEnrollments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/school.EnrollmentService/GetEnrollments',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            school__pb2.GetEnrollmentsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
