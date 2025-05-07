#!/usr/bin/env python3
"""
Module for inserting a document in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: The MongoDB collection object
        **kwargs: The key/value pairs of the document to insert
    Returns:
        The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
