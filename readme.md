# Emily-Rose Steyn OCL Tech Challenge
This is my submission for the OCL tech challenge :) Below you can find instructions for [setup](#setup) as well as answers/brief notes on the different challenges documented in the [instructions](./instructions.md).

## Setup
**Poetry**

Poetry is used to manage packages and virtual environments. Ensure you have [poetry](https://python-poetry.org/docs/) installed and then run:

```shell
 poetry shell
```

```shell
 poetry install
```

**Docker**

Ensure you have [docker](https://docs.docker.com/get-docker/) and docker-compose installed. Docker-compose should be packaged with Docker Desktop. Docker-compose is used to run the PostgreSQL database.

**Running Database**

Once installed, you can run the following to start the docker container with the PostgreSQL database:
```shell
docker-compose -f devops/development/docker-compose.yaml up -d

```

To access the database, you can run:
```shell
docker exec -it <CONTAINER_NAME> psql -U ocl_challenge
```

Where CONTAINER_NAME is the docker service name that shows up for the postgres instance after running `docker ps`. Eg `development-ocl_db-1`.

**Initialising Database**

## Part 1: Web Scraping and Data Storage

[//]: # (TODO: Data diagram)
[//]: # (TODO: Description of which parts I am leaving out - e.g. not doing second level scraping)

## Part 2: API Development

## Part 3: Deployment Strategy


## Caveats

**First Time Django**

This is my first time using Django and given the limited time constraint, I really just tested the waters. 

**Best Practices**

I would typically be a lot more thorough in designing and implementing maintainable, reusable, and secure code (e.g. using tailored database design depending on the use case and ensuring that environment variables are loaded from a git ignored env file rather than exposed in the repo). However, again, given the time constraint and being away, I chose to rather focus on developing a prototype to fit the instructions instead of over engineering the solution.

# Task List
* Clean data
* Save data - Django
* Init tables django
* Handle duplicates?
* Data diagram
* Description of not doing second level scraping - would need more info to ensure scraping is gathering correct data and in expected format
* Notes on robustness - error handling etc and maintainability
* API to retrieve from db
* Additional descriptions based on api?
* Part 3 deployment strategy