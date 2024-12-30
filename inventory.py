class Inventory:
    def __init__(self):
        """Initialize the player's inventory with default items."""
        self.items = {
            "torch": 3,  # Start with 3 torches
            "key": 0,    # Start with no key
        }

    def add_item(self, item, count=1):
        """Add an item to the inventory."""
        if item in self.items:
            self.items[item] += count
        else:
            self.items[item] = count

    def use_item(self, item):
        """Use an item from the inventory, if available."""
        if self.items.get(item, 0) > 0:
            self.items[item] -= 1
            return True
        return False

    def reset(self):
        """Reset the inventory to its default state."""
        self.items = {
            "torch": 3,  # Reset torches to 3
            "key": 0,    # Reset key count to 0
        }

    def has_item(self, item):
        """Check if the player has a specific item."""
        return self.items.get(item, 0) > 0

    def __str__(self):
        """Return a string representation of the inventory."""
        return f"Inventory: {self.items}"
    
# Create a single instance of the Inventory class
inventory = Inventory()