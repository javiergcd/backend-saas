# Backend SaaS

A modern backend application built with FastAPI, PostgreSQL and Docker.

## Features

* JWT Authentication
* User Management CRUD
* Protected Routes
* File Upload System
* File Validation
* Background Tasks
* WebSocket Communication
* PostgreSQL Integration
* Alembic Migrations
* Environment Variables
* Docker & Docker Compose
* API Testing with Pytest
* Application Logging
* Health Check Endpoint

## Tech Stack

### Backend

* Python 3.14
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL
* Alembic

### Security

* JWT Authentication
* Argon2 Password Hashing

### DevOps

* Docker
* Docker Compose

### Testing

* Pytest
* FastAPI TestClient

## Project Structure
```text
backend-saas/

app/
├── core/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
├── main.py

tests/

uploads/

alembic/
```
## Running Locally

Install dependencies:
```bash
pip install -r requirements.txt
```
Run application:
```bash
uvicorn app.main:app --reload
```
Swagger documentation:
```bash
http://localhost:8000/docs
```
## Docker

Build:
```bash
docker build -t backend-saas .
```
Run:
```bash
docker compose up --build
```
## API Features

Authentication:

* Register
* Login
* JWT Token Validation

Users:

* Create User
* Get Users
* Update User
* Delete User
* Current Authenticated User

Files:

* Upload Files
* File Validation
* Unique File Names

Realtime:

* WebSockets

## Status

Active Development

Next Planned Features:

* Cloud Deployment
* CI/CD Pipeline
* AI Integration
* RAG System
* OpenAI Integration

## Author

Javier Gustavo Corrales Delgadillo<br>
Computer Engineering Student<br>
Backend & AI Developer
