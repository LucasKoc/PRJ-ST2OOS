
const user = process.env.GRPC_MONGODB_USER || "7633127447147808253600436660721";
const password = process.env.GRPC_MONGODB_PASSWORD || "X6KY6vz5pEUH6bQSt0y7oalVxRwTd7E";
const database = process.env.GRPC_MONGODB_DATABASE || "prjst2oos";

const database_host = process.env.GRPC_MONGODB_HOST || "localhost";
const database_port = process.env.GRPC_MONGODB_PORT || "27017";

const root_user = process.env.MONGO_INITDB_ROOT_USERNAME || "0131842115714468018860424420915";
const root_password = process.env.MONGO_INITDB_ROOT_PASSWORD || "BphXT3oFmsTp51lE8cWJL2pJjxsOlEi";

// const db = connect("mongodb://" + user + ":" + password + "@" + database_host + ":" + database_port + "/" + database + "?authSource=admin");
let db = connect("mongodb://" + root_user + ":" + root_password + "@" + database_host + ":" + database_port + "/admin");
db = db.getSiblingDB(database);

db.createUser({
    user: user,
    pwd: password,
    roles: [
        { role: "readWrite", db: database }
    ]
});

db.createCollection("students");
db.students.insertMany([
    {
        student_id: 20210615,
        first_name: "Lucas",
        last_name: "KOCOGLU",
        school_email: "lucas.kocoglu@efrei.net",
        phone: "0767899931"
    },
    {
        student_id: 20210527,
        first_name: "Maxime",
        last_name: "BOULLE",
        school_email: "maxime.boulle@efrei.net",
        phone: null
    },
    {
        student_id: 20210619,
        first_name: "Nicolas",
        last_name: "LAHIMASY",
        school_email: "nicolas.lahimasy@efrei.net",
        phone: null
    }
]);

db.createCollection("teachers");
db.teachers.insertMany([
    {
        teacher_id: "ijenhani",
        first_name: "Ilyes",
        last_name: "JENHANI",
        school_email: "ilyes.jenhani@efrei.fr",
        phone: null,
        speciality: "Software Engineering Responsible"
    },
    {
        teacher_id: "yaitelmahjoub",
        first_name: "Youssef",
        last_name: "AIT EL MAHJOUB",
        school_email: "youssef.ait-el-mahjoub@efrei.fr",
        phone: "0616591379",
        speciality: "IT Paris & LSI BDX. Responsible, Researcher-Teacher"
    }
]);

db.createCollection("courses");
db.courses.insertMany([
    {
        course_id: "ST2SAS",
        course_name: "Docker Containers",
        teacher_id: "ijenhani"
    },
    {
        course_id: "ST2AIM",
        course_name: "AI & Machine Learning for IT Engineer",
        teacher_id: "yaitelmahjoub"
    }
]);

db.createCollection("enrollments");
db.enrollments.insertMany([
    { student_id: 20210615, course_id: "ST2SAS", grade: null },
    { student_id: 20210527, course_id: "ST2SAS", grade: null },
    { student_id: 20210619, course_id: "ST2SAS", grade: null },
    { student_id: 20210615, course_id: "ST2AIM", grade: null },
    { student_id: 20210527, course_id: "ST2AIM", grade: null },
    { student_id: 20210619, course_id: "ST2AIM", grade: null }
]);
