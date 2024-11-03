def test_create_student(client, db_session):
    student_data = {
        "student_id": 54351313,
        "first_name": "Levine",
        "last_name": "Mark",
        "school_email": "Levine.Mark@efrei.fr",
        "phone": "012345678"
    }
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201
    assert response.json() == student_data

def test_get_students(client, db_session):
    response = client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)
    assert len(students) > 0

def test_get_student(client, db_session):
    student_id = 54351313
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    student = response.json()
    assert student["student_id"] == student_id


def test_create_existing_student(client, db_session):
    student_data = {
        "student_id": 54351313,
        "first_name": "Levine",
        "last_name": "Mark",
        "school_email": "Levine.Mark@efrei.fr",
        "phone": "012345678"
    }
    response = client.post("/students/", json=student_data)
    assert response.status_code == 400
    assert "Student already registered" in response.json()["detail"]

def test_get_nonexistent_student(client):
    response = client.get("/students/999")
    assert response.status_code == 404
    assert "Student not found" in response.json()["detail"]
