#!/usr/bin/env python3
"""
Module for finding schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    Args:
        mongo_collection: The MongoDB collection object
        topic: The topic to search for
    Returns:
        The list of schools having the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
