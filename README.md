# Acelera Dev - Python - Stone

## Description
    The main objective of this project is to create an aplicantion for registration of vendor catalogues.

## Requirements and Resources Used.

### Computer

    Hp pavilion I5 4G RAM.

### Operational System

    Ubuntu 18.04 LTS.

### IDLE

    VsCode 1.46.1

### Main Stack
    
    Python 3.6.9

### Libraries

    django
    djangorestframework
    dj-database-url
    dj-static
    python-decouple

## How to developer?

    1. Clone the repository
    2. Create a virtualenv
    3. Active o virtualenv
    4. Install the dependencies.
    5. Configure the instance with .env
    6. Run secret_gen.py
    7. On file .venv, replace secret key generated into variable SECRET_KEY=<SECRET_KEY>
    8. Run migrations


```console
git clone https://github.com/Leonardoperrella/central-error stone
cd stone
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
cd contrib
python secret_gen.py
cd ..
python manage.py migrate
```
### URLS WEB
```
|-----------------------------------------------|
| Description           | URLS                  |
|-----------------------------------------------|
| Home                  | /                     |
| Register User         | /register/            |
| Login                 | /login/               |
| LogOut                | /logout/              |
| Admin                 | /admin/               |
| Error Create          | /create/              |
| Error Detail          | /detail/{id}/         |      
| Error Update          | /update/{id}/         |
| Error Delete Section  | /delete-error-section/|
|-----------------------------------------------|
```

### EndPoints and Verbs API

```
|---------------------------------------|
| EndPoints         | Verbs             |
|---------------------------------------|
| api/token/        | POST              |
| api/users/        | GET, POST         |
| api/users/{id}/   | GET, PUT, DELETE  |
| api/errors/       | GET, POST         |
| api/errors/{id}/  | GET, PUT, DELETE  |
|---------------------------------------|
```