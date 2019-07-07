import re, string

def make_recipe_id(recipe_name):
    """Creates a unique recipe ID from the recipe name
    Note that the max ID size is 24 char
    >>> make_recipe_id("Maria's Yellow Sponge Cake")
    'marias_yellow_sponge_cak'
    >>> make_recipe_id('Panettone Di Verona')
    'panettone_di_verona'
    >>> make_recipe_id('0123456789abcdef0123456789abcdef')
    '0123456789abcdef01234567'
    """

    return make_recipe_tag(recipe_name)[:24]

def make_recipe_tag(recipe_name):
    """Creates a db tag from the recipe name
    >>> make_recipe_tag("Maria's Yellow Sponge Cake")
    'marias_yellow_sponge_cake'
    >>> make_recipe_tag('Panettone Di Verona')
    'panettone_di_verona'
    >>> make_recipe_tag('0123456789abcdef0123456789abcdef')
    '0123456789abcdef0123456789abcdef'
    """

    recipe_name = recipe_name.lower().replace(' ', '_')
    return re.sub(r'\W+', '', recipe_name)
