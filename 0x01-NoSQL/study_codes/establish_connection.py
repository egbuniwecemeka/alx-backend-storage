#!/usr/bin/env python3
""" A script that establishes a connection to a MongoDB database"""

from pymongo import MongoClient

client = MongoClient()
print(client)