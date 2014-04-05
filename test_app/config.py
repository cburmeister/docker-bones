import os

POSTGRES_HOST = os.environ['POSTGRESQL_PORT_5432_TCP_ADDR']
POSTGRES_PORT = os.environ['POSTGRESQL_PORT_5432_TCP_PORT']
POSTGRES_USER = os.environ['POSTGRESQL_ENV_USER']
POSTGRES_PASS = os.environ['POSTGRESQL_ENV_PASS']
POSTGRES_DB = os.environ['POSTGRESQL_ENV_DB']

SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
    POSTGRES_USER,
    POSTGRES_PASS,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB
)

REDIS_HOST = os.environ['REDIS_PORT_6379_TCP_ADDR']
REDIS_PORT = os.environ['REDIS_PORT_6379_TCP_PORT']

CACHE_HOST = os.environ['MEMCACHED_PORT_11211_TCP_ADDR']
CACHE_PORT = os.environ['MEMCACHED_PORT_11211_TCP_PORT']