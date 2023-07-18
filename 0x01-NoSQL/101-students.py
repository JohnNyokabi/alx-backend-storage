#!/usr/bin/env python
"""
Function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """return all students by average scores"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    students = list(mongo_collection.aggregate(pipeline))
    return students
