from json import dumps as json_dumps
from os import environ
import bottle
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required

app = bottle.Bottle()

## Add a movie
@app.post("/movie-info/add")
def add_a_movie(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get movies list
@app.get("/movie-info/list")
def get_movies_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get movie details
@app.get("/movie-info/<movie_id>")
def get_movie_details(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Update movie details
@app.post("/movie-info/<movie_id>")
def update_movie_details(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get all reviews from a movie
@app.get("/movie-info/<movie_id>/review")
def get_all_movie_reviews(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add a review to a certain movie
@app.post("/movie-info/<movie_id>/review")
def add_a_review(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get a certain review from a certain movie
@app.get("/movie-info/<movie_id>/review/<review_id>")
def get_review_from_movie(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
