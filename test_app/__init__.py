from flask import Flask, jsonify
from redis import StrictRedis
from werkzeug.contrib.cache import MemcachedCache
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('test_app.config')

db = SQLAlchemy(app)

redis = StrictRedis(
    app.config['REDIS_HOST'],
    int(app.config['REDIS_PORT'])
)

cache = MemcachedCache(
    ['%s:%s' % (
        app.config['CACHE_HOST'],
        app.config['CACHE_PORT']
    )]
)

@app.route('/')
def hello_world():
    redis.incr('hits')
    return jsonify({
        'hits': redis.get('hits')
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
