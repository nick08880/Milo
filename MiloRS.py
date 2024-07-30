import random

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"Recipe for {self.name}\n\nIngredients:\n{self.ingredients}\n"

def welcome_message():
    print("Welcome to Milo's Recipe Storage!")
    print("Click 'a' to add a recipe.")
    print("Click 'i' to see inventory.")
    print("Click 'r' for a random recipe.")
    print("Click 'h' for help.")
    print("Click 'q' to quit.")

def help_message():
    print("Help Menu:")
    print("a - Add a recipe: Allows you to enter a new recipe into the storage.")
    print("i - View inventory: Displays all recipes currently stored.")
    print("r - Random recipe: Fetches and displays a random recipe from the inventory.")
    print("h - Help: Provides information about available commands and their benefits.")
    print("q - Quit: Exits the program.")
    print("\nNote: Adding a recipe will permanently store it in the inventory.")

def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma separated): ")
    confirm = input(f"Are you sure you want to add the recipe '{name}'? (y/n): ")
    if confirm.lower() != 'y':
        print("Recipe not added.")
        return
    recipe = Recipe(name, ingredients)
    recipes.append(recipe)
    history.append(('add', recipe))
    print("Recipe added successfully!")

def view_recipes():
    if not recipes:
        print("No recipes found.")
    for recipe in recipes:
        print(recipe)

def random_recipe():
    if not recipes:
        print("No recipes available.")
        return
    recipe = random.choice(recipes)
    print(recipe)

def undo():
    if not history:
        print("No actions to undo.")
        return
    action, item = history.pop()
    if action == 'add':
        confirm = input(f"Are you sure you want to undo adding the recipe '{item.name}'? (y/n): ")
        if confirm.lower() != 'y':
            history.append(('add', item))  # Re-add to history if undone action is canceled
            print("Undo canceled.")
            return
        recipes.remove(item)
        print("Last action undone.")
    else:
        print("Cannot undo this action.")

def menu():
    while True:
        welcome_message()
        choice = input("Choose an option: ")
        if choice == 'a':
            add_recipe()
        elif choice == 'i':
            view_recipes()
        elif choice == 'r':
            random_recipe()
        elif choice == 'h':
            help_message()
        elif choice == 'q':
            print("Exiting program.")
            break
        elif choice == 'u':
            undo()
        else:
            print("Invalid choice. Please try again.")

recipes = []
history = []

menu()