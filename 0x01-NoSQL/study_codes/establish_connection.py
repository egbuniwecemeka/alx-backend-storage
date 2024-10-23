#!/usr/bin/env python3
""" A script that establishes a connection to a default MongoDB database"""

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

# Specify collection (school) to insert or add document (language1)
lang = db.school

result = lang.insert_one(language1)
print(result)