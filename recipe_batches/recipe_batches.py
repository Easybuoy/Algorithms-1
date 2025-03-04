#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    if (len(recipe) > len(ingredients)):
        return 0

    for ingredient in ingredients.keys():
        if ingredients[ingredient] < recipe[ingredient]:
            return 0
        else:
            placeholder = ingredients[ingredient] // recipe[ingredient]
            batches.append(placeholder)

    return min(batches)


print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
      'milk': 198, 'butter': 52, 'cheese': 10}))

# print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
#       'milk': 1288, 'flour': 9, 'sugar': 95, 'butter': 10}))
if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
