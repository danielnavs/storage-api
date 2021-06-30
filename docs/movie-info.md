# Acerca de este proyecto

Este proyecto se trata sobre una coleccion de peliculas e informacion
relevante de estas. La finalidad es que el usuario pueda consultar
dicha informacion de ciertas peliculas para llegarlas a conocer mas a fondo
y en base a esto determinar si desea verla o no.

# Modo de uso

| Path                  | Descripción |
| --------------------- | ----------- |
|  /movie-info/movie           |   Muestra informacion basica de la pelicula          
|   /movie-info/user    | Muestra datos del usuario         |
| /movie-info/review          |  Muestra la reseña de la pelicula             |

# Archivos Relacionados

- `routes/movie-info.py`
- `modules/movie-info.py`

# Guia para articular un API JSON

La estructura del proyecto se basa en las siguientes entidades:

- Pelicula (titulo, genero, director, fecha_lanzamiento)
- Sinopsis (pendiente)
- Usuario (nombre, edad, id)
- Resena (usuario_id, rate)
