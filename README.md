# django-weather-api😎

### Welcome to django-weather-api 👋

***

- Para levantar crear ambiente virtual usar `python -m venv .`

- para instalar dependencias usar `pip install -r requirements.txt`

- para levantar Base de datos `docker run -d --name postgres_weather_api -e POSTGRES_USER=weather_api_user -e POSTGRES_PASSWORD=weather_api_pass -e POSTGRES_DB=weather_api_db -p 5432:5432 postgres` 📋

- para migrar debe de ir a la carpeta backend y usar `python manage.py migrate` 📁

- para levantar usar `python manage.py runserver`

- cuando este hecho hechar apuntar POST a ' http://127.0.0.1:8000/api/weather-info' enviando un body tipo json
`{
    "city":"toronto"
}`
- no es necesaria autenticacion

- respuesta esperada con 200 o 201
`{
    "result": {
        "currentemp": 269.67,
        "averagetemp": 274
    }
}`