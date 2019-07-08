from pymongo import MongoClient


class AmbrosiaStorage:
    def __init__(self, db_uri, db_name, collection_name):
        assert isinstance(db_uri, str)
        assert isinstance(db_name, str)
        assert isinstance(collection_name, str)

        self.mongo = MongoClient(db_uri)
        self.db = self.mongo.ambrosia
        self.collection = self.db.recipes

    def create_new_recipe(self, recipe):
        recipe['_id'] = recipe['rid']
        return self.collection.insert_one(recipe).inserted_id

    @staticmethod
    def _get_tags_query(tags):
        if tags is None or len(tags) is 0:
            return {}
        return {"tags": {"$all": tags}}

    def get_recipe_headers(self, tags):
        headers = []
        tag_filter = AmbrosiaStorage._get_tags_query(tags)
        print(tag_filter)
        for h in self.collection.find(tag_filter):
            h.pop('_id', None)
            headers.append(h)

        return headers
