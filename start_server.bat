set FLASK_APP=battlesnake
set FLASK_ENV=development
set REDIS_HOST=localhost
set REDIS_PORT=6379
docker start redis
flask run
