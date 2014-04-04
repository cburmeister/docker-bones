import os
from flask import Flask, jsonify
from redis import StrictRedis
from werkzeug.contrib.cache import MemcachedCache
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

postgres_host = os.environ['POSTGRESQL_PORT_5432_TCP_ADDR']
postgres_port = os.environ['POSTGRESQL_PORT_5432_TCP_PORT']
postgres_user = os.environ['POSTGRESQL_ENV_USER']
postgres_pass = os.environ['POSTGRESQL_ENV_PASS']
postgres_db = os.environ['POSTGRESQL_ENV_DB']

postgres_connection_uri = 'postgresql://%s:%s@%s:%s/%s' % (
    postgres_user,
    postgres_pass,
    postgres_host,
    postgres_port,
    postgres_db
)

app.config['SQLALCHEMY_DATABASE_URI'] = postgres_connection_uri

db = SQLAlchemy(app)

redis_host = os.environ['REDIS_PORT_6379_TCP_ADDR']
redis_port = os.environ['REDIS_PORT_6379_TCP_PORT']

redis = StrictRedis(redis_host, int(redis_port))

cache_host = os.environ['MEMCACHED_PORT_11211_TCP_ADDR']
cache_port = os.environ['MEMCACHED_PORT_11211_TCP_PORT']

cache = MemcachedCache(['%s:%s' % (cache_host, cache_port)])

@app.route('/')
def hello_world():
    return jsonify(
        redis={
            'host': redis_host,
            'port': redis_port,
        },
        memcached={
            'host': cache_host,
            'port': cache_port,
        },
        postgres={
            'host': postgres_host,
            'port': postgres_port,
            'user': postgres_user,
            'pass': postgres_pass,
            'db': postgres_db,
            'uri': postgres_connection_uri,
        },
    )

if __name__ == '__main__':
    app.run()
