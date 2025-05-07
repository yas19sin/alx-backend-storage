#!/usr/bin/env python3
"""
Module for sorting students by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    Args:
        mongo_collection: The MongoDB collection object
    Returns:
        List of students sorted by average score (descending)
    """
    # Use the MongoDB aggregation pipeline
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
