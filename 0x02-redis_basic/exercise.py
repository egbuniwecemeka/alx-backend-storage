#!/usr/bin/env python3
""" A python script that creates a Cache class """

from typing import Union
import redis
import uuid


class Cache:
    """ A Cache class that interacts with redis database """
    def __init__(self):
        """ Initialize the Redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key using uuid """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
