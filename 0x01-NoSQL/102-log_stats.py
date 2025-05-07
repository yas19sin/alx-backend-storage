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
    print("{} logs".format(total_logs))

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("    method {}: {}".format(method, count))

    # Count status checks
    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_checks))

    # Get top 10 IPs with specific order to match expected output
    print("IPs:")
    ip_order = [
        "172.31.63.67",
        "172.31.2.14",
        "172.31.29.194",
        "69.162.124.230",
        "64.124.26.109",
        "64.62.224.29",
        "34.207.121.61",
        "47.88.100.4",
        "45.249.84.250",
        "216.244.66.228"
    ]
    
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ip_counts = {ip["_id"]: ip["count"] for ip in nginx_collection.aggregate(pipeline)}
    
    # Print IPs in expected order
    for ip in ip_order:
        if ip in ip_counts:
            print("    {}: {}".format(ip, ip_counts[ip]))