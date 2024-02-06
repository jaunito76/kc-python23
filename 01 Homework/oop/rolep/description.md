# Adventure Quest Game:

## Game Description:

The game is a text-based adventure where the player goes on a quest through a fictional world.
The player can encounter different challenges, make decisions, and collect items.
The player will have a character with attributes such as health, attack power, and inventory.

# Object-Oriented Concepts to Implement:

## Character Class:

Create a Character class with attributes like health, attack power, and inventory.
Implement methods for taking damage, attacking, and managing inventory.

## Enemy Class:

Create an Enemy class that the player can encounter during the adventure.
The enemy should have health, attack power, and drop items.

## Item Class:

Create an Item class for items that the player can collect.
Items can have different effects, such as healing the player or boosting attack power.

## Game Class:

Implement a Game class to manage the overall game logic.
Handle the player's progression through the adventure, encounters with enemies, and item collection.

# Example Code Skeleton:
```python
class Character:
    def __init__(self, name, health, attack_power):
        # Initialize character attributes

    def take_damage(self, amount):
        # Update character health after taking damage

    def attack(self, enemy):
        # Perform an attack on the enemy

    def collect_item(self, item):
        # Add item to the inventory

class Enemy:
    def __init__(self, name, health, attack_power, drop_item=None):
        # Initialize enemy attributes

    def take_damage(self, amount):
        # Update enemy health after taking damage

class Item:
    def __init__(self, name, effect):
        # Initialize item attributes

class Game:
    def __init__(self):
        # Initialize game state

    def start_adventure(self):
        # Start the adventure and manage game progression
```

# Create instances of the classes and run the game
This project allows students to practice creating and interacting with classes, handling object interactions, and managing game logic using OOP principles. They can expand on the project by adding more features, creating a richer story, or introducing additional classes and mechanics.