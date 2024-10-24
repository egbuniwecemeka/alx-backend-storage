#!/usr/bin/env python3
""" A python script that returns a list from a document with a specific key """

from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List:
    """ Returns the list of school having specific topic """
    if mongo_collection != None:
        return list(mongo_collection.find({"topics": topic}))
    else:
        return []
