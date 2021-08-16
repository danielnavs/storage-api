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

# Function to add a movie.
def add_movie(movie_id = None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):

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
    # File name
    nombre_de_archivo = f"{movie_id}-{title}.json"

    # Returns a dict
    datos = store_string(
        "movie/movies",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

# Function get all movies list.
def get_movies_list():
    # Looks for all movies in dir movie/movies
    query_result = query_storage(
        "movie/movies",
    )
    # Returns a dict
    return query_result["content"]

# Function get a movie's details
def get_movie_details(movie_id=None):
    # Looks for the movie using the given id
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

# Function to update the data of a movie
def update_movie_details(movie_id = None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):

    print("Desde Modulo update_movie_details")
    print(movie_id, title, genre2, director, release_date, sinopsys)
    print("Exito")

    # Data that is going to be replaced. If only 1 valye is going to be replaces, The
    # other values must be stored the same way it was previouslyt stored.
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

# Function add a review to a movie.
def add_review(review_id = None, user_id = None, movie_id = None, movie_title = None, rate = None, comment = None):

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

# Function to get all reviews from a movie.
def get_reviews_from_movie(movie_id = None, reviews = None):
    # Looks for all reviews for that specific movie (using the movie id)
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

# Function to get all reviews from a movie.
def get_review_from_certain_movie(movie_id = None, review_id = None):
    # Looks for a specific review from a specific movie
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

# Function to add an image
def add_new_image(image_name=None, image_file=None):
    # File name
    filename = f"{image_name}.jpg"

    # Stores the image in dir movie/images
    store_bytes(
        "movie/images",
        filename,
        image_file.read()
    )
    return f"movie/pictures/{filename}"
