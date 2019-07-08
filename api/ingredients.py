import re
import string

class Ingredient:
    """The ingredient class holds business rules for ingredient management
    """

    @staticmethod
    def sanitize(ingredient):
        """Sanitizes the input json for an ingredient recipe
        >>> Ingredient.sanitize({'name': 'Egg Whites', 'qty': 12, 'unit': ''})
        {'name': 'egg whites', 'qty': 12.0, 'unit': None}
        >>> Ingredient.sanitize({'name': 'Butter', 'qty': '120.4', 'unit': 'g'})
        {'name': 'butter', 'qty': 120.4, 'unit': 'g'}
        >>> Ingredient.sanitize({'name': 'salt', 'qty': '', 'unit': 'pinch'})
        {'name': 'salt', 'qty': None, 'unit': 'pinch'}
        """
        val = dict()

        name = ingredient['name']
        assert len(name) > 0

        qty = ingredient['qty']
        if qty is '':
            qty = None
        else:
            qty = float(qty)

        unit = ingredient['unit']
        if len(unit) == 0:
            unit = None

        val['name'] = name.lower()
        val['qty'] = qty
        val['unit'] = unit

        return val 

class Ingredients:
    """The ingredients class is a list of ingredients. By wrapping it up as a class, we can perform
    a variety of cool tricks on the set
    """

    @staticmethod
    def sanitize(ingredients):
        return [Ingredient.sanitize(i) for i in ingredients]
