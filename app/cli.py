from database import *

# Movie CRUD Operations
def create_movie(title, release_year, rating, description, genre_name, director_name):
    db = SessionLocal()

    # Ensure genre exists
    genre = db.query(Genre).filter(Genre.name == genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        db.add(genre)
        db.commit()
        db.refresh(genre)

    # Ensure director exists
    director = db.query(Director).filter(Director.name == director_name).first()
    if not director:
        director = Director(name=director_name)
        db.add(director)
        db.commit()
        db.refresh(director)

    # Add movie
    movie = Movie(
        title=title,
        release_year=release_year,
        rating=rating,
        description=description,
        genre_id=genre.id,
        director_id=director.id,
    )
    db.add(movie)
    db.commit()
    print(f"Movie '{title}' added successfully!")
    db.close()

def view_movies():
    db = SessionLocal()
    movies = db.query(Movie).all()
    if movies:
        for movie in movies:
            print(f"ID: {movie.id} - Title: {movie.title}")
            print(f"Year: {movie.release_year}")
            print(f"Rating: {movie.rating}/10")
            print(f"Description: {movie.description}")
            print("-" * 40)  # Separator for readability
    else:
        print("No movies available.")
    db.close()

def delete_movie(movie_id):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
        print(f"Deleted movie with ID {movie_id}.")
    else:
        print(f"No movie found with ID {movie_id}.")
    db.close()

def update_movie(movie_id, new_title=None, new_release_year=None, new_rating=None, new_description=None):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        if new_title:
            movie.title = new_title
        if new_release_year:
            movie.release_year = new_release_year
        if new_rating:
            movie.rating = new_rating
        if new_description:
            movie.description = new_description
        db.commit()
        print(f"Movie with ID {movie_id} updated successfully!")
    else:
        print(f"No movie found with ID {movie_id}.")
    db.close()

# Genre CRUD Operations
def create_genre(name):
    db = SessionLocal()
    genre = Genre(name=name)
    db.add(genre)
    db.commit()
    print(f"Genre '{name}' created successfully!")
    db.close()

def view_genres():
    db = SessionLocal()
    genres = db.query(Genre).all()
    if genres:
        for genre in genres:
            print(f"Genre ID: {genre.id} - Name: {genre.name}")
            print("-" * 40)  # Separator for readability
    else:
        print("No genres available.")
    db.close()

def delete_genre(genre_id):
    db = SessionLocal()
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre:
        db.delete(genre)
        db.commit()
        print(f"Deleted genre with ID {genre_id}.")
    else:
        print(f"No genre found with ID {genre_id}.")
    db.close()

def update_genre(genre_id, new_name):
    db = SessionLocal()
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre:
        genre.name = new_name
        db.commit()
        print(f"Genre with ID {genre_id} updated successfully!")
    else:
        print(f"No genre found with ID {genre_id}.")
    db.close()

# Director CRUD Operations
def create_director(name):
    db = SessionLocal()
    director = Director(name=name)
    db.add(director)
    db.commit()
    print(f"Director '{name}' created successfully!")
    db.close()

def view_directors():
    db = SessionLocal()
    directors = db.query(Director).all()
    if directors:
        for director in directors:
            print(f"Director ID: {director.id} - Name: {director.name}")
            print("-" * 40)  # Separator for readability
    else:
        print("No directors available.")
    db.close()

def delete_director(director_id):
    db = SessionLocal()
    director = db.query(Director).filter(Director.id == director_id).first()
    if director:
        db.delete(director)
        db.commit()
        print(f"Deleted director with ID {director_id}.")
    else:
        print(f"No director found with ID {director_id}.")
    db.close()

def update_director(director_id, new_name):
    db = SessionLocal()
    director = db.query(Director).filter(Director.id == director_id).first()
    if director:
        director.name = new_name
        db.commit()
        print(f"Director with ID {director_id} updated successfully!")
    else:
        print(f"No director found with ID {director_id}.")
    db.close()

# Search Movies
def search_movies(search_term):
    db = SessionLocal()
    movies = db.query(Movie).filter(Movie.title.ilike(f"%{search_term}%")).all()
    if movies:
        for movie in movies:
            print(f"Title: {movie.title}")
            print(f"Year: {movie.release_year}")
            print(f"Rating: {movie.rating}/10")
            print(f"Description: {movie.description}")
            print("-" * 40)  # Separator for readability
    else:
        print(f"No movies found with title containing '{search_term}'.")
    db.close()

# CLI Menu
if __name__ == "__main__":
    while True:
        print("\n1. Add Movie")
        print("2. View Movies")
        print("3. Delete Movie")
        print("4. Update Movie")
        print("5. Add Genre")
        print("6. View Genres")
        print("7. Delete Genre")
        print("8. Update Genre")
        print("9. Add Director")
        print("10. View Directors")
        print("11. Delete Director")
        print("12. Update Director")
        print("13. Search Movies")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Movie Title: ")
            release_year = int(input("Release Year: "))
            rating = float(input("Rating (out of 10): "))
            description = input("Movie Description: ")
            genre_name = input("Genre: ")
            director_name = input("Director: ")
            create_movie(title, release_year, rating, description, genre_name, director_name)
        elif choice == "2":
            view_movies()
        elif choice == "3":
            movie_id = int(input("Movie ID to delete: "))
            delete_movie(movie_id)
        elif choice == "4":
            movie_id = int(input("Movie ID to update: "))
            new_title = input("New Title (press Enter to skip): ")
            new_release_year = input("New Release Year (press Enter to skip): ")
            new_rating = input("New Rating (press Enter to skip): ")
            new_description = input("New Description (press Enter to skip): ")

            new_release_year = int(new_release_year) if new_release_year else None
            new_rating = float(new_rating) if new_rating else None

            update_movie(movie_id, new_title, new_release_year, new_rating, new_description)
        elif choice == "5":
            genre_name = input("Genre Name: ")
            create_genre(genre_name)
        elif choice == "6":
            view_genres()
        elif choice == "7":
            genre_id = int(input("Genre ID to delete: "))
            delete_genre(genre_id)
        elif choice == "8":
            genre_id = int(input("Genre ID to update: "))
            new_name = input("New Name: ")
            update_genre(genre_id, new_name)
        elif choice == "9":
            director_name = input("Director Name: ")
            create_director(director_name)
        elif choice == "10":
            view_directors()
        elif choice == "11":
            director_id = int(input("Director ID to delete: "))
            delete_director(director_id)
        elif choice == "12":
            director_id = int(input("Director ID to update: "))
            new_name = input("New name: ")
            update_director(director_id, new_name)
        elif choice == "13":
            search_term = input("Enter movie title to search: ")
            search_movies(search_term)
        elif choice == "14":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
