def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # find the average regional city population for all countries in the cities collection
    # _id fields in group stages need not be single values. They can
    # also be compound keys (documents composed of multiple fields)
    pipeline = [
                {'$unwind':'$isPartOf'},
                {'$group': {'_id': {'isPartOf':'$isPartOf','country':'$country'}, 
                            'City Average': {'$avg':'$population'}}},
                #{'$project': {'_id':1, 'City Average':1, 'country':1} }
                {'$group': {'_id':'$_id.country', 'avgRegionalPopulation': {'$avg':'$City Average'} }}
               ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
   db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result) < 150:
        pprint.pprint(result)
    else:
        pprint.pprint(result[:100])
    key_pop = 0
    for country in result:
        if country["_id"] == 'Lithuania':
            assert country["_id"] == 'Lithuania'
            assert abs(country["avgRegionalPopulation"] - 14750.784447977203) < 1e-10
            key_pop = country["avgRegionalPopulation"]
    assert {'_id': 'Lithuania', 'avgRegionalPopulation': key_pop} in result
