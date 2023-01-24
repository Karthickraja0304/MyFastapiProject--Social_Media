# MyFastapiProject-Social_Media
Social media application which helps user to create an account and login into it, share thoughts through social media posts and also vote on the other user's posts. This is a FastAPI based application

## Features:
* Create, Login, Search user account
* Create, Read, Update, Delete posts
* Add or Remove Vote for a particular post
* JWT Authentication
* Object Relational Mapper (ORM) - SQLAlchemy for interacting with PostgreSQL database
* Pydantic models for definition of schema
* Alembic for Data Migration

## Path operations:
#### USER:
* Create/Register a user

        POST:/users

* Search a user with user_id

        GET:/users/{id}

* Login user

        POST:/login

#### POSTS:
* Create a new post

        POST:/posts

* Read all posts

        GET:/posts

* Read a specific post with help of post id

        GET:/posts/{id}

* Update a specific post with help of post id

        PUT:/posts/{id}

* Delete a specific post with help of post id

        DELETE:/posts/{id}

* Voting a post

        POST:/votes


create your .env file and it should contain as follows:

DATABASE_HOSTNAME= Hostname of Database

DATABASE_PORT= Port of Database

DATABASE_PASSWORD= Password of Database

DATABASE_NAME= Name of Database

DATABASE_USERNAME= Username of Database

WEB_TOKEN_SECRET_KEY = Run "openssl rand -hex32" gives randomly generated secret key

WEB_TOKEN_ALGORITHM = HS256

WEB_TOKEN_EXPIRATION_TIME = Set token expiration time (in terms of minutes)
