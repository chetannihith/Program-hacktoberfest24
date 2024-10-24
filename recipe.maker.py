import random

# List of ingredients
ingredients = [
    "chicken",
    "broccoli",
    "rice",
    "carrots",
    "onions",
    "bell peppers",
    "tomatoes",
    "cheese",
    "pasta",
    "olive oil",
    "garlic",
    "spinach",
    "soy sauce",
    "black beans",
    "tortillas"
]

# Function to create a random recipe
def create_recipe(ingredient_list, num_ingredients=5):
    # Randomly select a number of ingredients from the list
    selected_ingredients = random.sample(ingredient_list, min(num_ingredients, len(ingredient_list)))
    return selected_ingredients

# Generate a recipe
recipe = create_recipe(ingredients)
print("Your random recipe includes:")
for ingredient in recipe:
    print("-", ingredient)
