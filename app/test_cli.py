import pytest
from app.models import Movie, Genre, Director
from app.database import SessionLocal
from app.cli import create_movie, create_genre, create_director, delete_movie, delete_genre, delete_director

@pytest.fixture(scope="module")
def setup_db():
    yield
    db = SessionLocal()
    db.query(Movie).delete()
    db.query(Genre).delete()
    db.query(Director).delete()
    db.commit()

def test_create_genre(setup_db):
    create_genre("Sci-Fi")
    db = SessionLocal()
    genre = db.query(Genre).filter(Genre.name == "Sci-Fi").first()
    assert genre is not None
    assert genre.name == "Sci-Fi"
    db.close()

def test_create_director(setup_db):
    create_director("Christopher Nolan")
    db = SessionLocal()
    director = db.query(Director).filter(Director.name == "Christopher Nolan").first()
    assert director is not None
    assert director.name == "Christopher Nolan"
    db.close()

def test_create_movie(setup_db):
    create_movie("Inception", 2010, 8.8, "Sci-Fi", "Christopher Nolan")
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.title == "Inception").first()
    assert movie is not None
    assert movie.title == "Inception"
    db.close()

def test_delete_movie(setup_db):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.title == "Inception").first()
    delete_movie(movie.id)
    movie_after_delete = db.query(Movie).filter(Movie.title == "Inception").first()
    assert movie_after_delete is None
    db.close()

def test_delete_genre(setup_db):
    db = SessionLocal()
    genre = db.query(Genre).filter(Genre.name == "Sci-Fi").first()
    delete_genre(genre.id)
    genre_after_delete = db.query(Genre).filter(Genre.name == "Sci-Fi").first()
    assert genre_after_delete is None
    db.close()

def test_delete_director(setup_db):
    db = SessionLocal()
    director = db.query(Director).filter(Director.name == "Christopher Nolan").first()
    delete_director(director.id)
    director_after_delete = db.query(Director).filter(Director.name == "Christopher Nolan").first()
    assert director_after_delete is None
    db.close()
