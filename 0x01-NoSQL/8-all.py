#!/usr/bin/env python3
"""function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    documents = list(mongo_collection.find())
    return documents
