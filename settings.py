import random

# Define the size of the map
GRID_WIDTH = random.randint(4,10)
GRID_HEIGHT = random.randint(4,10)
MAP_SIZE = (GRID_WIDTH,GRID_HEIGHT)

# Initial variable values
DEFAULT_NUM_OF_TORCHES = 3
DEFAULT_SEARCHED_POSITIONS = []
DEFAULT_RANDOM_POS = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))