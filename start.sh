# start redis
sudo docker run \
    -d \
    --name redis \
    dockerfile/redis

# start memcached
sudo docker run \
    -d \
    --name memcached \
    ehazlett/memcache

# start postgres
sudo docker run \
    -d \
    --name="postgresql" \
    -e USER="some_random_username" \
    -e PASS="some_random_string" \
    -e DB="test_app" \
    paintedfox/postgresql

# start app server
sudo docker run \
    -d \
    -p 80:80 \
    --link redis:redis \
    --link memcached:memcached \
    --link postgresql:postgresql \
    --name webapp \
    cburmeister/test_app:latest
