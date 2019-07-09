from api.ingredients import Ingredients

class Stage:
    """The recipe stage is a set of ingredients and steps that contribute towards
    a recipe. This is a separate class that can enforce business rules.
    """

    @staticmethod
    def sanitize(rid, stage_prototype):
        """Sanitizes the input json for a stage
        >>> Stage.sanitize('rid', {'f': 'f', 'name': 'abc', 'index': 1, 'notes': 'abc', 'steps': ['a', 'b', 'c'], 'ingredients': [{'name': 'biga', 'qty': '', 'unit': ''}]})
        ('rid.1', {'sid': 'rid.1', 'name': 'abc', 'notes': 'abc', 'steps': ['a', 'b', 'c'], 'ingredients': [{'name': 'biga', 'qty': None, 'unit': None}]})
        """
        stage = dict()

        sid = "%s.%d" % (rid, stage_prototype['index'])
        stage['sid'] = sid
        stage['name'] = stage_prototype['name'].lower()
        stage['notes'] = stage_prototype['notes']
        stage['steps'] = stage_prototype['steps']
        stage['ingredients'] = Ingredients.sanitize(stage_prototype['ingredients'])

        return sid, stage


