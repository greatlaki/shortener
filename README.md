# The shortener is a service for shortening long links

## Getting Started

- If you have pyenv, set a local python 3.11.* version

```
pyenv local 3.11.*  # set python version which was installed before
```

- then install dependencies:

```
poetry install
```

### Using Docker

- Clone the repo

```
git@github.com:greatlaki/shortener.git
```

- Bring up the app

```
docker-compose up -d --build
```

- Perform the migration

```
docker-compose exec web python manage.py migrate
```