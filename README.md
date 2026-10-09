# 02-django-e-commerce-backend

Full-featured e-commerce catalog API built on Django 5.0 and Django REST Framework.

## Features
- Category and Product models with relational mapping
- Paginated REST endpoints with search and ordering filters
- Django ORM schema and admin register ready

## Running the Application
```bash
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
