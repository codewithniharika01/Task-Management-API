<<<<<<< HEAD
# Task Management API 🚀

A backend Task Management API built using FastAPI with JWT Authentication.

## Features

- User Registration
- User Login
- JWT Token Authentication
- Password Hashing using bcrypt
- Create Tasks
- Read Tasks
- Update Tasks
- Delete Tasks
- User-wise Task Management
- Protected APIs

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- Passlib (bcrypt)

## Project Structure
Taskmanagement
│
├── app
│ ├── main.py
│ ├── auth.py
│ ├── crud.py
│ ├── dependencies.py
│ ├── db.py
│ ├── tasks
│ └── user
│
├── requirements.txt
├── .gitignore
└── README.md


## Installation

Clone the repository:

```bash
git clone your-repository-link
..................................

*Create virtual environment:
python -m venv env
...................................

*Activate environment:
*Windows:
env\Scripts\activate
...................................

*Install dependencies:
pip install -r requirements.txt
...................................

*Run Application
uvicorn app.main:app --reload

*API Documentation
*Swagger UI:

http://127.0.0.1:8000/docs
.....................................

Authentication Flow:
*Register user
*Login and get JWT token
*Authorize using Bearer Token
*Access protected task APIs

Future Improvements:
*PostgreSQL Database
*Docker Support
*Cloud Deployment
*Role Based Authentication
=======
# Task-Management-API
>>>>>>> aa71b383725097988de9d91e77f97a2e9d00f8aa
