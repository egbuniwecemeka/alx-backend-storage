#!/usr/bin/env python3
""" A python script that creates a Cache class """

from typing import Union, Callable, Any
import redis
import uuid
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """ A decorator that increments count every time method is called """
    count_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Key count is based on method type """
        # Increments the count in Redis
        self._redis.incr(count_key)

        # Call the originaaal method
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ A Cache class that interacts with redis database """
    def __init__(self):
        """ Initialize the Redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key using uuid """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Callable[[bytes], Any] = None) -> Any:
        """Retrieve data from redis and apply optional conversion function """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
        
    def get_str(self, key: str) -> Union[str, None]:
        """ Retrieve a string from Redis """
        return self.get(key, lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Union[int, None]:
        """ Retrieves an integer from Redis """
        return self.get(key, int)