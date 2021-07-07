# Descripcion general del proyecto
Este proyecto consiste en una coleccion de peliculas e informacion
relevante de estas. La finalidad es que el usuario pueda consultar e interactuar
con dicha informacion, de tal manera que pueda dar su opinion sobre la pelicula
a manera de reseña.

### Sector
 Este proyecto esta pensado para generar interacciones entre los amantes del cine, respecto
a sus peliculas favoritas. El hecho de crear una comunidad puede ser beneficioso para la industria del cine o servicios de streaming. Al hacer mencion de peliculas, independientemente si son recientes o antiguas, estas cobran una nueva vida al ser descubiertas por nuevos espectadores en busca de una buena pieza de entretenimiento.

### Modelado de datos
El tener una estructura establecida previo al inicio de un proyecto es muy importante para el buen funcionamiento y desarrollo de este. La estructura del proyecto se basa en las siguientes entidades:

- Pelicula (id, titulo, genero, director, fecha_lanzamiento, sinopsis)
- Reseña (usuario_id, pelicula_id, puntuacion, comentario)

Cada entidad cuenta con sus propios atributos, los cuales son necesarios para poder tener interacciones entre ambas,

### Interacciones de datos

La interaccion entre los datos es la base del funcionamiento de este proyecto. Algunas interacciones basicas son las siguientes:

- Al registrar una nueva pelicula, esta puede permanecer sin reseña . Sin embargo, no es posible crear una reseña que no ha sido asignada a ninguna pelicula.
- Al registrar una nueva reseña, se solicita el id de la pelicula deseada.
- Es posible obtener detalles de una reseña en particular, para una pelicula en especifico.

### Consultas de datos

Las consultas de datos sirven para obtener detalles de la informacion ya recabada. A continuacion se enlistan las consultas posibles a la informacion de este proyecto:

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

### Operaciones de datos
El usuario puede interactuar con los datos del servidor de diferentes maneras:

- Al querer registrar reseñas, el usuario debe tener en cuenta que peliculas estan disponibles para poder interactuar. Para ello, puede consultar en el servidor la **lista completa de las peliculas** existentes.
- El usuario, ya con conocimiento de las peliculas existentes, puede **extraer informacion detallada** de una **pelicula** en especifico.
- Los usuarios pueden **escribir una reseña** sobre la pelicula de su eleccion.
- Si lo desea, un usuario puede **consultar todas las reseñas** que hayan hecho otros usuarios sobre una pelicula en especifico.

### Rutas HTTP
A continuacion, se presentan las rutas HTTP y su respectiva descripcion.

| Path                  | Descripción |
| --------------------- | ----------- |
|  /movie-info/add|   Agregar una pelicula
|  /movie-info/list         |   Listar peliculas    
|  /movie-info/<movie_id>         |   Obtener informacion de pelicula por id
|  /movie-info/<movie_id>          |  Actualizar informacion de pelicula por id
|  /movie-info/<movie_id>/review |   Listar reseñas de pelicula por id de pelicula        
|  /movie-info/<movie_id>/review   | Agregar una reseña a una pelicula con id    |
|  /movie-info/<movie_id>/review/<review_id>|   Obtener detalle de reseña con id para pelicula con id

### Ejemplos de mensajes HTTP que aceptara y emitira el servidor

#### Registro de pelicula
```
{
   "titulo": "Shrek 2",
   "genero": "Fantasia",
   "director": "Andrew Adamson",
   "fecha_de_lanzamiento": "1988-01-01",
   "sinopsis": "Shrek, Burro y la Princesa Fiona se enfrentan a toda una divertida serie de nuevas aventuras en las que aparecen personajes clásicos de cuentos de hadas."
}
```
- Respuesta de registro de pelicula exitoso
```
{ "id": "P001" }
```
-  Mensaje de fallo
```
{
	"code": "500",
	"message": "An error has occurred"
}
```

#### Registro de reseña
```
{
   "user_id": "U001",
   "movie_id": "P001",
   "rate": "4/5"
   "comment": "Me agrada la pelicula y el desenlace de los personajes."
}
```
- Respuesta de registro de reseña exitoso
```
{ "id": "R001" }
```
-  Mensaje de fallo
```
{
	"code": "500",
	"message": "An error has occurred"
}
```
### Ejemplos de interacciones con el servidor
```
POST /movie-info/add
```
- Recibe una estructura de registro de pelicula.
- 201, registrar una pelicula regresa estructura de id para la nueva pelicula.
- D.O.M, regresa mensaje de fallo.
```
GET /movie-info/list
```
- 200, regresa una lista de peliculas.
- D.O.M, regresa mensaje de fallo en formato json.
```
GET /movie-info/<movie_id>
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
GET /movie-info/<movie_id>/review/<review_id>
```
- 200, regresa una reseña en especifico, de una pelicula.
- D.O.M, regresa mensaje de fallo.

### Autenticacion y autorizacion de usuarios
Los usuarios estan autorizados a consultar y leer toda la informacion respecto a las peliculas y resenas ajenas. Sin embargo, no esta permitido que las editen.

- Leer todo, editar solo las reseñas propias.
`('app:reviews:read:all', 'app:reviews:write:self)`

# Documento de plan de implementacion
## Aspecto General
## Aspecto Tecnico
