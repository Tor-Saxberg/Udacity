def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # What is the average city population for a region in India?
    pipeline = [{'$match':{'country':'India'} },
                {'$unwind':'$isPartOf'},
                {'$group': {'_id':'$isPartOf',
                            'City Average': {'$avg':'$population'} }},
                {'$group': {'_id':'India Regional Average',
                            'avg': {'$avg':'$City Average'} }}]

    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result) == 1
    # Your result should be close to the value after the minus sign.
    assert abs(result[0]["avg"] - 201128.0241546919) < 10 ** -8
    import pprint
    pprint.pprint(result)
