from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.core.settings import Settings
from api.routes.students_route import router as students_router
from api.routes.teachers_route import router as teachers_router
from api.routes.courses_route import router as courses_router
from api.routes.enrollments_route import router as enrollments_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the car routes
app.include_router(students_router, prefix="/students", tags=["students"])
app.include_router(teachers_router, prefix="/teachers", tags=["teachers"])
app.include_router(courses_router, prefix="/courses", tags=["courses"])
app.include_router(enrollments_router, prefix="/enrollments", tags=["enrollments"])

@app.get("/")
def read_root():
    return {"message": "Routes available at /docs"}

if __name__ == "__main__":
    uvicorn.run("api.main:app", host=Settings.API_HOST, port=int(Settings.API_PORT), reload=True, log_level="info")