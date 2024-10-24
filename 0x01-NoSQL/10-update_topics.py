#!/usr/bin/env python3
""" A python script that changes all topics of a document based on the name """

from typing import List

def update_topics(mongo_collection, name: str, topics: List):
    """ Updates topics of the school documents """
    if mongo_collection != None:
        # Use update_many to update multiple documents where name match
        mongo_collection.update_many(
        { 'name': name},
        { '$set': {'topics': topics}}
        )
