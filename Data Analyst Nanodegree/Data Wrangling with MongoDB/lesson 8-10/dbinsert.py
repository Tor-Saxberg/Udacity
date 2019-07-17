"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json

if __name__ == "__main__":
    
    from pymongo import MongoClient
    # client = MongoClient("mongodb://localhost:27017")
    client = MongoClient()
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
		db.arachnid.insert(data)
        print db.arachnid.find_one()
