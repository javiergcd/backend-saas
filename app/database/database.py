from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = (
    "postgresql+psycopg://postgres:admin@host.docker.internal:5432/backend_saas"
    # "postgresql+psycopg://postgres:admin@localhost:5432/backend_saas"       para correr de manera local
    # "postgresql+psycopg://postgres:admin@host.docker.internal:5432/backend_saas"     para correr de con Docker Compose en Windows
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)