from api.storage import AmbrosiaStorage
from api.recipe import Recipe
from api.stage import Stage


def get_recipes(storage, tags):
    assert isinstance(storage, AmbrosiaStorage)
    return storage.get_recipe_headers(tags)

def get_recipe(storage, rid):
    assert isinstance(storage, AmbrosiaStorage)
    return storage.get_recipe(rid)

def add_recipe(storage, recipe_header):
    assert isinstance(storage, AmbrosiaStorage)
    rid, recipe_header = Recipe.sanitize_header(recipe_header)
    storage.create_new_recipe(recipe_header)
    return rid

def add_stage(storage, rid, stage):
    assert isinstance(storage, AmbrosiaStorage)
    sid, stage = Stage.sanitize(rid, stage)
    storage.add_stage(stage)
    return sid
