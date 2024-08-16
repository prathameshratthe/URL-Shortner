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
