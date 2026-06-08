# Backend SaaS

Modern Backend SaaS with FastAPI, PostgreSQL, JWT Authentication and Clean Architecture.

## Features

* User CRUD operations
* PostgreSQL integration
* SQLAlchemy ORM
* Pydantic validation
* JWT Authentication
* Password hashing with Argon2
* Clean Architecture
* REST API documentation with Swagger

## Tech Stack

* Python 3.14
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT
* Argon2
* Uvicorn

## Project Structure

```text
app/
├── core/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
└── main.py
```

## Run Locally

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

## API Documentation

```text
http://localhost:8000/docs
```

## Status

🚧 Currently under development.

Planned features:

* Role-based access control
* File uploads
* Docker support
* Alembic migrations
* Automated tests
* Cloud deployment
* WebSockets
* Background tasks
