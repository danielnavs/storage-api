import datetime
import binascii
from functools import wraps
from os import environ, urandom
import hashlib
from bottle import response, request
import jwt
import models.auth as mauth

def add_movie(title = None, genre2 = None, director = None, release_date = None, sinopsys = None):

    """
    Esta funcion recibe los parametros necesarios para agregar
    una pelicula al sistema.

    movie = {
        "movie_id": movie_id,
        "title": title,
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "sinopsys": sinopsys
    }
    movies.append(movie)
    return json.dumps(movie)
    """

    print("Desde modulo movie_info.py")
    print(title, genre2, director, release_date, sinopsys)
    print("Exito")

def get_movies_list(movies=None):
    print("Desde modulo movie_info.py")
    print(movies)
    print("Exito")

def get_movie_details(movie_id=None, title = None, genre2 = None, director = None, release_date = None, sinopsys = None):
    print("Desde modulo movie_info.py")
    print(movie_id, title, genre2, director, release_date, sinopsys)
    print("Exito")

def update_movie_details(title = None, genre2 = None, director = None, release_date = None, sinopsys = None):
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
