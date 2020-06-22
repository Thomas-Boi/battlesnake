from flask import g
from redis import Redis


def get_redis() -> Redis:
    """
    Get a Redis connection. If one is not available in the
    request, create one.
    :precondition: the redis server must be live.
    :return: a redis client.
    """
    if "redis" not in g:
        g.redis = Redis()
    return g.redis
