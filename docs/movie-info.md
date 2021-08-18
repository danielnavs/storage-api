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
|  /movie/store|   Agregar una pelicula
|  /movie/list         |   Listar peliculas    
|  /movie/movie_id        |   Obtener informacion de pelicula por id
|  /movie/movie_id        |  Actualizar informacion de pelicula por id
|  /movie/movie_id/reviews |   Listar reseñas de pelicula por id de pelicula        
|  /movie/movie_id/review   | Agregar una reseña a una pelicula con id    |
|  /movie/movie_id/reviews/review_id|   Obtener detalle de reseña con id para pelicula con id
|  /movie/image/new/image_name  | Agregar imagen de pelicula

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
{ "code": "201", "message": "Movie succesfully added" }
```
-  Mensaje de fallo
```
{
   "code": "400",
   "message": "Invalid data"
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
{ "code": "201", "message": "Your review has been succesfully added" }
```
-  Mensaje de fallo
```
{
   "code": "400",
   "message": "Invalid data"
}
```
### Ejemplos de interacciones con el servidor

```
POST /movie/store
```
- Recibe una estructura de registro de pelicula.
- 201, registrar una pelicula regresa estructura de id para la nueva pelicula.
- D.O.M, regresa mensaje de fallo.

```
GET /movie/list
```
- 200, regresa una lista de peliculas.
- D.O.M, regresa mensaje de fallo en formato json.
- curl http://localhost:8080/movie/list -X GET

```
GET /movie/<movie_id>
```
- 200, regresa datos de pelicula con id.
- D.O.M, regresa mensaje de fallo en formato json.
- curl http://localhost:8080/movie/M001 -X GET

```
POST /movie/<movie_id>
```
- 201, actualizar informacion de una pelicula.
- D.O.M, regresa mensaje de fallo.

```
GET /movie/<movie_id>/review
```
- 200, regresa reseñas de pelicula
- D.O.M, regresa mensaje de fallo.
- curl http://localhost:8080/movie/M001/reviews -X GET
```
POST /movie/<movie_id>/review
```
- 201, agregar una reseña a una pelicula.
- D.O.M, regresa mensaje de fallo.
```
GET /movie/<movie_id>/reviews/<review_id>
```
- 200, regresa una reseña en especifico, de una pelicula.
- D.O.M, regresa mensaje de fallo.
- curl http://localhost:8080/movie/M002/reviews/R002 -X GET

### Autenticacion y autorizacion de usuarios
Los usuarios estan autorizados a consultar y leer toda la informacion respecto a las peliculas y reseñas ajenas. Sin embargo, no esta permitido que las editen.

- Leer todo, editar solo las reseñas propias.
`('app:reviews:read:all', 'app:reviews:write:self)`

- Leer todo, no se permite editar la informacion de las peliculas.
`('app:movies:read:all', 'app:movies:write:none)`

# Documento de plan de implementacion
### Aspecto General
Este proyecto esta pensado para ayudar a los amantes del cine a encontrar nuevas peliculas de las cuales disfrutar, basandose en las reseñas que otras personas han puesto sobre estas.

Este proyecto es un proceso de mejora continua ya que todos los usuarios dependen de todos, teniendo en cuenta que cada uno puede aportar algo significativo al post analisis de una pelicula.
Lo que me motivo a realizar este proyecto fue la satisfaccion de poder generar una comunidad amante del cine dispuesta a cooperar mutuamente para el desarrollo del mismo.

Los recursos que se necesitan para trabajar este proyecto son los desarrolladores involucrados en el desarrollo del sistema. Los usuarios una parte fundamental tambien, ya que sin ellos no funcionaria de la manera correcta. En cuanto a recursos de computo es necesario contar con las herramientas necesarias, las cuales abarcan desde computadoras hasta conocimientos de programacion e implementacion de sistemas en servicios de nube, por mencionar alguno, Google Cloud.

Al concluir y desplegar este proyecto, se realizaran pruebas de funcionamiento y en base a estas se determinara si se necesitan ajustes en el mismo.

### Aspecto Tecnico

#### Modulos de codigo necesarios

- Rutas
Las rutas son una pieza fundamental del proyecto, ya que estas brindan una estructura en cuanto a la navegacion de todas las funcionalidades.

- Funciones de almacenamiento
Las funciones de almacenamiento son necesarias para poder establecer donde se va a guardar toda la informacion obtenida.

- Modulos de funcionalidades del API
Ejemplo: para agregar/listar peliculas o reseñas.

#### Metodos de almacenamiento requeridos

- Almacenamiento de archivos locales

#### Plan para la codificacion de los modulos

Cada modulo debe ser creado a manera de que se puedan realizar pruebas de funcionamiento de los mismos. Es imprescindible que se haga una planificacion previa de la funcionalidad de los modulos. Asi se evitara crear funciones innecesarias y usar de la mejor manera los recursos que se tienen a disposicion.

#### Plan para la verificacion de la  calidad del producto

Al finalizar el proyecto se realizaran pruebas para verificar el correcto funcionamiento de este. Esto con la finalidad de cumplir con todas las espectativas planteadas al inicio del proyecto. Asimismo, las pruebas nos ayudan a encontrar ciertas vulnerabilidades o defectos en el sistema y asi, solucionarlo antes de realizar el despliegue.

# Evaluacion - Computo en la nube
1. Crear un fork del proyecto storage-api
**Señalar cual es el commit-hash a partir de haber realizado el fork**

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de Fork|   a56280933431fd3254f2d220a0b98fdcb7479dd2

2. Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones.  **Señalar el commit-hash que contiene la creación de dichos archivos.**

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de docs/movie-info.md|   a56280933431fd3254f2d220a0b98fdcb7479dd2
|  Creacion de: modules/movie-info.py routes/movie-info.py models/movie-info.py|   ce38e60ec25bb8e3129b9ff5ebc94d9e33b9c28e

3. Crear todas las rutas especificadas en su archivo de documentación dentro de su archivo en la carpeta routes, y todas deben de responder 501, con Content-Type: application/json, y un cuerpo de respuesta en formato json con 2 llaves, code y message, el message debe contener el mensaje, Not Implemented.
 **Señalar el commit-hash que contiene la codificacion de las rutas.**

 | Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de rutas|   bbf0375065aa028f5cd8be05267e3bf10ea47b72

4. Crear en su carpeta de modulos funciones que emulen las interacciones con el almacén de archivos o datos, es decir que si necesitas una función de consulta, crear una función que retorne una consulta simulada con datos codificados como constantes, y si necesitas crear objetos funciones que retornen simulando una creación exitosa.
**Señalar el commit-hash que contiene la codificacion de estas funciones asistentes.**

 | Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de funciones |   e85e432504cbb880143be4fa06a20254b782a03a


5. Crear mock ups, de las vistas que desean implementar, utilizando MoqUps (conectar a su google drive).
– Una vez concluidas las propuestas de vistas exportar a imagen, e incluir en el documento una explicacion de los datos expresados en las vistas emparejandolos con que endpoints contienen dicha informacion o a cual endpoint de su proyecto, estos activan.
– Las imagenes deberan ser nombradas como ./docs/assets/--.png
**Señalar el commit-hash que contiene la inclusión de estas descripciones al documento, junto con los commits que contienen las imagenes.**

### Explicacion de mock-ups

![Login](https://github.com/danielnavs/storage-api/raw/master/docs/assets/movie-info-0001-review_page.PNG)

La imagen **docs/assets/movie-info-0001-review_page.png** muestra un formulario donde el usuario puede registrar una reseña en la pelicula de su eleccion. Se le solicita una calificacion y un comentario respecto a la pelicula. Al final se encuentra un boton de submit, el cual sirve para guardar los cambios.

![Login](./assets/movie-info-0002-add_movie_page.PNG)

La imagen **docs/assets/movie-info-0002-add_movie_page.png** muestra un formulario para agregar una nueva pelicula al sistema. Se despliegan diferentes campos los cuales se le asignaran como atributos a la pelicula en cuestion. Al final se encuentra un boton de submit, el cual sirve para guardar los cambios.

![Login](assets/movie-info-0003-movies_list.PNG)

La imagen **docs/assets/movie-info-0003-movies_list** muestra la lista de todas las peliculas existentes seguido de dos opciones:
- Ver informacion. Proporciona la informacion de cada pelicula, independientemente.
- Agregar reseña. Funcion para agregar una reseña a una pelicula.

 | Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion y explicacion de mock-ups|   e1201c5529b6b655d48cf583eb92661f9b509f19

# Casos de uso

- El usuario desea agregar una nueva pelicula.
  - Para ello, el usuario debe ingresar los campos requeridos para almacenar una pelicula. Los cuales son: id, titulo, genero, director, fecha de lanzamiento y sinopsis.
  - Si el usuario registra los datos incorrectamente, se le mostrara un error html 400 con el mensaje "Invalid data".
  - Ejemplo de curl de un registro exitoso (metodo POST):

 ```
 curl http://localhost:8080/movie/store -X POST -H 'Content-Type: application/json' -d '{"movie_id": "M003","title": "Hulk", "genre2": "Accion", "director": "Louis Leterrier", "release_date": "2008-06-08", "sinopsys": "Bruce Banner recorre el mundo en busca de un antidoto para librarse de su alter ego."}'
 ```

- El usuario desea actualizar los detalles de una pelicula. En especifico, se desea actualizar la sinopsis.
  - Para actualizar los datos de una pelicula, es necesario ingresar los campos de la pelicula que ya han sido registrados anteriormente, con la diferencia de que la sinopsis sera reemplazada.
  - Si el usuario registra los datos incorrectamente, se le mostrara un error html 400 con el mensaje "Invalid data".
  - Ejemplo de curl para una actualizacion de pelicula (metodo POST):

 ```
  curl http://localhost:8080/movie/M003 -X POST -H 'Content-Type: application/json' -d '{"movie_id": "M003","title": "Hulk", "genre2": "Accion", "director": "Louis Leterrier", "release_date": "2008-06-08", "sinopsys": "Bruce Banner recorre el mundo en busca de un antidoto."}'
 ```

- El usuario desea consultar todas las peliculas almacenadas el sistema.
  - Si el usuario utiliza una ruta incorrecta, se le mostrara un error html 500 con el mensaje "Error interno".
  - Ejemplo de curl (metodo GET):

  ```
  curl http://localhost:8080/movie/list -X GET
  ```

- El usuario desea consultar los detalles de una pelicula en especifico.
  - En estos casos, se cuenta con el identificador unico de cada pelicula. El requerimiento es que el usuario especifique cual es el identificador (id) de la pelicula a consultar.
  - Si el usuario utiliza una ruta o un id incorrecto (o inexistente), se le mostrara un error html 500 con el mensaje "Error interno".
  - Ejemplo de curl para una consulta de todas las peliculas (metodo GET):

  ```
  curl http://localhost:8080/movie/M003 -X GET
  ```

- El usuario desea agregar una reseña a una pelicula.
  - Para ello, el usuario debe ingresar los campos requeridos para almacenar una reseña. Los cuales son: id de la pelicula a la cual se le asignara la reseña (movie_id), id de la reseña, el id del usuario, titulo de la pelicula, puntuacion y comentario.
  - Si el usuario registra los datos incorrectamente, se le mostrara un error html 400 con el mensaje "Invalid data".
  - Ejemplo de curl para agregar una reseña (metodo POST):

  ```
  curl http://localhost:8080/movie/M003/review -X POST -H 'Content-Type: application/json' -d '{"review_id": "R004","user_id": "U001", "movie_id": "M003", "movie_title": "Hulk", "rate": "5", "comment": "Muy buena pelicula. Entretenida."}'
  ```

- El usuario desea consultar todas las reseñas que ha recibido una pelicula.
  - Para ello, el usuario debe especificar el id de la pelicula a consultar.
  - Si el usuario utiliza una ruta o un ID incorrecto (o inexistente), se le mostrara un error html 500 con el mensaje "Error interno".
  - Ejemplo de curl para una consuilta de reseñas exitosa (metodo GET):

  ```
  curl http://localhost:8080/movie/M003/reviews -X GET
  ```

- El usuario desea consultar una reseña en especifico de una pelicula en particular.
  - Para ello, el usuario debe especificar el id de la pelicula y el id de la reseña a consultar.
  - Si el usuario utiliza una ruta o un ID incorrecto (o inexistente), se le mostrara un error html 500 con el mensaje "Error interno".
  - Ejemplo de curl para una consulta exitosa (metodo GET):

  ```
  curl http://localhost:8080/movie/M002/reviews/R002 -X GET
  ```

- El usuario desea agregar una imagen de una pelicula.
  - Para el almacenamiento de imagenes, estas deben estar nombradas como el titulo de la pelicula. Ejemplo: Shrek2.jpg. De igual manera, es necesario especificar la ruta completa donde se encuentra la imagen.
  - Si el usuario ingresa la ruta del archivo o el nombre de la imagen incorrectamente, se le mostrara un error html 400 con el mensaje "Invalid data".
  - Ejemplo de curl para subir una imagen exitosamente (metodo POST):

```
curl http://localhost:8080/movie/image/new/Hulk -X POST -H 'Content-Type: multipart/form-data' -F 'image_file=@/C/Users/dnavarro/images/Hulk.jpg'
```

# Planeacion del desarrollo del frontend

El desarrollo del frontend requiere de un análisis profundo en cuanto a las funcionalidades del proyecto. Todas y cada una de las funcionalidades deben de ir acorde con lo establecido en el backend. La base de dicha interfaz será estructurada en un archivo html, que, en conjunto con funciones de JavaScript y CSS se le dará vida al proyecto y el propósito es que la interfaz sea amigable para el usuario.

Se integrará una página principal, la cual contara con sub paginas donde se mostrarán las siguientes opciones con las que el usuario puede interactuar:

- **Consultar todas las peliculas.**

![Login](assets/movie-info-0003-movies_list.PNG)

La imagen muestra la lista de todas las peliculas existentes seguido de dos opciones:
- **Ver informacion de pelicula.** Proporciona los detalles de cada pelicula, independientemente.
  - **Consultar todas las reseñas de una peliculas.** Una vez el usuario ha entrado a la pagina de la pelicula en cuestion, puede ver todas las reseñas que dicha pelicula ha recibbido.
  - **Consultar una reseña en especifico sobre una pelicula.** Una vez el usuario ha entrado a la pagina de la pelicula en cuestion, puede consultar una reseña en especifico sobre la pelicula.
- **Actualizar datos de pelicula.** Es posible actualizar los detalles de una pelicula.
- **Agregar reseña.** Funcion para agregar una reseña a una pelicula.

![Login](https://github.com/danielnavs/storage-api/raw/master/docs/assets/movie-info-0001-review_page.PNG)

La imagen  muestra un formulario donde el usuario puede registrar una reseña en la pelicula de su eleccion. Se le solicita una calificacion y un comentario respecto a la pelicula. Al final se encuentra un boton de submit, el cual sirve para guardar los cambios.

- **Agregar pelicula.**

![Login](./assets/movie-info-0002-add_movie_page.PNG)

La imagen muestra un formulario para agregar una nueva pelicula al sistema. Se despliegan diferentes campos los cuales se le asignaran como atributos a la pelicula en cuestion. Al final se encuentra un boton de submit, el cual sirve para guardar los cambios.

Entre otras funcionalidades, se encuentran la siguiente:
- **Subir una imagen de una pelicula.**

Es importante tener en cuenta las necesidades o peticiones del usuario ya que en base a esto se puede mejorar el sistema al agregar nuevas funcionalidades y solucionar posibles fallos de funcionamiento.
