# URL Shortener API

This is a basic URL shortener API built using FastAPI and PostgreSQL. It allows users to shorten long URLs and retrieve the original URL using a short code.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [License](#license)

## Features
- **POST /shorten**: Accept a long URL and return a shortened URL.
- **GET /{short_code}**: Redirect to the original URL based on the short code.

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/url-shortener-api.git
cd url-shortener-api
```

### Step 2: Set Up the Virtual Environment
1. **Create a Virtual Environment**:
   - On macOS/Linux:
     ```bash
     python3 -m venv env
     ```
   - On Windows:
     ```bash
     python -m venv env
     ```

2. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

### Step 3: Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install fastapi[all] uvicorn psycopg2-binary
```

### Step 4: Set Up PostgreSQL
1. **Install PostgreSQL** if you haven't already.
2. **Create a New Database**:
   - Open the PostgreSQL command line or `pgAdmin` and run the following command to create a new database:
     ```sql
     CREATE DATABASE url_shortener;
     ```
3. **Update the Database URL**:
   - Open the `database.py` file and update the `SQLALCHEMY_DATABASE_URL` variable with your PostgreSQL username, password, and the database name you just created:
     ```python
     SQLALCHEMY_DATABASE_URL = "postgresql://your_username:your_password@localhost/url_shortener"
     ```

### Step 5: Run the Migrations (Optional)
If you are using Alembic for migrations, apply them to create the necessary tables in your database:
```bash
alembic upgrade head
```

### Step 6: Start the Server
Launch the FastAPI application using `uvicorn`:
```bash
uvicorn main:app --reload
```
## Usage

### Shorten a URL
1. **Endpoint**: `POST /shorten`
2. **Description**: Accepts a long URL and returns a shortened URL.
3. **Request**:
   - **URL**: `http://127.0.0.1:8000/shorten`
   - **Method**: POST
   - **Headers**: 
     ```plaintext
     Content-Type: application/json
     ```
   - **Body**:
     ```json
     {
       "long_url": "https://example.com"
     }
     ```
4. **Response**:
   - **Status Code**: 200 OK
   - **Body**:
     ```json
     {
       "id": 1,
       "long_url": "https://example.com",
       "short_code": "abc123"
     }
     ```

### Redirect to Original URL
1. **Endpoint**: `GET /{short_code}`
2. **Description**: Redirects to the original URL based on the short code.
3. **Request**:
   - **URL**: `http://127.0.0.1:8000/{short_code}`
   - **Method**: GET
   - **Path Parameter**: 
     - `short_code`: The shortened URL code (e.g., `abc123`)
4. **Response**:
   - **Status Code**: 200 OK
   - **Body**:
     ```json
     {
       "long_url": "https://example.com"
     }
     ```
   - **Redirection**: The request will be redirected to the original long URL.

## API Endpoints

- **POST /shorten**
  - **Description**: Shortens a provided long URL.
  - **Request Body**:
    ```json
    {
      "long_url": "https://example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "long_url": "https://example.com",
      "short_code": "abc123"
    }
    ```

- **GET /{short_code}**
  - **Description**: Retrieves the original long URL based on the short code.
  - **Path Parameter**:
    - `short_code`: The code used to shorten the original URL.
  - **Response**:
    ```json
    {
      "long_url": "https://example.com"
    }
    ```

Created by Prathamesh Ratthe  
[GitHub](https://github.com/prathameshratthe/)
