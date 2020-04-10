# database.py

import sys, shelve

def store_person(db):
    """
    input data to shelf 
    """
    pid = input('Enter unique ID number:')
    person = {}
    person['name'] = input('Enter name: ')
    person['age']