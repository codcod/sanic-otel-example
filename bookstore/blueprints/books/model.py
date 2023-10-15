import random


class Genre:
    name: str
    _genres = {
        'sci-fi': 40,
        'thriller': 20,
        'horror': 15,
        'fantasy': 10,
        'mystery': 10,
        'dystopian': 5,
    }

    def __init__(self, name: str | None = None):
        self.name = name if name else self.random()

    @classmethod
    def random(cls) -> str:
        genres = cls._genres
        genre = random.choices(tuple(genres.keys()), tuple(genres.values()))
        return genre.pop()

    @classmethod
    def list(cls):
        return cls._genres.keys()

    def __repr__(self) -> str:
        return self.name


class Book:
    genre: Genre

    def __init__(self, genre_name: str | None = None):
        self.genre = Genre(genre_name)
