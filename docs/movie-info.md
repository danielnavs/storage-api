# Acerca de este proyecto

Este proyecto se trata sobre una coleccion de peliculas e informacion
relevante de estas. La finalidad es que el usuario pueda consultar e interactuar
con dicha informacion, de tal manera que pueda dar su opinion
al respecto a manera de reseña.

# Modo de uso

| Path                  | Descripción |
| --------------------- | ----------- |
|  /movie-info/movie/movie_id          |   Muestra informacion basica de la pelicula          
|   /movie-info/user/user_id    | Muestra datos del usuario         |
| /movie-info/movie/movie_id/reseña          |  Muestra la reseña de la pelicula             |

# Archivos Relacionados

- `routes/movie-info.py`
- `modules/movie-info.py`

# Guia para articular un API JSON

La estructura del proyecto se basa en las siguientes entidades:

- Pelicula (id, titulo, genero, director, fecha_lanzamiento, sinopsis)
- Usuario (id, nombre, edad)
- Reseña (usuario_id, pelicula_id, rate)

# Operaciones de Almacenamiento de datos

### Operaciones de  Usuario :man:
- Se solicita nombre y edad.
- El ID se auto asigna al usuario.

### Operaciones de Peliculas :clapper:
- Se solicita el titulo de la pelicula, genero, director, fecha de lanzamiento y sinopsis.
- El ID se auto asigna a la pelicula

### Operaciones de Reseñas :page_facing_up:
- Se solicita el ID del usuario, el ID de la pelicula, y la reseña.

# Operaciones de consulta de datos
Pendiente

# Estructuras de solicitud y respuesta
### Registro de usuario
```
{
    "nombre": "Javier Hernandez",
    "fecha_de_nacimiento": "1988-01-01"
}

```
### Respuesta de registro de usuario exitoso
```
{ "id": "0001" }
```

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
Pendiente
