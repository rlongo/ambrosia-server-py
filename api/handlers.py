from api.storage import AmbrosiaStorage
from api.recipe import Recipe


def get_recipes(storage, headers_only, tags):
    assert isinstance(storage, AmbrosiaStorage)
    return storage.get_recipe_headers(tags)


def add_recipe(storage, recipe_header):
    assert isinstance(storage, AmbrosiaStorage)
    rid, recipe_header = Recipe.sanitize_header(recipe_header)
    storage.create_new_recipe(recipe_header)
    return rid
