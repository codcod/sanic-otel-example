import random


def random_book() -> dict:
    genres = {
        'fantasy': 10,
        'sci-fi': 40,
        'dystopian': 5,
        'mystery': 10,
        'horror': 15,
        'thriller': 20,
    }
    genre = random.choices(tuple(genres.keys()), tuple(genres.values()))
    return {
        'genre': genre.pop(),
    }
