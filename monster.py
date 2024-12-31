import random
from settings import settings
from utils import calculate_distance
from typewriter import typewriter

class Monster:
    def __init__(self, initial_position):
        """
        Initializes the Monster class with an initial position and the turn counter.
        
        Args:
        initial_position (tuple): The (x, y) coordinates of the monster's starting position.
        """
        self.position = initial_position
        self.turns_since_move = 0  # Track how many turns since the last move for the cooldown timer
        self.repellent_turns_left = 0  # Track how many turns the repellent is active

    def random_move(self):
        """
        Moves the monster in a random direction (north, south, east, west) if the move is within bounds.
        """
        directions = ["north", "south", "east", "west"]
        direction = random.choice(directions)
        
        if direction == "north" and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "south" and self.position[1] < settings.GRID_HEIGHT - 1:
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "east" and self.position[0] < settings.GRID_WIDTH - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "west" and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])

    def is_near_player(self, player_position):
        """
        Checks if the monster is within 2 steps of the player using Manhattan distance.
        
        Args:
        player_position (tuple): The (x, y) coordinates of the player's position.
        
        Returns:
        bool: True if the monster is within 2 steps of the player, otherwise False.
        """
        # Manhattan distance: sum of absolute differences in x and y
        distance = calculate_distance(self.position, player_position)
        return distance <= 2  # Monster chases the player if within 2 steps

    def chase_player(self, player_position):
        """
        Moves the monster one step towards the player's position.
        
        Args:
        player_position (tuple): The (x, y) coordinates of the player's position.
        """
        # Move towards the player horizontally or vertically
        if self.position[0] < player_position[0]:
            self.position = (self.position[0] + 1, self.position[1])
        elif self.position[0] > player_position[0]:
            self.position = (self.position[0] - 1, self.position[1])
        elif self.position[1] < player_position[1]:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.position[1] > player_position[1]:
            self.position = (self.position[0], self.position[1] - 1)

    def check_if_caught(self, player_position):
        """
        Checks if the monster has caught the player by comparing their positions.
        
        Args:
        player_position (tuple): The (x, y) coordinates of the player's position.
        
        Returns:
        bool: True if the monster has caught the player, otherwise False.
        """
        if self.position == player_position:
            return True
        return False
    
    def move(self, player_position):
        """
        Determines the monster's movement based on the turn count and its proximity to the player.
        The monster moves every two turns. If it's near the player, it chases the player; otherwise, it moves randomly.
        
        Args:
        player_position (tuple): The (x, y) coordinates of the player's position.
        """
        
        # TODO write this more elegantly
        self.turns_since_move += 1
        if self.turns_since_move >= 2:
            self.turns_since_move = 0
            # If repellent is active, move randomly for 3 turns
            if self.repellent_turns_left > 0:
                self.repellent_turns_left -= 1
                self.random_move()
            # If the monster is close to the player, it chases the player,
            elif self.is_near_player(player_position):
                typewriter("\033[91mYou hear a bloodcurdling howl as a foul stench fills the air.\033[0m", 0.05)
                self.chase_player(player_position)
            # else it moves randomly
            else:
                self.random_move()