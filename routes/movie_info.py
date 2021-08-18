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
    get_review_from_certain_movie,
    add_new_image
)

app = BottleJson()


@app.get("/")
    #Default route

@app.post("/store")
def store(*args, **kwargs):
    """

    Route to add a movie.
    Curl Example:
    curl http://localhost:8080/movie/store -X POST -H 'Content-Type: application/json' -d '{"movie_id": "M003","title": "Hulk", "genre2": "Accion", "director": "Louis Leterrier", "release_date": "2008-06-08", "sinopsys": "Bruce Banner recorre el mundo en busca de un antidoto para librarse de su alter ego."}'

    """
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
    raise bottle.HTTPError(201, "Movie succesfully added")


@app.get("/list")
def get_all_movies(*args, **kwargs):

    """

    Route to get movies list
    Curl example:
    curl http://localhost:8080/movie/list -X GET

    """
    try:
       respuesta = get_movies_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


@app.get("/<movie_id>")
def get_movie_per_id(*args, movie_id=None, **kwargs):

    """

    Route to get movie details
    Curl Example:
    curl http://localhost:8080/movie/M001 -X GET

    """
    try:
        respuesta = get_movie_details(movie_id = movie_id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

@app.post("/<movie_id>")
def update_movie_data(*args, **kwargs):
    """

    Route to update movie details
    This works as a simple post. The store_string function
    updates de info that was previously stored.
    Curl example to update the Soy Leyenda movie information
    curl http://localhost:8080/movie/M002 -X POST -H /
    'Content-Type: application/json' -d /
    '{"movie_id": "M002","title": "Soy Leyenda", "genre2": "Accion", "director": "Francis Lawrence", "release_date": "2008-01-18", "sinopsys": "Un cientifico lucha por sobrevivir contra unos mutantes nocturnos con sed de sangre."}'

    """
    payload = bottle.request.json
    print(payload)
    try:
        movie_id = str(payload['movie_id'])
        title = str(payload['title'])
        genre2 = str(payload['genre2'])
        director = str(payload['director'])
        release_date = str(payload['release_date'])
        year, month, date = [int(x) for x in release_date.split("-")]
        sinopsys= str(payload['sinopsys'])
        print("Datos validos")
        respuesta = update_movie_details(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, "Movie data has been updated")


@app.post("/<movie_id>/review")
def bar(*args, **kwargs):
    """

    Route to add a review to a certain movie
    Example curl:
    curl http://localhost:8080/movie/007/review -X POST -H 'Content-Type: application/json' -d '{"review_id": "R004","user_id": "001", "movie_id": "M001", "movie_title": "Shrek 2", "rate": "5", "comment": "goooood bro ngl"}'

    """
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
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, "Your review has been succesfully added")

@app.get("/<movie_id>/reviews")
def get_all_reviews_from_movie(*args, movie_id=None, **kwargs):

    """

    Route to get all reviews from a movie
    Curl example:
    curl http://localhost:8080/movie/M001/reviews -X GET

    """
    try:
       respuesta = get_reviews_from_movie(movie_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


@app.get("/<movie_id>/reviews/<review_id>")
def get_specific_review_from_movie(*args, movie_id=None,  review_id=None, **kwargs):

    """

    Route to get a certain review from a certain movie
    Curl examples:
    curl http://localhost:8080/movie/M002/reviews/R003 -X GET
    curl http://localhost:8080/movie/M002/reviews/R002 -X GET

    """

    try:
       respuesta = get_review_from_certain_movie(review_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


@app.post("/image/new/<image_name>")
def new_image(image_name):
    """

    Route to store a movie image
    Curl example:
    curl http://localhost:8080/movie/image/new/Shrek2 -X POST -H 'Content-Type: multipart/form-data' -F 'image_file=@/C/Users/dnavarro/images/shrek.jpg'

    """
    try:
        image_file = bottle.request.files.get("image_file")
        payload = {
            "image_name": image_name,
            "image_file": image_file.file
        }
        respuesta = add_new_image(**payload)
    except:
        print("Invalid data")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, "The movie image has been uploaded succesfully")
