#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """Connect to the MongoDB database"""
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        count = collection.count_documents({"method": method})
        method_counts[method] = count

    status_check = collection.count_documents
    ({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
