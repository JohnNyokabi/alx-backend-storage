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

    ip_pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]
    top_ips = collection.aggregate(ip_pipeline)

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check} status check")
    print("IPs:")
    for ip_doc in top_ips:
        ip = ip_doc["_id"]
        count = ip_doc["count"]
        print(f"    {ip}: {count}")


if __name__ == "__main__":
    log_stats()
