import pymongo

class AmbrosiaStorage:
    def __init__(self, db_uri, db_name, collection_name):
        assert isinstance(db_uri, str)
        assert isinstance(db_name, str)
        assert isinstance(collection_name, str)

        self.mongo = pymongo.MongoClient(db_uri)
        self.db = self.mongo.ambrosia
        self.collection = self.db.recipes

    def create_new_recipe(self, recipe):
        return self.collection.insert_one(recipe).inserted_id

    def add_stage(self, stage):
        f = {'sid': stage['sid']}
        self.collection.update_one(f, {'$set': stage}, upsert=True)

    @staticmethod
    def _get_tags_query(tags):
        if tags is None or len(tags) is 0:
            return {}
        return {"tags": {"$all": tags}}

    def get_recipe_headers(self, tags):
        headers = []
        tag_filter = AmbrosiaStorage._get_tags_query(tags)
        rid_filter = {'rid': { '$exists': True} }
        f = {'$and': [ tag_filter, rid_filter ]}
        for h in self.collection.find(f):
            h.pop('_id')
            headers.append(h)

        return headers

    def get_recipe(self, rid):
        recipe = self.collection.find_one({'_id': rid})
        if recipe is None:
            return None

        recipe.pop('_id')
        recipe['rid'] = rid

        stages = []
        
        r = "^%s\.\d+" % rid
        stages_filter = {'sid': {'$regex': r}}
        for s in self.collection.find(stages_filter).sort('sid', pymongo.ASCENDING):
            s.pop('_id', None)
            stages.append(s)

        recipe['stages'] = stages

        return recipe
