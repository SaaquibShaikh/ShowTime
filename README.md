# ShowTime

API for identifing the top movies and a ticket booking system, where users can check the movies and book tickets.

## Setting up the project
### Installing Django and other requirements
Python 3.10.5 is the version used for creating this project

Open the project folder
and install requirements.txt

```
pip3 install -r requirements.txt
```

Creating the Django Project

```
django-admin startproject ShowTime
```
Creating necessary tables related to authentications,logentries and other tables

````
python manage.py migrate
````
Creating SuperUser(Admin) for the project
```
python manage.py createsuperuser
```
## Creating app and adding it to Django Project

```
python manage.py startapp api
```
This will create 'api' app folder in the project.

Now open ShowTime/settings.py
	Inside Installed Apps list add the created app named ```'api'``` and save the file, this will integrate the api app to the project.

Inside the api app, in models.py file we define Models that are needed for the application

Shows, Theatre, Movie, City

```
python manage.py makemigrations api
python manage.py migrate
```

To start the server use the following command

```
python manage.py runserver
```

### Checking Shows for a movie in the City

http://127.0.0.1/api/movies

{
  "movies": [
    {
      "id": 433,
      "name": "The Shawshank Redemption",
      "rating": 9.2
    },
    {
      "id": 434,
      "name": "The Godfather",
      "rating": 9.2
    },
    {
      "id": 435,
      "name": "The Dark Knight",
      "rating": 9
    },
    {
      "id": 436,
      "name": "The Godfather Part II",
      "rating": 9
    },
    {
      "id": 437,
      "name": "12 Angry Men",
      "rating": 9
    },
    {
      "id": 438,
      "name": "Schindler's List",
      "rating": 8.9
    },
    {
      "id": 439,
      "name": "The Lord of the Rings: The Return of the King",
      "rating": 8.9
    },
    {
      "id": 440,
      "name": "Pulp Fiction",
      "rating": 8.8
    },
    {
      "id": 441,
      "name": "The Lord of the Rings: The Fellowship of the Ring",
      "rating": 8.8
    },
    {
      "id": 442,
      "name": "The Good, the Bad and the Ugly",
      "rating": 8.8
    },
    {
      "id": 443,
      "name": "Forrest Gump",
      "rating": 8.8
    },
    {
      "id": 444,
      "name": "Fight Club",
      "rating": 8.7
    },
    {
      "id": 445,
      "name": "Inception",
      "rating": 8.7
    },
    {
      "id": 446,
      "name": "The Lord of the Rings: The Two Towers",
      "rating": 8.7
    },
    {
      "id": 447,
      "name": "Star Wars: Episode V - The Empire Strikes Back",
      "rating": 8.7
    },
    {
      "id": 448,
      "name": "The Matrix",
      "rating": 8.7
    },
    {
      "id": 449,
      "name": "Goodfellas",
      "rating": 8.7
    },
    {
      "id": 450,
      "name": "One Flew Over the Cuckoo's Nest",
      "rating": 8.6
    },
    {
      "id": 451,
      "name": "Se7en",
      "rating": 8.6
    },
    {
      "id": 452,
      "name": "Seven Samurai",
      "rating": 8.6
    },
    {
      "id": 453,
      "name": "It's a Wonderful Life",
      "rating": 8.6
    },
    {
      "id": 454,
      "name": "The Silence of the Lambs",
      "rating": 8.6
    },
    {
      "id": 455,
      "name": "City of God",
      "rating": 8.6
    },
    {
      "id": 456,
      "name": "Saving Private Ryan",
      "rating": 8.6
    },
    {
      "id": 457,
      "name": "Life Is Beautiful",
      "rating": 8.6
    },
    {
      "id": 458,
      "name": "Interstellar",
      "rating": 8.6
    }
  ]
}
