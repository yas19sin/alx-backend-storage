#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection
    Args:
        mongo_collection: The MongoDB collection object
    Returns:
        A list of all documents in the collection or an empty list if no documents
    """
    if mongo_collection is not None:
        return list(mongo_collection.find())
    return []