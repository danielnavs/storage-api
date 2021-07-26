""""
import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
"""
import bottle
from modules.bottles import BottleJson
from modules.movie_info import add_movie, add_review

app = BottleJson()

@app.get("/")


## Add a movie
# Curl Example:
# curl "localhost:8080/movie_info/add?title=shrek2&genre2=cartoon&director=elnava&release_date=2000-05-23&sinopsys=muylejanojajj"

@app.post("/movie_info/add")
def bar(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
        #movie_id: int(payload['movie_id'])
        title = str(payload['title'])
        genre2 = str(payload['genre2'])
        director = str(payload['director'])
        release_date = str(payload['release_date'])
        year, month, date = [int(x) for x in release_date.split("-")]
        sinopsys= str(payload['sinopsys'])
        print("Datos validos")
        respuesta = add_movie(**payload)
        raise bottle.HTTPError(201)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)

## Get movies list
@app.get("/movie_info/list")
def get_movies_list(*args, **kwargs):
    payload = bottle.request.query
    print(payload)

## Get movie details
@app.get("/movie_info/<movie_id>")
def get_movie_details(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Update movie details
@app.post("/movie_info/<movie_id>")
def update_movie_details(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get all reviews from a movie
@app.get("/movie_info/<movie_id>/review")
def get_all_movie_reviews(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add a review to a certain movie
@app.post("/movie_info/<movie_id>/review")
def add_a_review(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
        #user_id = str(payload['user_id'])
        movie_id = int(payload['movie_id'])
        rate = str(payload['rate'])
        comment = str(payload['comment'])
        print("Datos validos")
        respuesta = add_review(**payload)
        raise HTTPError(201)
    except:
        print("Datos invalidos")
        raise HTTPError(400)
    raise HTTPError(500)

## Get a certain review from a certain movie
@app.get("/movie_info/<movie_id>/review/<review_id>")
def get_review_from_movie(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
