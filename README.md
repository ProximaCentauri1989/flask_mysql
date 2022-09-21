# flask_mysql

This is a working skeleton for SQL migration under Flask web server.

## Run solution

Solution contains web server and mysql database.

Run composition as shown below:

```
docker-compose up "$@"
```

## Migrations
To manage migrations you need to operate inside docker container with webserver

1. Go to docker container:

Search for containers
```
docker ps
```

Copy hash of 'flask_mysql_app' and run:

```
docker exec -it <hash>
```

2. Initialize migrations (only once)

```
flask db init
```
This step creates migrations folder which contains versions (migration files)

3. Generate versions form source code

```
flask db migrate
```

This step will generate *.py file with upgrade() and downgrade() methods

4. Run migrations

```
flask db upgrade or flask db downgrade
```





