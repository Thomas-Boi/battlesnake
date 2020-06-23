from flask import g
from redis import Redis
import os
from urllib.parse import urlparse


def get_redis() -> Redis:
    """
    Get a Redis connection. If one is not available in the
    request, create one.
    :precondition: the redis server must be live.
    :return: a redis client.
    """
    if "redis" not in g:
        url = os.getenv("REDISCLOUD_URL")
        if url is None:
            # get the info for dev env
            host = os.getenv("REDIS_HOST")
            port = os.getenv("REDIS_PORT")
            g.redis = Redis(host=host, port=port)
        else:
            parsed_url = urlparse(url)
            g.redis = Redis(host=parsed_url.host, port=parsed_url.port,
                            username=parsed_url.username,
                            password=parsed_url.password)
    return g.redis
