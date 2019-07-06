from flask import Blueprint, jsonify, abort

ambrosia_api = Blueprint('ambrosia_api', __name__)

@ambrosia_api.route('/recipes')
def get_recipes():
    s = [{"_id":"571d4a71-9950-11e9-9445-02420aff0021","name":"Eggnog","author":"How To Drink","rating":7,"notes":"https://www.youtube.com/watch?v=HYqXJWOZybY","tags":["eggnog","howtodrink","iced","christmas","bourbon","cognac","alcohol","drink"],"stages":[{"name":"Mixing","notes":"Preparation for the mixed portion of the drink.","ingredients":[{"name":"egg","unit":"","quantity":1},{"name":"bourbon","unit":"oz","quantity":2},{"name":"cognac","unit":"oz","quantity":0.5},{"name":"luxardo maraschino","unit":"oz","quantity":0.5},{"name":"simple syrup","unit":"oz","quantity":0.5}],"steps":["Mix the ingredients and shake until emulsified.","Add ice and continue shaking until chilled.","Strain into a glass."]},{"name":"Serving Instructions","notes":"","ingredients":[{"name":"grated nutmeg","unit":"","quantity":0},{"name":"grated orange peel","unit":"","quantity":0},{"name":"maraschino cherries","unit":"","quantity":0},{"name":"milk","unit":"oz","quantity":2}],"steps":["Top with milk.","Garnish with the grated nutmeg, orange peel, and cherries."]}]}]
    return jsonify(s)
