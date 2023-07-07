# django-basic-todo

## Installation

Required Python 3.10

```bash
  python -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
```
Create Superuser
```bash
  python manage.py migrate
  python manage.py createsuperuser
```
Generate fake data
```bash
  python manage.py importtodos
```

Run server
```bash
  python manage.py runserver
```

    