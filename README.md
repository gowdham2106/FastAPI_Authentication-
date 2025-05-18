# FastAPI Project

## Overview  
This project is a RESTful API built with FastAPI that includes user authentication using JWT tokens, password hashing, and database interaction with SQLAlchemy. The project follows a modular structure with routers, repositories, and schemas for clean code organization.

## Features  
- User registration and authentication with OAuth2 and JWT  
- Password hashing and verification  
- CRUD operations using SQLAlchemy models  
- Organized routers for different API endpoints  
- SQLite database for storage

## Project Structure  

project-root/
│
├── repository/
│   ├── blog.py
│   ├── user.py
│
├── routers/
│   ├── __init__.py
│   ├── authentication.py
│   ├── blog.py
│   ├── user.py
│   ├── __init__.py
│
├── blog.db
├── database.py
├── hassing.py
├── JWTtoken.py
├── main.py
├── models.py
├── oauth2.py
├── requirements.txt
├── schemas.py




## Installation

1. Clone the repository  
git clone <your-repo-url>
cd <your-project-folder>

2.Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows

3.Install dependencies
pip install -r requirements.txt

4.Run the application
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000

Usage
Access API docs at http://127.0.0.1:8000/docs
Register users, login to get JWT tokens, and perform authenticated requests


