# FastAPI Student Records Simple CRUD API

This is a simple API built using FastAPI to manage student records.

## Features

- **Get Student by ID**: Retrieve a student record by their ID.
- **Get All Students**: Retrieve all student records.
- **Get Student by Name**: Retrieve a student record by their name.
- **Create Student**: Create a new student record.
- **Update Student**: Update an existing student record.
- **Delete Student**: Delete an existing student record.

## Documentation

The API is documented using FastAPI's automatic OpenAPI and Swagger UI generation. You can view the documentation by running the server and visiting the `/docs` or `/redoc` endpoints in your browser.

## Setting Up the Project

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd fastapi-student-records
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

```bash
uvicorn main:app --reload
```

## Accessing the API
Once the server is running, you can access the API and its documentation:

API: http://localhost:8000
Documentation (Swagger UI): http://localhost:8000/docs
Documentation (ReDoc): http://localhost:8000/redoc