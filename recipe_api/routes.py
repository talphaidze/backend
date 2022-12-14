from flask import Flask, request
from recipe_api import db, app
from recipe_api.models import Recipe


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'

@app.route('/recipes', methods=['POST'])
def create_account():
    name = request.json['name']
    ingredients = request.json['ingredients']
    rating = request.json['rating']
    favorite = request.json['favorite']
    recipe = Recipe(name, ingredients, rating, favorite)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.rating = request.json['rating']
    recipe.favorite = request.json['favorite']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'rating': recipe.rating,
        'favorite': recipe.favorite,
        'created_at': recipe.created_at,
    }
