from flask import g
from redis import Redis


def get_redis():
    if "redis" not in g:
        g.redis = Redis()
    return g.redis
