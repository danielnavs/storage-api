import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.movie_info import (
    add_movie,
    get_movies_list,
    get_movie_details,
    update_movie_details,
    get_reviews_from_movie,
    add_review,
    get_review_from_certain_movie
)

app = BottleJson()

@app.get("/")
    #Default route

## Add a movie
# Curl Example:
# curl http://localhost:8080/movie/store -X POST -H 'Content-Type: application/json' -d '{"movie_id": "002","title": "Shrek3", "genre2": "Cartoon", "director": "elnava", "release_date": "1999-01-01", "sinopsys": "muylejanojaja"}'
@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        movie_id = str(payload['movie_id'])
        title  = str(payload['title'])
        genre2 = str(payload['genre2'])
        director = str(payload['director'])
        release_date = dt.date.fromisoformat(payload['release_date'])
        sinopsys= str(payload['sinopsys'])
        print("Datos validos")
        respuesta = add_movie(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)

## Get movies list
## Curl example:
# curl http://localhost:8080/movie/list -X GET
@app.get("/list")
def get_all_movies(*args, **kwargs):
    try:
       respuesta = get_movies_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Get movie details
## Curl Example:
# curl http://localhost:8080/movie/001 -X GET
@app.get("/<movie_id>")
def get_movie_per_id(*args, movie_id=None, **kwargs):
    try:
        respuesta = get_movie_details(movie_id = movie_id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

## Update movie details
@app.post("/<movie_id>")
def bar(*args, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    try:
        title = str(payload['title'])
        genre2 = str(payload['genre2'])
        director = str(payload['director'])
        release_date = str(payload['release_date'])
        year, month, date = [int(x) for x in release_date.split("-")]
        sinopsys= str(payload['sinopsys'])
        print("Datos validos")
        respuesta = update_movie_details(**payload)
        raise bottle.HTTPError(201)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)

## Add a review to a certain movie
# Example curl:
# curl http://localhost:8080/movie/007/review -X POST -H 'Content-Type: application/json' -d '{"review_id": "002","user_id": "001", "movie_id": "007", "movie_title": "Inception", "rate": "5", "comment": "goooood bro ngl"}'
@app.post("/<movie_id>/review")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        movie_id = str(payload['movie_id'])
        review_id = str(payload['review_id'])
        user_id = str(payload['user_id'])
        movie_title = str(payload['movie_title'])
        rate = str(payload['rate'])
        comment = str(payload['comment'])
        print("Datos validos")
        respuesta = add_review(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, "Your review has been succesfully added")

## Get all reviews from a movie
## Curl example:
# curl http://localhost:8080/movie/M001/reviews -X GET
@app.get("/<movie_id>/reviews")
def get_all_reviews_from_movie(*args, movie_id=None, **kwargs):
    try:
       respuesta = get_reviews_from_movie(movie_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Get a certain review from a certain movie
## Curl examples:
# curl http://localhost:8080/movie/M002/reviews/R003 -X GET
# curl http://localhost:8080/movie/M002/reviews/R002 -X GET
@app.get("/<movie_id>/reviews/<review_id>")
def get_specific_review_from_movie(*args, movie_id=None,  review_id=None, **kwargs):
    try:
       respuesta = get_review_from_certain_movie(review_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)
