#!/bin/bash

WEB_PORT=$(docker port webapp 5000 | awk -F: '{ print $2 }')

curl http://127.0.0.1:$WEB_PORT
