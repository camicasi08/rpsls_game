# RPSLS -GAME

Para la ejecución de esta aplicación es necesario seguir los siguientes pasos:

Requerimientos 
* [Python 3.7]
# Instalación
```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```
* Es necesario instalar un servidor de Redis para el funcionamiento de la aplicación, la versión usada en windows para las pruebas de la aplicación fue la 3.2. Es una carpeta y se ejecuta el archivo redis-server.exe

```sh
$ python manage.py runsever
```


