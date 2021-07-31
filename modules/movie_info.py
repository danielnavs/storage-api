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
    nombre_de_archivo = f"{movie_id}-{title}.json"
    datos = store_string(
        "movie/movies",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_movies_list(movies=None):
    query_result = query_storage(
        "movie/movies",
    )
    if movies is None:
        return query_result["content"]

def get_movie_details(movie_id=None):
    query_result = query_storage(
        "movie/movies",
    )
    if movie_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Almost done perro")

def update_movie_details(title = None, genre2 = None, director = None, release_date = None, sinopsys = None):

    #update = True
    print("Desde modulo movie_info.py")
    print(title, genre2, director, release_date, sinopsys)
    print("Exito")

def add_review(review_id = None, user_id = None, movie_id = None, movie_title = None, rate = None, comment = None):

    print("Desde Modulo add_review")
    print(review_id, user_id, movie_id, movie_title, rate, comment)
    print("Exito")

    almacenable = {
        "review_id": review_id,
        "user_id": user_id,
        "movie_id": movie_id,
        "movie_title": movie_title,
        "rate": rate,
        "comment": comment,
    }
    nombre_de_archivo = f"{movie_id}-{review_id}-{movie_title}.json"
    datos = store_string(
        "movie/reviews",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_reviews_from_movie(movie_id = None, reviews = None):
    query_result = query_storage(
        "movie/reviews",
    )
    if movie_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Done compita")


def get_review_from_certain_movie(movie_id = None, review_id = None):
    query_result = query_storage(
        "movie/reviews",
    )
    if movie_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Done compita")
