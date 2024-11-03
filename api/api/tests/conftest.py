import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from api.main import app
from api.database.database import Base, get_db
from api.core.settings import Settings

# Test database URL + engine
TEST_DATABASE_URL = Settings.DATABASE_FULL_URL + "_test"
engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """
    Override the get_db dependency to use the test database
    """
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()

# Apply the override
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session")
def db_engine():
    """
    Create the database tables and drop them after the tests are done
    Scope="session" means the engine will be created once per test session
    """
    if not database_exists(TEST_DATABASE_URL):
        create_database(TEST_DATABASE_URL)

    # If not schema SETTINGS.POSTGRES_SCHEMA exists, create it
    with engine.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {Settings.POSTGRES_SCHEMA}"))
        conn.commit()

    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield engine

    # Drop the schema SETTINGS.POSTGRES_SCHEMA
    with engine.connect() as conn:
        conn.execute(text(f"DROP SCHEMA IF EXISTS {Settings.POSTGRES_SCHEMA} CASCADE"))
        conn.commit()

@pytest.fixture(scope="function")
def db_session(db_engine):
    """
    Create a new session for each test
    Scope="function" means the session will be created once per test function
    """
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="module")
def client():
    """
    Create a test client for the FastAPI application
    Scope="module" means the client will be created once per test module
    """
    with TestClient(app) as c:
        yield c