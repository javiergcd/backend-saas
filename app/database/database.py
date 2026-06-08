from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = (
    "postgresql+psycopg://postgres:admin@localhost:5432/backend_saas"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)