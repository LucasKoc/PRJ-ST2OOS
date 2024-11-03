def test_create_course(client, db_session):
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
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 201
    assert response.json() == course_data


def test_get_courses(client, db_session):
    response = client.get("/courses/")
    assert response.status_code == 200
    courses = response.json()
    assert isinstance(courses, list)
    assert len(courses) > 0


def test_get_course(client, db_session):
    course_id = "FE2CED"
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    course = response.json()
    assert course["course_id"] == course_id

def test_create_existing_course(client, db_session):
    teacher_data = {
        "teacher_id": "asabaody3",
        "first_name": "Antoine",
        "last_name": "Sabaody",
        "school_email": "antoine.sabaody@efrei.fr",
        "speciality": "SHC (Science Humaine et Communication)"
    }
    client.post("/teachers/", json=teacher_data)

    course_data = {
        "course_id": "FE2CED3",
        "course_name": "Communication éditoriale",
        "teacher_id": "asabaody3"
    }
    client.post("/courses/", json=course_data)
    # Attempt to create the same course again
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 400
    assert "Course already registered" in response.json()["detail"]

def test_get_nonexistent_course(client):
    response = client.get("/courses/NonExistentCourseID")
    assert response.status_code == 404
    assert "Course not found" in response.json()["detail"]