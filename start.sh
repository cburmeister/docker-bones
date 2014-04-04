#!/bin/bash

# fetch docker containers
sudo docker pull paintedfox/postgresql
sudo docker pull dockerfile/redis
sudo docker pull ehazlett/memcached

# build app container
sudo docker build -t $USER/test_app .

# start redis container
sudo docker run \
    -d \
    --name redis \
    dockerfile/redis

# start memcached container
sudo docker run \
    -d \
    --name memcached \
    ehazlett/memcached

# start postgres container
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
    $USER/test_app:latest
