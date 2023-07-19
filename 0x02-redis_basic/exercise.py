#!/usr/bin/env python3
""" Redis-python basics"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional, Any


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    input_list_key = "{}:inputs".format(method.__qualname__)
    output_list_key = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args):
        input_str = str(args)
        self._redis.rpush(input_list_key, input_str)

        output = method(self, *args)
        self._redis.rpush(output_list_key, output)

        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """counts number of times Cache class method is called """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Stores an instance of redis client private variable"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a random generated key during storage of data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)


def replay(method: Callable):
    """display the history of calls of a particular function"""
    key = method.__qualname__
    input_list_key = key + ":inputs"
    output_list_key = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    inputList = redis.lrange(input_list_key, 0, -1)
    outputList = redis.lrange(output_list_key, 0, -1)
    redis_zipped = list(zip(inputList, outputList))
    for a, b in redis_zipped:
        attr, data = a.decode("utf-8"), b.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))
