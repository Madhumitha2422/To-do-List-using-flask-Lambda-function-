# To-Do Manager using Flask and Python Lambda Functions

This project is a to-do manager web application built with Flask, leveraging Python's `lambda` functions for handling specific operations related to tasks. Users can create, view, update, and delete their to-do tasks using this application.

## Features

- **Create:** Add new tasks to your to-do list.
- **Read:** View all tasks or individual task details.
- **Update:** Modify existing task details.
- **Delete:** Remove tasks from your to-do list.

## Prerequisites

Before setting up and running the application, ensure you have:

- Python 3.x
- Flask (`pip install Flask`)

## Setup

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Implement Python `lambda` functions for task operations:

    - Inside `app.py` or in a separate module, define Python `lambda` functions to handle CRUD operations (create, read, update, delete) for tasks.

3. Integrate Flask with the `lambda` functions:

    - Update the routes and relevant endpoints within the Flask application (`app.py`) to use these `lambda` functions for handling tasks.

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Access the to-do manager web application via the provided URL (typically `http://127.0.0.1:5000`).

3. Perform CRUD operations on your to-do list by adding, viewing, updating, or deleting tasks.

## Additional Notes

- Ensure that the Python `lambda` functions are properly integrated and utilized within the Flask application for task management.
- Customize the app's UI, add authentication, implement search functionality, or integrate with databases for persistent storage.
- Test thoroughly to ensure the `lambda` functions handle tasks as expected and modify them as needed to suit your requirements.

