# Emily-Rose Steyn OCL Tech Challenge

This is my submission for the OCL tech challenge :) Below you can find instructions for [setup](#setup) as well as
answers/brief notes on the different challenges documented in the [instructions](./instructions.md).

## Setup

**Poetry**

Poetry is used to manage packages and virtual environments. Ensure you have [poetry](https://python-poetry.org/docs/)
installed and then run:

```shell
 poetry shell
```

```shell
 poetry install
```

**Docker**

Ensure you have [docker](https://docs.docker.com/get-docker/) and docker-compose installed. Docker-compose should be
packaged with Docker Desktop. Docker-compose is used to run the PostgreSQL database.

**Running Database**

Once installed, you can run the following to start the docker container with the PostgreSQL database:

```shell
docker-compose -f devops/development/docker-compose.yaml up -d

```

To access the database, you can run:

```shell
docker exec -it <CONTAINER_NAME> psql -U ocl_challenge
```

Where CONTAINER_NAME is the docker service name that shows up for the postgres instance after running `docker ps`.
Eg `development-ocl_db-1`.

**Initialising Database**

**Running Django Server**

To run the Django app, run the following from root:

`python src/manage.py runserver`

## Part 1: Web Scraping and Data Storage

To implement scraping of the 2022 Durban valuations, requests and BeautifulSoup are used. A script is implemented that
can be run from the root directory using Django's base command functionality:

```shell
python src/manage.py scrape_valuations
```

To keep things simple, the data layer is designed to be flat with no relations. Data is also minimally cleaned and typed. However, in a "real" application, the database would be designed to have normalised relations that make sense for the given application and cleaning would be more thorough. 

Additionally, in this case, no second level scraping is done - ie only the returned table is stored and links are not followed in the retrieved tables.

Finally, all data scraped is stored. This is useful for tracking changes. However, a better solution would be to only store unique data.

[//]: # (TODO: Data diagram)

## Part 2: API Development

In order to retrieve data via API, [django-ninja](https://github.com/vitalik/django-ninja) is used which also helps with openapi specifications. The API endpoint is documented at [http://127.0.0.1:8000/valuations/docs](http://127.0.0.1:8000/valuations/docs).

Originally, a "vanilla" django view was used but this proved difficult to document easily. Django ninja seemed like a lightweight alternative for setting up the API endpoint. However, I would prefer to have the api docs fully available at something like /swagger or /docs rather than what seems to be docs per api file (in this case, valuations).

Ideally, a bit more time would have been spent on searching and filtering data and ensuring that duplicates don't get returned from the endpoint. This would be done by querying for latest data by rate number (assuming rate number is what's unique). Unfortunately, didn't have time to get to this.

## Part 3: Deployment Strategy

## Caveats

**Best Practices**

This app is developed as a prototype for a development environment. I would typically be a lot more thorough in
designing and implementing maintainable, reusable, and secure code (e.g. using tailored database design depending on the
use case and ensuring that environment variables are loaded from a git ignored env file rather than exposed in the
repo). However, again, given the time constraint and being away, I chose to rather focus on developing a prototype to
fit the instructions instead of over engineering the solution.

**First Time Django**

This is my first time using Django and given the limited time constraint, I really just tested the waters.
