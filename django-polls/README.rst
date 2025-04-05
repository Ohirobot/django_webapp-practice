django-polls
============

Overview
--------
The `django-polls` app is a simple Django application for creating and managing polls. It allows users to create questions with multiple choices and vote on them. This app is designed as a learning project to understand the basics of Django.

Features:
- Create polls with multiple-choice questions.
- Vote on polls and view results.
- Admin interface for managing polls and choices.

Installation
------------
1. Clone the repository:
    ```
    git clone <repository-url>
    cd django-polls
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```
    python manage.py migrate
    ```

4. Run the development server:
    ```
    python manage.py runserver
    ```

Usage
-----
1. Access the app in your browser at `http://127.0.0.1:8000/`.
2. Use the admin interface to create polls and choices.
3. Share the poll URL with users to collect votes.
4. View the results of the polls in real-time.