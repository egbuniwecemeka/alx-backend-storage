#!/usr/bin/env python3
""" A python script with a function that inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ Function inserts a document into a collection """
    result = []
    if mongo_collection != None:
        for key, value in kwargs.items():
            result = mongo_collection.get('_id')
    else:
        return
    return result
