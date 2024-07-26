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