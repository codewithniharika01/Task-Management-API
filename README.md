# Smart Task Manager API 🚀

A secure Task Management REST API built using FastAPI with JWT Authentication and SQLAlchemy ORM.

## 🌟 Features

- User Registration
- User Login with JWT Authentication
- Password Hashing using bcrypt
- Create Tasks
- Get All Tasks
- Get Single Task
- Update Tasks
- Delete Tasks
- User-specific Task Management
- RESTful API Design

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic
- Uvicorn
- Railway Deployment

## 📂 Project Structure
app/
│
├── main.py
├── auth.py
├── crud.py
├── database.py
│
├── models/
├── schemas/
└── routers/

## 🔐 Authentication Flow

1. User registers account
2. Password is securely hashed
3. User logs in
4. JWT token is generated
5. Token is used to access protected APIs

## 📌 API Endpoints

### Authentication

| Method | Endpoint |
|---|---|
| POST | /register |
| POST | /login |

### Tasks

| Method | Endpoint |
|---|---|
| GET | /tasks |
| POST | /tasks |
| GET | /tasks/{task_id} |
| PUT | /tasks/{task_id} |
| DELETE | /tasks/{task_id} |

## 🌐 Deployment

Live API:
https://vibrant-dedication-production-5393.up.railway.app

Swagger Documentation:

/docs

## 👩‍💻 Author

Niharika
