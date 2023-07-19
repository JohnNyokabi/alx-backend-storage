#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker"""
import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """
    count number of times a particular URL was accessed in the key
    """
    r.set(f"cached:{url}", count)
    response = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
