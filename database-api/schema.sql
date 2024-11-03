-- This is a file example of request inside our API application
-- This file is used to create the database schema and populate it with some data

CREATE SCHEMA IF NOT EXISTS school;
-- USE School schema
SHOW search_path;
SET search_path TO school;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    school_email VARCHAR(255) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id VARCHAR(255) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    school_email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    speciality VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS courses (
    course_id VARCHAR(255) PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    teacher_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE IF NOT EXISTS enrollments (
    student_id INT NOT NULL,
    course_id VARCHAR(255) NOT NULL,
    grade DECIMAL(3, 2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)
);

INSERT INTO students (student_id, first_name, last_name, school_email, phone)
VALUES (20210615, 'Lucas', 'KOCOGLU', 'lucas.kocoglu@efrei.net', '0767899931');
INSERT INTO students (student_id, first_name, last_name, school_email, phone)
VALUES (20210527, 'Maxime', 'BOULLE', 'maxime.boulle@efrei.net', null);
INSERT INTO students (student_id, first_name, last_name, school_email, phone)
VALUES (20210619, 'Nicolas', 'LAHIMASY', 'nicolas.lahimasy@efrei.net', null);

INSERT INTO teachers (teacher_id, first_name, last_name, school_email, phone, speciality)
VALUES ('ijenhani', 'Ilyes', 'JENHANI', 'ilyes.jenhani@efrei.fr', null, 'Software Engineering Responsible');
INSERT INTO teachers (teacher_id, first_name, last_name, school_email, phone, speciality)
VALUES ('yaitelmahjoub', 'Youssef', 'AIT EL MAHJOUB', 'youssef.ait-el-mahjoub@efrei.fr', '0616591379', 'IT Paris & LSI BDX. Responsible, Researcher-Teacher');

INSERT INTO courses (course_id, course_name, teacher_id)
VALUES ('ST2SAS', 'Docker Containers', 'ijenhani');
INSERT INTO courses (course_id, course_name, teacher_id)
VALUES ('ST2AIM', 'AI & Machine Learning for IT Engineer', 'yaitelmahjoub');

INSERT INTO enrollments (student_id, course_id, grade)
VALUES (20210615, 'ST2SAS', null);
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (20210527, 'ST2SAS', null);
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (20210619, 'ST2SAS', null);
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (20210615, 'ST2AIM', null);
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (20210527, 'ST2AIM', null);
INSERT INTO enrollments (student_id, course_id, grade)
VALUES (20210619, 'ST2AIM', null);
