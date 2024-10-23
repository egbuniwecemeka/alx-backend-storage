#!/usr/bin/env python3
""" A script that establishes a connection to a default MongoDB database"""

import pprint
from pymongo import MongoClient

# Specify host name, port etc as parameters
client = MongoClient(host="localhost", port=27017)

# MongoDB URI format
# client = MongoClient("mongodb://localhost:27017")
print(client)

# Once connected, any database within it can be specified.
# This assumes that school is a database.
# If it doesn't exist, MongoDB creates it after perform it's first operation
db = client.my_db
# db = client['school'] - Handy when database name is not a valid Python identifier

# Insertion. Before insertion into database, create documents to insert
# Documents in python are stored using dictionaries
language1 = {
    "name": "Python",
    "e-hub": "ALX",
    "stage": "Specialization",
    "months": 3
}

language2 = {
    "name": "NoSQL",
    "e-hub": "ALX",
    "stage": "Specialization",
    "months": 3
}

language3 = {
    "name": "JavaScript",
    "e-hub": "ALX",
    "stage": "Specialization",
    "months": 3
}

# Specify collection (school) to insert or add document (language1)
lang = db.school

# Insertion, use insert_one for single document (language1) and insert_many for multiple docs
result = lang.insert_many([language1, language2, language3])

# Print returned InsertOneResult or InsertManyResult object
# print(result)

# Retrieve documents from a collection using find
for res in lang.find():
    pprint.pprint(res)  # pprint is for pretty print that is user friendly

# Retrieve a single document using find_one()
fav_lang = lang.find_one({"name": "JavaScript"})
print()
pprint.pprint(f"{fav_lang}")