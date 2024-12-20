# 🎬 FastAPI Movie Management System 🎬

Welcome to the **FastAPI Movie Management System**! 🚀

This project is a simple **FastAPI** application designed to manage a collection of movies. It allows you to **create**, **read**, **update**, and **delete** movie records. The movie data is stored in memory (in the `Movies` list), making it a great choice for development and testing purposes. 

Whether you're building a small movie catalog or learning how to use FastAPI, this project has you covered!

---

## 📋 Features

✨ This API allows you to:

- **Create a Movie**: Add a new movie to the collection.
- **Read All Movies**: Retrieve a list of all movies in the system.
- **Delete a Movie**: Remove a movie from the collection by its unique `id`.
- **Update a Movie**: Modify an existing movie's details using its `id`.

---

## ⚙️ Requirements

To run this application, you'll need the following:

- **Python 3.7+** 🐍
- **FastAPI** 🌐
- **Uvicorn** (ASGI server for FastAPI) 🚀

---

## 🛠️ Installation

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fast-api.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd fast-api
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. **Install  `FastAPI` and `Uvicorn` manually:
    ```bash
    pip install fastapi uvicorn
    ```

---

## 🚀 Running the Application

To start the FastAPI server, run:

```bash
uvicorn Movie:app --port 8080
