#!/usr/bin/env python3
""" 9-main """
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

from pymongo import MongoClient


if __name__ == "__main__":
    """ A python script that inserts a new document in a collection based on kwargs """
    client = MongoClient()
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCFS", address="505 Parnassus street")
    print("New school created: {}".format(new_school_id.get('_id')))

    schools = list_all(school_collection)
    for school in schools:
        print("[()] {} {}".format(school.get('_id'), school.get('name'), school.get('address')))
