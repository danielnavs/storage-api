import json
import datetime as dt
from os import environ
from pathlib import Path
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)


def add_movie(movie_id = None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):
    """
    This is a function to add a movie. It needs to receive all the values in order to work, otherwise, it'll just
    throw an error message...
    Saves the movie in dir movie/movies
    """
    print("Desde Modulo add_movie")
    print(movie_id, title, genre2, director, release_date, sinopsys)
    print("Exito")

    # Data that is going to be stored
    almacenable = {
        "movie_id": movie_id,
        "title": title,
        "genre2": genre2,
        "director": director,
        "release_date": release_date,
        "sinopsys": sinopsys,
    }

    nombre_de_archivo = f"{movie_id}-{title}.json"

    # Returns a dict
    datos = store_string(
        "movie/movies",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_movies_list():
    """
    This is a function to get all movies list. Looks for all movies in dir movie/movies and returns a dict.
    """
    query_result = query_storage(
        "movie/movies",
    )
    # Returns a dict
    return query_result["content"]


def get_movie_details(movie_id=None):
    """
    This is a function to get a movie's details. It looks for the movie in dir movie/movies using the given id.
    """
    query_result = query_storage(
        "movie/movies",
    )
    # Returns a dict containing the movie details.
    if movie_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Done")


def update_movie_details(movie_id = None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):
    """
    This is a function to update the data of a movie. It needs to receive all the values in order to work, otherwise, it'll just
    throw an error message...
    If only 1 value is going to be replaced, the other values must be posted the same way it was previouslyt stored.
    """
    print("Desde Modulo update_movie_details")
    print(movie_id, title, genre2, director, release_date, sinopsys)
    print("Exito")

    # Data that is going to be replaced.
    almacenable = {
        "movie_id": movie_id,
        "title": title,
        "genre2": genre2,
        "director": director,
        "release_date": release_date,
        "sinopsys": sinopsys,
    }
    # File name
    nombre_de_archivo = f"{movie_id}-{title}.json"

    # Returns a dict
    datos = store_string(
        "movie/movies",
        nombre_de_archivo,
        json.dumps(almacenable),
        update=True
    )
    return datos


def add_review(review_id = None, user_id = None, movie_id = None, movie_title = None, rate = None, comment = None):
    """
    This is a function to add a review to a movie. It needs to receive all the values in order to work, otherwise, it'll just
    throw an error message...
    The review is going to be saved in dir movie/reviews.
    """
    print("Desde Modulo add_review")
    print(review_id, user_id, movie_id, movie_title, rate, comment)
    print("Exito")

    # Data that is going to be stored
    almacenable = {
        "review_id": review_id,
        "user_id": user_id,
        "movie_id": movie_id,
        "movie_title": movie_title,
        "rate": rate,
        "comment": comment,
    }

    #File name
    nombre_de_archivo = f"{movie_id}-{review_id}-{movie_title}.json"

    # Returns a dict
    datos = store_string(
        "movie/reviews",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos


def get_reviews_from_movie(movie_id = None, reviews = None):
    """
    This is a function to get all reviews from a movie. It looks for all reviews for that specific movie (using the movie id).
    If it receives a wrong or inexistent id, it'll throw an error message.
    """
    query_result = query_storage(
        "movie/reviews",
    )
    # Returns a dict
    if movie_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Done")


def get_review_from_certain_movie(movie_id = None, review_id = None):
    """
    This is a function to get all reviews from a movie. Looks for a specific review from a specific movie, using both movie and review id's.
    """
    query_result = query_storage(
        "movie/reviews",
    )
    # Returns a dict
    if movie_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Done")


def add_new_image(image_name=None, image_file=None):
    """
    This is a function to add an image.
    Stores the image in dir movie/images
    """
    filename = f"{image_name}.jpg"

    store_bytes(
        "movie/images",
        filename,
        image_file.read()
    )
    return f"movie/pictures/{filename}"
