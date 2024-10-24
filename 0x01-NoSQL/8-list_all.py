#!/usr/bin/env/python3
""" A script that list all documents in a collection """


def list_all(mongo_collection):
    """ List all documents in mongo_collection """
    result = []
    if mongo_collection is None:
        result
    else:
        result = mongo_collection.find()
    return result