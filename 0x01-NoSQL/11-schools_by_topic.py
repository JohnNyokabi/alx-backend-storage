#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of school"""
    query = {"topics": topic}
    schools = list(mongo_collection.find(query))
    return schools
