# PRJ-ST2OOS
Project - ST2OOS - OO Systems Development (I2 - 2425S7) - 2024/2025

### Context

This project is a Project for the course "PRJ - OO Systems Development (ST2OOS)". The goal is to create a REST API and a gRPC server to manage school class information.

Language/tools used is **Python** with **FastAPI**, **gRPC** and **PostgreSQL**.
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
# Database Configuration
POSTGRES_CONTAINER_NAME=prjst2oos-database
POSTGRES_USER=8827772055324206084786940047496
POSTGRES_PASSWORD=HgUPqVinEzpMCWkLQMKKwUU4rU5HDYR
POSTGRES_DB=prjst2oos
POSTGRES_SCHEMA=school
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# API Configuration
API_CONTAINER_NAME=prjst2oos-api
API_PORT=3000
API_HOST=0.0.0.0

# Frontend Configuration
FRONTEND_CONTAINER_NAME=prjst2oos-frontend

# Network Configuration
NETWORK_NAME=prjst2oos-network
```

