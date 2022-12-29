# Fastapi mono template

## Techstack:
* Fastapi
* SqlAlchemy
* Mysql
* Typer

## Prerequisite

- Python >= 3.8
- pip >= 20

## Installation

Environment:
 
- Create `.env` from `${root}/app/env.example`


### Manual installation 

    ```
    pip install -r requirements.txt
    ```
    
Change to app directory. at ./app/

if this is the first time you create database schema:

    ```
    alembic revision --autogenerate -m "init"
    alembic upgrade head
    ```

else just run:
    ```
    alembic upgrade head
    ```
finally:
    ```
    uvicorn main:app
    ```
Now try to access in browser.

### manage.py cli

manage.py using typer to run cli.

* generate admin user (default: email: admin@mail.com, password: 123456@abc):

```
    python manage.py user create_admin
```

* run app:

```
    python manage.py run
```

* run autogenerate alembic :

```
    python manage.py alembic generate
```

* run autogenerate alembic :

```
    python manage.py alembic upgrade
```

* run autogenerate alembic :

```
    python manage.py alembic downgrade
```


### Bashell Linting and format code

Froom root of repo, run:

```bash
    scripts/format-imports.sh
```
and
```bash
   scripts/lint.sh
```



### Docker (On dev)
- Install `docker` & `docker-compose`

- Run:
    ```
    docker-compose up -d
    ```

## Testing (On dev)
- To run unit test:


    ```
    python -m pytest tests
    ```


- To run unit test with coverage


    ```
    nosetests -v --with-coverage --cover-html --cover-erase --cover-branch --cover-package=. --cover-min-percentage=80
    ```
