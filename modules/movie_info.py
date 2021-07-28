import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)

def add_movie(movie_id = None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):

    print("Desde Modulo store")
    print(movie_id, title, genre2, director, release_date, sinopsys)
    print("Exito")

    almacenable = {
        "movie_id": movie_id,
        "title": title,
        "genre2": genre2,
        "director": director,
        "release_date": release_date,
        "sinopsys": sinopsys,
    }
    nombre_de_archivo = f"{title}-{movie_id}.json"
    datos = store_string(
        "movie/movies",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_movies_list(movies=None):
    print("Desde modulo movie_info.py")
    print(movies)
    print("Exito")

def get_movie_details(movie_id=None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):
    print("Desde modulo movie_info.py")
    print(movie_id, title, genre2, director, release_date, sinopsys)
    print("Exito")

def update_movie_details(title = None, genre2 = None, director = None, release_date = None, sinopsys = None):

    #update = True
    print("Desde modulo movie_info.py")
    print(title, genre2, director, release_date, sinopsys)
    print("Exito")

def get_reviews_from_movie(movie_id = None, reviews = None):
    print("Desde modulo movie_info.py")
    print(movie_id, reviews)
    print("Exito")

def add_review(user_id = None, movie_id = None, rate = None, comment = None):
    """
    review = {
        "user_id": user_id,
        "movie_id": movie_id,
        "rate": rate,
        "comment": comment
    }
    reviews.append(review)
    return json.dumps(reviews)
    """
    print("Desde modulo movie_info.py")
    print(user_id,  movie_id, rate , comment)
    print("Exito")

def get_review_from_certain_movie(movie_id = None, review_id = None):
    print("Desde modulo movie_info.py")
    print(movie_id, reviews)
    print("Exito")
