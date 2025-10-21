from typing import TypedDict


# Define the structure of a movie dictionary
class MovieDetails(TypedDict):
    title: str
    director: str
    release_year: int


def format_movie_info(movie: MovieDetails) -> str:
    # Type checkers like mypy will ensure 'title', 'director', and 'release_year' are present
    # and correctly typed, treating the dict as a structured type.
    return f"{movie['title']} directed by {movie['director']} ({movie['release_year']})"


# This dict conforms to the structure, so it passes type checks
sample_movie: MovieDetails = {
    "title": "Code Odyssey",
    "director": "Tech Guru",
    "release_year": 2023,
}
print(format_movie_info(sample_movie))
# Static analysis would flag issues if you omitted 'release_year' or used the wrong type!
