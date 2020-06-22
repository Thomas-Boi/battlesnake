from flask import g
from redis import Redis
import os


def get_redis() -> Redis:
    """
    Get a Redis connection. If one is not available in the
    request, create one.
    :precondition: the redis server must be live.
    :return: a redis client.
    """
    if "redis" not in g:
        host = os.getenv("REDIS_HOST")
        port = os.getenv("REDIS_PORT")
        g.redis = Redis(host=host, port=port)
    return g.redis
