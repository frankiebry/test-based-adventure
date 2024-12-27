import sys, time, os
import random

# Define the grid limits (no need for map_grid anymore)
GRID_SIZE = 4  # The grid is 4x4, so valid coordinates are (0, 0) to (3, 3)

# Make text output slower for immersion
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1)
            
    sys.stdout.write("\n")  # Ensure a newline at the end of the message
    sys.stdout.flush()

# Check if player is in the same location as treasure
def treasure_found(player_position, treasure_position):
    return player_position == treasure_position

# Tell the player their current coordinates
def reveal_position(position):
    typewriter("You light a torch and check your map.")
    typewriter(f"Your current coordinates are: {position}.")
    typewriter("The light has gone out")
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
            typewriter(f"You were caught by the monster at position {self.position}!")
            typewriter("Game Over!")
            return True
        return False

# Start the player in the top-left corner (0, 0)
player_position = (0, 0)
treasure_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
monster = Monster((random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))

# Main game loop
while True:
    # # Use to debug, comment out during gameplay
    # typewriter(f"You are at position {player_position}.")
    typewriter(f"The treasure is at {treasure_position}.")
    # typewriter(f"The monster is at {monster.position}.")
    
    command = input("What do you want to do?: ").strip().lower()
    
    if command.startswith("go "):
        direction = command[3:]  # Slicing syntax: Start at index 3 and begin extracting characters from the 4th character
        if direction == "north" and player_position[1] > 0:
            player_position = (player_position[0], player_position[1] - 1)
            typewriter(f"You moved north.")
            print(" ")
        elif direction == "south" and player_position[1] < GRID_SIZE - 1:
            player_position = (player_position[0], player_position[1] + 1)
            typewriter(f"You moved south.")
            print(" ")
        elif direction == "east" and player_position[0] < GRID_SIZE - 1:
            player_position = (player_position[0] + 1, player_position[1])
            typewriter(f"You moved east.")
            print(" ")
        elif direction == "west" and player_position[0] > 0:
            player_position = (player_position[0] - 1, player_position[1])
            typewriter(f"You moved west.")
            print(" ")
        else:
            typewriter("The way is blocked.")
            print(" ")
        
        # Move the monster and check if the player is caught
        monster.move()
        if monster.check_if_caught(player_position):
            break  # End the game if the player was caught by the monster

    elif command == 'look for treasure'.strip().lower():
        if treasure_found(player_position, treasure_position):
            typewriter("You found the treasure!")
            print(" ")
            typewriter("Game Over")
            break
        else:
            typewriter("There is nothing here")
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
        typewriter(f"I don't know what '{command}' means.")
        print(" ")