import re
import string


class Recipe:
    """The recipe class holds any business rules for recipe management
    """

    @staticmethod
    def sanitize_header(recipe_header):
        """Sanitizes the input json for a recipe header
        >>> Recipe.sanitize_header({'name': 'Marias Cake', 'tags': ['a', 'F', 'a'], 'author': 'a', 'notes': 'n'})[1]
        {'name': 'Marias Cake', 'tags': ['a', 'f', 'marias_cake'], 'author': 'a', 'notes': 'n', '_id': 'marias_cake'}
        """
        recipe_name = recipe_header['name']
        tags = recipe_header['tags']

        assert len(recipe_name) > 0
        if tags is None:
            tags = []

        recipe_tag_name = Recipe.make_tag(recipe_name)
        tags.append(recipe_tag_name)

        rid = Recipe.make_id(recipe_name)
        recipe_header['_id'] = rid
        recipe_header['tags'] = Recipe.sanitize_tags(tags)

        return rid, recipe_header

    @staticmethod
    def sanitize_tags(tags):
        """Sanitizes an array of input tags to be a set. A set is defined as
        all lower case, no spaces
        >>> Recipe.sanitize_tags(['a', 'F'])
        ['a', 'f']
        >>> Recipe.sanitize_tags(['a', 'F', 'a', 'duck_hunt', 'Duck Hunt'])
        ['a', 'duck_hunt', 'f']
        """

        tags = [Recipe.make_tag(t) for t in tags]
        return sorted(list(set(tags)))

    @staticmethod
    def make_id(recipe_name):
        """Creates a unique recipe ID from the recipe name
        Note that the max ID size is 24 char
        >>> Recipe.make_id("Maria's Yellow Sponge Cake")
        'marias_yellow_sponge_cak'
        >>> Recipe.make_id('Panettone Di Verona')
        'panettone_di_verona'
        >>> Recipe.make_id('0123456789abcdef0123456789abcdef')
        '0123456789abcdef01234567'
        """

        return Recipe.make_tag(recipe_name)[:24]

    @staticmethod
    def make_tag(recipe_name):
        """Creates a db tag from the recipe name
        >>> Recipe.make_tag("Maria's Yellow Sponge Cake")
        'marias_yellow_sponge_cake'
        >>> Recipe.make_tag('Panettone Di Verona')
        'panettone_di_verona'
        >>> Recipe.make_tag('0123456789abcdef0123456789abcdef')
        '0123456789abcdef0123456789abcdef'
        """

        recipe_name = recipe_name.lower().replace(' ', '_')
        return re.sub(r'\W+', '', recipe_name)
