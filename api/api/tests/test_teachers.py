def test_create_teacher(client, db_session):
    teacher_data = {
        "teacher_id": "bcharroux",
        "first_name": "CHARROUX",
        "last_name": "Benoit",
        "school_email": "Benoit.Charroux@efrei.fr",
        "speciality": "OO System Development",
        "phone": "0123456789"
    }
    response = client.post("/teachers/", json=teacher_data)
    assert response.status_code == 201
    assert response.json() == teacher_data

def test_get_teachers(client, db_session):
    response = client.get("/teachers/")
    assert response.status_code == 200
    teachers = response.json()
    assert isinstance(teachers, list)
    assert len(teachers) > 0

def test_get_teacher(client, db_session):
    teacher_id = "bcharroux"
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    teacher = response.json()
    assert teacher["teacher_id"] == teacher_id

def test_create_existing_teacher(client, db_session):
    teacher_data = {
        "teacher_id": "asabaody2",
        "first_name": "Antoine2",
        "last_name": "Sabaody2",
        "school_email": "antoine.sabaody@efrei.fr2",
        "speciality": "SHC (Science Humaine et Communication)2"
    }
    client.post("/teachers/", json=teacher_data)
    # Attempt to create the same teacher again
    response = client.post("/teachers/", json=teacher_data)
    assert response.status_code == 400
    assert "Teacher already registered" in response.json()["detail"]

def test_get_nonexistent_teacher(client):
    response = client.get("/teachers/6q5sd4f3sd21f3sq2d1f3qs21dfsq35d4")
    assert response.status_code == 404
    assert "Teacher not found" in response.json()["detail"]