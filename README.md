# PRJ-ST2OOS
Project - ST2OOS - OO Systems Development (I2 - 2425S7) - 2024/2025

### Context

This project is a Project for the course "PRJ - OO Systems Development (ST2OOS)". The goal is to create a REST API and a gRPC server to manage school class information.

Language/tools used are Python, FastAPI, gRPC, PostgreSQL, MongoDB, Docker, Nginx.
This project use Docker to run the services.

### Objectives

- code at least two services communicating (one using the REST architecture, the
other the RPC architecture)
- Each service must have its own database (more than one type of database is
desirable : SQL, NoSQL…)
- Respect the rules given in the following project (to be adapted according to the
programming language):
  - Layering (No business code in the web layer)
  - Logger (ex in java: Logger logger = LoggerFactory.getLogger(MyService.class);)
  - Exception handling with HttpStatus code and message
  - OpenAPI documentation (Swagger)
  - Testing (unit tests, web tier tests)
- The services must be documented according to the Open API specification
(Swagger). Show screenshots in the Readme page oy your repository.
- Explain your project in the Readme page.
- The Rest service must be accessible via curl (give the list of the requests in the
Readme of your repository), or via a Javascript program (noted as a bonus) (give
screenshots in the Readme page) (separate the services from the Javascript
program on separated servers).

### Installation and configuration

This project is managed by Docker. Make sure you have Docker installed on your machine.
At the root of the project, run this command to start the services:
```bash
docker-compose up --build
```

Please make sur the `.env` file is present and configured in the root of the project.
```dotenv
# Example of .env file for the Project
# Database-API Configuration
POSTGRES_CONTAINER_NAME=prjst2oos-database-api
POSTGRES_USER=8827772055324206084786940047496
POSTGRES_PASSWORD=HgUPqVinEzpMCWkLQMKKwUU4rU5HDYR
POSTGRES_DB=prjst2oos
POSTGRES_SCHEMA=school
POSTGRES_HOST=0.0.0.0
POSTGRES_PORT=5432

# API Configuration
API_CONTAINER_NAME=prjst2oos-api
API_PORT=3000
API_HOST=0.0.0.0

# gRPC Configuration
GRPC_CONTAINER_NAME=prjst2oos-grpc
GRPC_PORT=50051

# gRPC Database Configuration
GRPC_MONGODB_CONTAINER_NAME=prjst2oos-database-grpc
GRPC_MONGODB_USER=7633127447147808253600436660721
GRPC_MONGODB_PASSWORD=X6KY6vz5pEUH6bQSt0y7oalVxRwTd7E
GRPC_MONGODB_DATABASE=prjst2oos
GRPC_MONGODB_HOST=localhost
GRPC_MONGODB_PORT=27017
MONGO_INITDB_ROOT_USERNAME=0131842115714468018860424420915
MONGO_INITDB_ROOT_PASSWORD=BphXT3oFmsTp51lE8cWJL2pJjxsOlEi

# Frontend Configuration
FRONTEND_CONTAINER_NAME=prjst2oos-frontend

# Network Configuration
NETWORK_NAME=prjst2oos-network
```

### Services

- **API Service**: FastAPI REST API
  - Server running using Uvicorn
  - Documentation: [http://localhost:3000/docs](http://localhost:3000/docs)
  - Using unit tests to test the API (go to the `api` folder and run `python -m pytest`)

- **Database Service**: PostgreSQL Database
  - Database: `prjst2oos`
  - Schema: `school`
  - Tables: `students`, `teachers`, `courses`, `enrollments`
  - Using PostgreSQL to store data for the API

- **Frontend Service**: Nginx Server
  - Main page: [http://localhost:80](http://localhost:80)
  - Using JavaScript (build in React) to interact with the API

- **gRPC Service**: gRPC Serve
  - Using unit tests to test the gRPC service (go to the `grpc` folder and run `python -m pytest`)

- **gRPC Database**: MongoDB Database
  - Database: `prjst2oos`
  - Collections: `students`, `teachers`, `courses`, `enrollments`
  - Using MongoDB to store data for the gRPC service

/!\ To run tests, you need to run the services first via docker compose, because it interacts with the database services.<br>
Test can also be launched at the root of the project using the following command:
```bash
pytest
```

To run services, you can use the following commands:
```bash
# Start the services for the first time
docker-compose up --build
# Start service already created
docker-compose start
```

To stop the services, you can use the following commands:
```bash
# Stop the services
docker-compose stop
```

### API Requests

1. Students
2. Teachers
3. Courses
4. Enrollments

Documentation is available at [http://localhost:3000/docs](http://localhost:3000/docs)<br>
You can interact with the API using the Frontend app (client service) at [http://localhost:80](http://localhost:80)<br>
Example (before insertion):<br>
![Frontend](https://raw.githubusercontent.com/LucasKoc/PRJ-ST2OOS/refs/heads/main/ressources/Screenshot%202024-11-03%20at%2018.20.12.png)<br>
Example (after insertion):<br>
![Frontend](https://raw.githubusercontent.com/LucasKoc/PRJ-ST2OOS/refs/heads/main/ressources/Screenshot%202024-11-03%20at%2018.20.55.png)<br>
View the data in the database:<br>
![Frontend](https://raw.githubusercontent.com/LucasKoc/PRJ-ST2OOS/refs/heads/main/ressources/Screenshot%202024-11-03%20at%2018.21.52.png)<br>

### gRPC Requests

1. Students
2. Teachers
3. Courses
4. Enrollments

To interact with the gRPC service, you can use client in `grpc` folder and run the following command:
```bash
python client.py
```

Example:<br>
![gRPC](https://raw.githubusercontent.com/LucasKoc/PRJ-ST2OOS/refs/heads/main/ressources/Screenshot%202024-11-03%20at%2018.31.58.png)<br>
Example after insertion (also contain mockup data on initialization):<br>
![gRPC](https://raw.githubusercontent.com/LucasKoc/PRJ-ST2OOS/refs/heads/main/ressources/Screenshot%202024-11-03%20at%2018.32.34.png)<br>

### Authors

- KOCOGLU Lucas