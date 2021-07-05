# Acerca de este proyecto

Este proyecto consiste en tener una coleccion de peliculas e informacion
relevante de estas. La finalidad es que el usuario pueda consultar e interactuar
con dicha informacion, de tal manera que pueda dar su opinion sobre la pelicula
a manera de reseña.

# API

| Path                  | Descripción |
| --------------------- | ----------- |
|  /movie-info/add|   Agregar una pelicula
|  /movie-info/list         |   Listar peliculas    
|  /movie-info/<movie_id>         |   Obtener informacion de pelicula por id
|  /movie-info/<movie_id>          |  Actualizar informacion de pelicula por id
|  /movie-info/<movie_id>/review |   Listar reseñas de pelicula por id de pelicula        
|  /movie-info/<movie_id>/review   | Agregar una reseña a una pelicula con id    |
|  /movie-info/<movie_id>/review/<review_id>|   Obtener detalle de reseña con id para pelicula con id

# Archivos Relacionados

- `routes/movie-info.py`
- `modules/movie-info.py`

# Estructura del proyecto

La estructura del proyecto se basa en las siguientes entidades:

- Pelicula (id, titulo, genero, director, fecha_lanzamiento, sinopsis)
- Reseña (usuario_id, pelicula_id, puntuacion, comentario)

# Operaciones de Almacenamiento de datos

### Operaciones de Peliculas :clapper:
- Se solicita el titulo de la pelicula, genero, director, fecha de lanzamiento y sinopsis.
- El ID se auto asigna a la pelicula

### Operaciones de Reseñas :page_facing_up:
- Se solicita el ID del usuario, el ID de la pelicula, la puntuacion y comentario.
- El ID se auto asigna a la reseña

# Operaciones de consulta de datos

- Solicitar datos de una pelicula
  - Por ID
- Solicitar datos de una reseña
  - Por ID
- Lista de peliculas
  - Por ID
  - Todas
- Lista de reseñas
  - Por ID
   - Todas

# Estructuras de solicitud y respuesta

### Registro de pelicula
```
{
   "titulo": "Shrek 2",
   "genero": "Fantasia",
   "director": "Andrew Adamson"
   "fecha_de_lanzamiento": "1988-01-01"
}
```
### Respuesta de registro de pelicula exitoso
```
{ "id": "P001" }
```
### Mensaje de fallo
```
{
	"code": "",
	"message": "An error has occurred"
}
```
# Implementación de rutas para los recursos
```
POST /movie-info/add
```
- Recibe una estructura de registro de pelicula.
- 201, registrar una pelicula regresa estructura de id para la nueva pelicula.
- D.O.M, regresa mensaje de fallo.
```
GET/movie-info/list
```
- 200, regresa una lista de peliculas.
- D.O.M, regresa mensaje de fallo en formato json.
```
GET/movie-info/<movie_id>
```
- 200, regresa datos de pelicula con id.
- D.O.M, regresa mensaje de fallo en formato json.
```
POST /movie-info/<movie_id>
```
- 201, actualizar informacion de una pelicula.
- D.O.M, regresa mensaje de fallo.
```
GET /movie-info/<movie_id>/review
```
- 200, regresa reseñas de pelicula
- D.O.M, regresa mensaje de fallo.
```
POST /movie-info/<movie_id>/review
```
- 201, agregar una reseña a una pelicula.
- D.O.M, regresa mensaje de fallo.
```
GET/movie-info/<movie_id>/review/<review_id>
```
- 200, regresa una reseña en especifico, de una pelicula.
- D.O.M, regresa mensaje de fallo.
