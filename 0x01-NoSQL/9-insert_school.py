#!/usr/bin/env python3
""" A python script with a function that inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ Function inserts a document into a collection """
    document = {}
    if mongo_collection != None:
        # Manually construct the document to insert into (Optional)
        for key, value in kwargs.items():
            document[key] = value
        new_inserted_id = mongo_collection.insert_one(document)
        return new_inserted_id
    else:
        return None
