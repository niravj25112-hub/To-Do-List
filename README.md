# My To-Do List

A Django web application for managing daily tasks.

## Features

- Add tasks with a title and description.
- View title, description, creation date, and status for every task.
- Edit, delete, and change a task between pending and completed.
- Clear completed and pending status styling, plus an empty-state message.
- CSRF-protected POST forms for all data changes.

## Run locally

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.
