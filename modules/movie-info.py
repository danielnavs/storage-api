import datetime
import binascii
from functools import wraps
from os import environ, urandom
import hashlib
from bottle import response, request
import jwt
import models.auth as mauth

movies= []
def add_movie(movie_id, title, genre, director, release_date, sinopsys):
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

reviews = []
def add_review(user_id, movie_id, rate, comment):
    review = {
        "user_id": user_id,
        "movie_id": movie_id,
        "rate": rate,
        "comment": comment
    }
    reviews.append(movie)
    return json.dumps(movie)

def get_movies_list()
    return print(movies)

def get_reviews_list()
    return print(movies)
