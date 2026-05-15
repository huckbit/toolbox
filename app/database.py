# app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# This reads the URL we specified in your docker-compose environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/toolbox")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This helper function handles opening and closing connections automatically
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()