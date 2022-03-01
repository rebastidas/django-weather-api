# django-weather-api😎

### Welcome to django-weather-api 👋

***

- Para levantar crear ambiente virtual usar `python -m venv .`

- para instalar dependencias usar `pip install -r requirements.txt`

- para levantar Base de datos `docker run -d --name postgres_weather_api -e POSTGRES_USER=weather_api_user -e POSTGRES_PASSWORD=weather_api_pass -e POSTGRES_DB=weather_api_db -p 5432:5432 postgres` 📋

- para migrar debe de ir a la carpeta backend y usar `python manage.py migrate` 📁

- para crear user capaz de recibir token `python manage.py createsuperuser`

- para levantar usar `python manage.py runserver`

- para la autenticacion debe esnviar un header debe apuntar un post a 'http://127.0.0.1:8000/api/token' enviando un body tipo json:
`{
    "username":"agregar username como string">,
    "password":"pass como string"
}`
  esto dara como resltado una respuesta 200 que traera un json:

  `{
    "refresh":"token",
    "access":"token"
  }`

- cuando este hecho hechar apuntar POST a 'http://127.0.0.1:8000/api/weather-info' enviando un body tipo json
`{
    "city":"toronto"
}`
 con un `header = {"Authentication" : "Bearer accessTOKEN"}`

- respuesta esperada con 200 o 201
`{
    "result": {
        "currentemp": 269.67,
        "averagetemp": 274
    }
}`