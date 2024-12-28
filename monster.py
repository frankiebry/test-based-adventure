import random
from typewriter import typewriter
from settings import GRID_WIDTH, GRID_HEIGHT

class Monster:
    def __init__(self, position):
        self.position = position
        self.turns_since_move = 0  # Track how many turns since the last move

    def random_move(self):
        directions = ["north", "south", "east", "west"]
        direction = random.choice(directions)
        
        if direction == "north" and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "south" and self.position[1] < GRID_HEIGHT - 1:
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "east" and self.position[0] < GRID_WIDTH - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "west" and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])

    def is_near_player(self, player_position):
        """Manhattan distance: sum of the absolute differences in x and y"""
        distance = abs(self.position[0] - player_position[0]) + abs(self.position[1] - player_position[1])
        return distance <= 2  # Monster chases the player if within 2 steps

    def chase_player(self, player_position):
        """Chase the player by moving towards them"""
        if self.position[0] < player_position[0]:
            self.position = (self.position[0] + 1, self.position[1])
        elif self.position[0] > player_position[0]:
            self.position = (self.position[0] - 1, self.position[1])
        elif self.position[1] < player_position[1]:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.position[1] > player_position[1]:
            self.position = (self.position[0], self.position[1] - 1)

    def check_if_caught(self, player_position):
        if self.position == player_position:
            return True
        return False
    
    def move(self, player_position):
        """Monster only moves every two turns"""
        self.turns_since_move += 1
        if self.turns_since_move >= 2:
            self.turns_since_move = 0
            # If the monster is close to the player, it chases the player,
            if self.is_near_player(player_position):
                self.chase_player(player_position)
            # else it moves randomly
            else:
                self.random_move()