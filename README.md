# A simple CRUD operations microservices built using FastAPI

- The project can be used as an example to learn how to build a web API using FastAPI and PostgreSQL.
- To learn how to write unit and integration tests for a web API.
- As an Exploratory tester, understand what is covered in automated checks and do exploratory tests.

## Technology stack
- Python 3.8
  - FastAPI
  - Pytest
  - Poetry

## How to install the project locally

The project dependencies are maintained by poetry, so install [poetry](https://python-poetry.org/docs/)

### STEP 1: Clone the repo

```shell
git clone https://github.com/dhanasekars/simple-crud-microservices.git 
```

#### STEP 2  

Navigate to your project directory using the 'cd' command.

#### STEP 3: Install Poetry

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

#### STEP 4: Install dependencies using Poetry

```shell
poetry install
```

#### STEP 5: Run the microservices server  

``` shell
poetry run python main.py
```

This will run the server at [http://127.0.0.1:8000](http://127.0.0.1:8000)

To understand the endpoints, look at the swagger file [docs](http://127.0.0.1:8000/docs).

or  

You can use the requirements.txt present in the project.  

> :warning: **If you are using requirements.txt**: It may not get updated reqularly.  

## Docker  

You can run the Docker file to create a container.  
> :warning: **Do port mapping to <your_prefered_port>:8000**.  

## Makefile

You can make use of Makefile to run run tests and linting 
