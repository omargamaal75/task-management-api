# Task Management API

A Django REST Framework API for managing tasks with user authentication.

## Features

- User registration and authentication with token-based auth
- CRUD operations for tasks
- Task filtering and sorting
- Mark tasks as complete/incomplete
- Data validation

## Installation

1. Install dependencies: `pip install -r requirements.txt`
2. Create MySQL database named `task_manager_db`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Run server: `python manage.py runserver`

## API Endpoints

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login user
- `GET /api/tasks/` - List all tasks for authenticated user
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task
- `POST /api/tasks/{id}/mark_complete/` - Mark task as complete
- `POST /api/tasks/{id}/mark_incomplete/` - Mark task as incomplete