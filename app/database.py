from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Movie, Genre, Director

DATABASE_URL = "sqlite:///./movies.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



