# Acerca de este proyecto

Este proyecto consiste en tener una coleccion de peliculas e informacion
relevante de estas. La finalidad es que el usuario pueda consultar e interactuar
con dicha informacion, de tal manera que pueda dar su opinion al respecto
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

# Guia para articular un API JSON

La estructura del proyecto se basa en las siguientes entidades:

- Pelicula (id, titulo, genero, director, fecha_lanzamiento, sinopsis)
- Reseña (usuario_id, pelicula_id, puntuacion, comentario)

# Operaciones de Almacenamiento de datos

### Operaciones de Peliculas :clapper:
- Se solicita el titulo de la pelicula, genero, director, fecha de lanzamiento y sinopsis.
- El ID se auto asigna a la pelicula

### Operaciones de Reseñas :page_facing_up:
- Se solicita el ID del usuario, el ID de la pelicula, la puntuacion y la reseña.

# Operaciones de consulta de datos
Pendiente

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

# Implementación de rutas para los recursos
```
POST /movie-info/add
```
- Pendiente
```
GET/movie-info/list
```
```
GET/movie-info/<movie_id>
```
```
POST /movie-info/<movie_id>
```
```
GET /movie-info/<movie_id>/review
```
```
POST /movie-info/add
```
```
GET/movie-info/<movie_id>/review/<review_id>
```
