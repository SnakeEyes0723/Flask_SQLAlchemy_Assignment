from src.models import Movie, db

class MovieRepository:

    def get_all_movies(self):
        movie: list[Movie]=Movie.query.all()
        return movie

    def get_movie_by_id(self, movie_id):
        movie: Movie = Movie.query.first()
        return movie

    def create_movie(self, title, director, rating):
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        movie: list[Movie] = Movie.query.filter(Movie.title.ilike(f'%{title}')).all()
        return movie


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
