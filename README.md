# Microservices

## Lancement du projet

### Configuration

Créez une base de données MongoDB puis entrez dans le dossier du microservice 'student' : ```cd student```.
Il faudra également créer une base de données MongoDB pour le microservice PostgreSQL.

Créez un fichier .env et rentrez les informations suivantes :

```
'NAME': <nom de la base de données postgres>
'USER': <nom d'utilisateur de la base de données>
'PASSWORD': <mot de passe associé>
'HOST': <host (localhost)>
'PORT': <numéro de port (5432)>
```

Le fichier requirements.txt est situé à la racine du projet. Par conséquent, dans le terminal de votre projet, 

écrivez ```cd```, puis : ```pip install -r requirements.txt```.

Ensuite, appliquez les migrations : ```python manage.py migrate```.

Puis lancer les serveurs :

- gateway : ```python manage.py runserver 0.0.0.0:8000```
- school : ```python manage.py runserver 0.0.0.0:8001```
- student : ```python manage.py runserver 0.0.0.0:8002```.

Dans chaque app, les models sont la représentation de la base de données. Ils contiennent les champs  
contenus dans chaque base. Les views contiennent la logique métier. Elles définissent ce qui se passe  
lorsqu'une requête est envoyée à une url spécifique. Les urls elles-mêmes sont définies dans le fichier urls.

Django Rest Framework fournit un front dans lequel on peut représenter les champs de la base. Le front est lancé
dans l'url du serveur.