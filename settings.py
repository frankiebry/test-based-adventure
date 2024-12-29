import random

class Settings:
    def __init__(self):
        self.reset()

    def reset(self):
        """Resets all settings to their initial random state."""
        self.GRID_WIDTH = random.randint(4, 10)
        self.GRID_HEIGHT = random.randint(4, 10)
        self.DEFAULT_NUM_OF_TORCHES = 3
        self.DEFAULT_SEARCHED_POSITIONS = []
        self.DEFAULT_PLAYER_POS = (random.randint(0, self.GRID_WIDTH - 1), random.randint(0, self.GRID_HEIGHT - 1))
        self.DEFAULT_TREASURE_POS = (random.randint(0, self.GRID_WIDTH - 1), random.randint(0, self.GRID_HEIGHT - 1))
        self.DEFAULT_MONSTER_POS = (random.randint(0, self.GRID_WIDTH - 1), random.randint(0, self.GRID_HEIGHT - 1))

# Create a single instance of the Settings class
settings = Settings()