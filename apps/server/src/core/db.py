from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(settings.snowflake_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """FastAPI dependency that provides a synchronous database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
