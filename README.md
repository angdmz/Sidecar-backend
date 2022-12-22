# Sidecar-backend
### Admin credentials


```
user: admin
pass: Clave123!
```


### How to run
You can edit some of the envs used in docker-compose and in the application in .env file

```
docker-compose up -d db
docker-compose up -d migrations
docker-compose up -d fixtures
docker-compose up -d sidecar
```