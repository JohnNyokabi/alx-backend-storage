# 0x02. Redis Basic

## Requirements
        * Ubuntu 18.04LTS
        * Redis
        * Python3
        * pycodestyle
        * vim/vi/emacs

## Task
    | Task | Details |
    | ---- | ------- |
    | 0. Writing strings to Redis | Cache class in the `__init__` method that stores an instance of the Redis client as a private variable `named _redis` and flush the instance using `flushdb` |
    | 1. Reading from Redis and recovering original type | a get method that take a key string argument and an optional Callable argument named `fn` |
    | 2. Incrementing values | system that counts how many times methods of the Cache class are called |
    | 3. Storing lists |  a `call_history` decorator to store the history of inputs and outputs for a particular function |
    | 4. Retrieving lists |  a `replay` function to display the history of calls of a particular function |
    | Implementing an expiring web cache and tracker |  uses the requests module to obtain the HTML content of a particular URL and returns it |