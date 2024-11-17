# Chat App

This is a simple chat application built with Python, utilizing FastAPI as the web server, JWT (JSON Web Token) for authentication, and MongoDB as the database. The app allows users to sign up, log in, and engage in real-time chat with others in the app.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Environment Variables](#environment-variables)
    - [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- **User Authentication**: Sign up and log in with JWT-based authentication.
- **Real-Time Chat**: Engage in real-time messaging with other users.
- **MongoDB Integration**: Stores user and message data in a MongoDB database.

## Technologies

- **Python** - Main programming language.
- **FastAPI** - Framework for building the server and API endpoints.
- **JWT (JSON Web Token)** - For secure authentication and authorization.
- **MongoDB** - NoSQL database for storing user and chat data.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- MongoDB (Local or MongoDB Atlas)
- pip (Python package manager)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/chat-app.git
    cd chat-app_py
    ```

2. Create a virtual environment:

    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

Update the values
- For MongoDB connection:
    - `MONGO_URI`: in database > settings.py
    - `DATA_BASE`: in database > settings.py

- For JWT
    - `SECRET_KEY`: in security > helper.py
    - `ALGORITHM`: in security > helper.py

### Running the Server

    ```bash
    python3  main.py
    ```
server will be running on http://localhost:7777/

## API Endpoints
API documentation can be found at http://localhost:7777/docs

## License
MIT License