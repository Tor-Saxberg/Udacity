def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = []
    pipeline.append({'$match':{    'user.time_zone':'Brasilia',
                                   'user.statuses_count':{'$gte':100} }})
    pipeline.append({'$project':{   'screen_name':'$user.name',
                                    "_id" : 0,
                                    'tweets':'$user.statuses_count',
                                    'followers':'$user.followers_count'}})
    pipeline.append({'$sort':{'followers':-1}})
    pipeline.append({'$limit':1})

    return pipeline

def aggregate(db, pipeline):
    agg = db.tweets.aggregate(pipeline)
    print type(agg)
    return [doc for doc in agg]


if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    assert len(result) == 1
    assert result[0]["followers"] == 17209

