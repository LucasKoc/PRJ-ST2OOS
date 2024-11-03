import os

class Settings:
    """
    Settings class to store all the environment variables

    Attributes (All are str):
    - POSTGRES_USER: Postgres username
    - POSTGRES_PASSWORD: Postgres password
    - POSTGRES_DB: Postgres database name
    - POSTGRES_SCHEMA: Postgres schema name
    - POSTGRES_HOST: Postgres host
    - POSTGRES_PORT: Postgres port

    - DATABASE_FULL_URL: Full database URL
    - DATABASE_URL_NO_DB: Database URL without the database name

    - API_HOST: API host
    - API_PORT: API port
    """
    POSTGRES_USER = os.getenv("POSTGRES_USER", "8827772055324206084786940047496")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "HgUPqVinEzpMCWkLQMKKwUU4rU5HDYR")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "prjst2oos")
    POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA", "school")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    DATABASE_FULL_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    DATABASE_URL_NO_DB = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/postgres"

    API_HOST = os.getenv("API_HOST", "localhost")
    API_PORT = os.getenv("API_PORT", "3000")

    print(DATABASE_FULL_URL)
    print(DATABASE_URL_NO_DB)