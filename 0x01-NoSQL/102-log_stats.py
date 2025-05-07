#!/usr/bin/env python3
"""
Module for providing enhanced stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Provides enhanced stats about Nginx logs in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Count status checks
    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_checks} status check")

    # Get top 10 IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)

    for ip_data in top_ips:
        print(f"    {ip_data.get('_id')}: {ip_data.get('count')}")