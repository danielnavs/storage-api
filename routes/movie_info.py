import bottle
from modules.bottles import BottleJson

app = BottleJson()

@app.get("/")
def store_record(*args, **kwargs):
    return dict(code= 501, message = "Not implemented")

## Add a movie
@app.post("/movie_info/add")
def add_a_movie(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented hah")

## Get movies list
@app.get("/movie_info/list")
def get_movies_list(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

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
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get a certain review from a certain movie
@app.get("/movie_info/<movie_id>/review/<review_id>")
def get_review_from_movie(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
