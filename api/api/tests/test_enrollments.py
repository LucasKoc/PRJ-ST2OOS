def test_create_enrollment(client, db_session):
    student_data = {
        "student_id": 10476523,
        "first_name": "Anthony",
        "last_name": "Starter",
        "school_email": "Anthony.Starter@efrei.fr",
        "phone": "012345678"
    }
    client.post("/students/", json=student_data)

    teacher_data = {
        "teacher_id": "asabaody",
        "first_name": "Antoine",
        "last_name": "Sabaody",
        "school_email": "antoine.sabaody@efrei.fr",
        "speciality": "SHC (Science Humaine et Communication)"
    }
    client.post("/teachers/", json=teacher_data)

    course_data = {
        "course_id": "FE2CED",
        "course_name": "Communication éditoriale",
        "teacher_id": "asabaody"
    }
    client.post("/courses/", json=course_data)

    enrollment_data = {
        "student_id": 10476523,
        "course_id": "FE2CED",
        "grade": None
    }
    response = client.post("/enrollments/", json=enrollment_data)
    assert response.status_code == 201
    assert response.json() == enrollment_data

def test_get_enrollments(client, db_session):
    response = client.get("/enrollments/")
    assert response.status_code == 200
    enrollments = response.json()
    assert isinstance(enrollments, list)
    assert len(enrollments) > 0

def test_get_student_enrollments(client, db_session):
    student_id = 10476523
    response = client.get(f"/enrollments/{student_id}")
    assert response.status_code == 200
    enrollments = response.json()
    assert isinstance(enrollments, list)
    assert len(enrollments) > 0
    for enrollment in enrollments:
        assert enrollment["student_id"] == student_id

def test_create_enrollment_nonexistent_student(client, db_session):
    course_data = {
        "course_id": "ST2OOS",
        "course_name": "OO System Development",
        "teacher_id": "asabaody"
    }
    client.post("/courses/", json=course_data)

    enrollment_data = {
        "student_id": 10101010101010101,
        "course_id": "ST2OOS",
        "grade": None
    }
    response = client.post("/enrollments/", json=enrollment_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_create_enrollment_nonexistent_course(client, db_session):
    student_data = {
        "student_id": 10476523,
        "first_name": "Anthony",
        "last_name": "Starter",
        "school_email": "Anthony.Starter@efrei.fr",
        "phone": "012345678"
    }
    client.post("/students/", json=student_data)

    enrollment_data = {
        "student_id": 10476523,
        "course_id": "54qdsf3dsqfq1",
        "grade": None
    }
    response = client.post("/enrollments/", json=enrollment_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"

def test_create_existing_enrollment(client, db_session):
    student_data = {
        "student_id": 10476523,
        "first_name": "Anthony",
        "last_name": "Starter",
        "school_email": "Anthony.Starter@efrei.fr",
        "phone": "012345678"
    }
    client.post("/students/", json=student_data)

    teacher_data = {
        "teacher_id": "asabaody",
        "first_name": "Antoine",
        "last_name": "Sabaody",
        "school_email": "antoine.sabaody@efrei.fr",
        "speciality": "SHC (Science Humaine et Communication)"
    }
    client.post("/teachers/", json=teacher_data)

    course_data = {
        "course_id": "FE2CED",
        "course_name": "Communication éditoriale",
        "teacher_id": "asabaody"
    }
    client.post("/courses/", json=course_data)

    enrollment_data = {
        "student_id": 10476523,
        "course_id": "FE2CED",
        "grade": None
    }
    client.post("/enrollments/", json=enrollment_data)
    # Attempt to create the same enrollment again
    response = client.post("/enrollments/", json=enrollment_data)
    assert response.status_code == 400
    assert "Enrollment already exist" in response.json()["detail"]

def test_get_enrollments_nonexistent_student(client):
    response = client.get("/enrollments/05465132134686046")
    assert response.status_code == 404
    assert "Student not found" in response.json()["detail"]


def test_get_student_nonexistent_enrollments(client, db_session):
    student_id = 987654321

    student_data = {
        "student_id": student_id,
        "first_name": "Savage",
        "last_name": "Carter",
        "school_email": "Savage.Carter@efrei.net",
        "phone": "0123456789"
    }
    client.post("/students/", json=student_data)

    # Attempt to get the student's enrollments
    response = client.get(f"/enrollments/{student_id}")
    assert response.status_code == 404
    assert "Student's enrollments not found" in response.json()["detail"]