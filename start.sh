#!/bin/bash

# fetch docker containers
docker pull paintedfox/postgresql
docker pull dockerfile/redis
docker pull ehazlett/memcached

# build app container
docker build -t $USER/test_app .

# start redis container
docker run \
    -d \
    --name redis \
    dockerfile/redis

# start memcached container
docker run \
    -d \
    --name memcached \
    ehazlett/memcached

# start postgres container
docker run \
    -d \
    --name="postgresql" \
    -e USER="some_random_username" \
    -e PASS="some_random_string" \
    -e DB="test_app" \
    paintedfox/postgresql

# start app server
docker run \
    -d \
    -p 5000 \
    --link redis:redis \
    --link memcached:memcached \
    --link postgresql:postgresql \
    --name webapp \
    $USER/test_app:latest
