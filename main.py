import random

# Define the grid limits (no need for map_grid anymore)
GRID_SIZE = 4  # The grid is 4x4, so valid coordinates are (0, 0) to (3, 3)

# Check if player is in the same location as treasure
def treasure_found(player_position, treasure_position):
    return player_position == treasure_position

# Tell the player their current coordinates
def reveal_position(position):
    print("You light a torch and check your map.")
    print(f"Your current coordinates are: {position}.")
    print("The light has gone out")
    print(" ")

class Monster:
    def __init__(self, position):
        self.position = position

    def move(self):
        directions = ["north", "south", "east", "west"]
        direction = random.choice(directions)
        
        if direction == "north" and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "south" and self.position[1] < GRID_SIZE - 1:
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "east" and self.position[0] < GRID_SIZE - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "west" and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])

    def check_if_caught(self, player_position):
        if self.position == player_position:
            print(f"You were caught by the monster at position {self.position}!")
            print("Game Over!")
            return True
        return False

# Start the player in the top-left corner (0, 0)
player_position = (0, 0)
treasure_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
monster = Monster((random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))

# Main game loop
while True:
    # # Use to debug, comment out during gameplay
    # print(f"You are at position {player_position}.")
    # print(f"The treasure is at {treasure_position}.")
    # print(f"The monster is at {monster.position}.")
    
    command = input("What do you want to do?: ").strip().lower()
    
    if command.startswith("go "):
        direction = command[3:]  # Slicing syntax: Start at index 3 and begin extracting characters from the 4th character
        if direction == "north" and player_position[1] > 0:
            player_position = (player_position[0], player_position[1] - 1)
            print(f"You moved north.")
            print(" ")
        elif direction == "south" and player_position[1] < GRID_SIZE - 1:
            player_position = (player_position[0], player_position[1] + 1)
            print(f"You moved south.")
            print(" ")
        elif direction == "east" and player_position[0] < GRID_SIZE - 1:
            player_position = (player_position[0] + 1, player_position[1])
            print(f"You moved east.")
            print(" ")
        elif direction == "west" and player_position[0] > 0:
            player_position = (player_position[0] - 1, player_position[1])
            print(f"You moved west.")
            print(" ")
        else:
            print("The way is blocked.")
            print(" ")
        
        # Move the monster and check if the player is caught
        monster.move()
        if monster.check_if_caught(player_position):
            break  # End the game if the player was caught by the monster

    elif command == 'look for treasure'.strip().lower():
        if treasure_found(player_position, treasure_position):
            print("You found treasure!")
            print(" ")
            print("Game Over")
            break
        else:
            print("There is nothing here")
            print(" ")
            
            # Move the monster and check if the player is caught
            monster.move()
            if monster.check_if_caught(player_position):
                break  # End the game if the player was caught by the monster
    elif command == 'look around'.strip().lower():
        reveal_position(player_position)
        monster.move()
        if monster.check_if_caught(player_position):
            break  # End the game if the player was caught by the monster
    else:
        print(f"I don't know what '{command}' means.")
        print(" ")