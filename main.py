from monster import Monster
from typewriter import typewriter
from settings import settings
from utils import calculate_distance

class Game:
    def __init__(self):
        """Initialize the game by resetting to default settings."""
        self.reset_game() # Reset the game to its initial state with default settings

    def reset_game(self):
        """Reset the game to its initial state with default settings."""
        settings.reset() # Reset the settings to their default values
        self.remaining_torches = settings.DEFAULT_NUM_OF_TORCHES
        self.searched_positions = settings.DEFAULT_SEARCHED_POSITIONS
        self.player_position = settings.DEFAULT_PLAYER_POS
        self.treasure_position = settings.DEFAULT_TREASURE_POS
        self.monster = Monster(settings.DEFAULT_MONSTER_POS)

    def treasure_found(self):
        """Check if the player is at the treasure's position."""
        return self.player_position == self.treasure_position

    def draw_map(self, show_treasure=False):
        """
        Draw the game map with the player, monster, and optionally the treasure.

        Args:
            show_treasure (bool): Whether to display the treasure on the map.
        """
        grid = [['□ ' for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]
        for pos in self.searched_positions: # Mark the spots the player has already dug
            x, y = pos
            grid[y][x] = '\033[96mX \033[0m' # Use ANSI escape codes for colored text - Bright Cyan
        player_x, player_y = self.player_position
        grid[player_y][player_x] = '\033[92m⧆ \033[0m' # Bright Green
        monster_x, monster_y = self.monster.position
        grid[monster_y][monster_x] = '\033[95mM \033[0m' # Bright Magenta
        if show_treasure:
            treasure_x, treasure_y = self.treasure_position
            grid[treasure_y][treasure_x] = '\033[93m⚿ \033[0m' # Bright Yellow
        for row in grid: # Print the map row by row
            print(''.join(row))

    def light_torch(self):
        """Use a torch to reveal the map and display helpful information."""
        if self.remaining_torches > 0: # Check if the player has any torches left
            self.remaining_torches -= 1
            typewriter("You light a torch and check your map.", 0.05)
            print(" ")
            self.draw_map()
            print(" ")
            typewriter("\033[92m⧆\033[0m: Your current location.", 0.05)
            typewriter("\033[96mX\033[0m: Spots you've already dug.", 0.05)
            typewriter("\033[95mM\033[0m: You see an ominous shadowy figure standing there...", 0.1)
            if self.remaining_torches == 1: # Handle singular vs. plural in the message.
                typewriter(f"The light has gone out. You have {self.remaining_torches} torch left", 0.05)
            else:
                typewriter(f"The light has gone out. You have {self.remaining_torches} torches left", 0.05)
            print(" ")
        else:
            typewriter("You don't have any torches left", 0.05)

    def sweep_for_treasure(self):
        """Use the metal detector to get a hint about the treasure's location."""
        distance = calculate_distance(self.player_position, self.treasure_position)
        if distance == 0:
            typewriter("The metal detector is going wild!!", 0.05)
        elif distance == 1:
            typewriter("The metal detector is beeping rapidly!", 0.05)
        elif distance == 2:
            typewriter("The metal detector is slowly beeping.", 0.05)
        else:
            typewriter("The metal detector is silent.", 0.05)

    def display_commands(self):
        """Display the list of available commands to the player."""
        print(" ")
        typewriter("*****************", 0.02)
        typewriter("* Legal commands *", 0.02)
        typewriter("*****************", 0.02)
        print(" ")
        typewriter("MOVE NORTH", 0.02)
        typewriter("MOVE SOUTH", 0.02)
        typewriter("MOVE EAST", 0.02)
        typewriter("MOVE WEST", 0.02)
        typewriter("DIG HERE", 0.02)
        typewriter("USE A TORCH: check your map", 0.02)
        typewriter("SWEEP FOR TREASURE: use metal detector", 0.02)
        print(" ")

    def debug(self):
        """Display the full map, including the treasure's location (cheat/debug mode)."""
        print(" ")
        self.draw_map(show_treasure=True) # Show the treasure on the map
        print(" ")

    def welcome_screen(self):
        """Display the welcome screen and explain the rules for first timers."""
        response = input(
            "Welcome to Frankie's text based adventure game. Have you played this game before? (Y/N): "
        ).strip().lower()
        if response in ['n', 'no']:
            print(" ")
            typewriter("Here are the rules:", 0.05)
            print(" ")
            typewriter("You are in a dark cave. Each turn you can use a command to do one of the following.", 0.05)
            typewriter("* Move north, south, east or west", 0.05)
            typewriter("* Use your metal detector to sweep for treasure.", 0.05)
            typewriter("* Dig for treasure.", 0.05)
            typewriter("* Light a torch to check your map. You only get 3 torches.", 0.05)
            typewriter("Beware, there is a monster in the cave with you. Each turn the monster moves one pace.", 0.05)
            typewriter("The game will end if you find the treasure... or the monster catches you. Good luck!", 0.05)

    def play_again(self):
        """Prompt the player to decide whether to play again."""
        response = input("Do you want to play again? (Y/N): ").strip().lower()
        return response in ["y", "yes"]

    def run(self):
        """Run the main game loop, handling player commands and game logic."""
        self.welcome_screen()
        while True:
            print(" ")
            command = input("What do you want to do?: ").strip().lower()
            monster_should_move = True # Assume the monster will move on each turn by default

            match command:
                case "go north" | "move north" | "go up" | "move up":
                    if self.player_position[1] > 0:
                        self.player_position = (self.player_position[0], self.player_position[1] - 1)
                        typewriter("You moved north.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case "go south" | "move south" | "go down" | "move down":
                    if self.player_position[1] < settings.GRID_HEIGHT - 1:
                        self.player_position = (self.player_position[0], self.player_position[1] + 1)
                        typewriter("You moved south.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case "go east" | "move east" | "go right" | "move right":
                    if self.player_position[0] < settings.GRID_WIDTH - 1:
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        typewriter("You moved east.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case "go west" | "move west" | "go left" | "move left":
                    if self.player_position[0] > 0:
                        self.player_position = (self.player_position[0] - 1, self.player_position[1])
                        typewriter("You moved west.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case "dig" | "dig for treasure" | "dig here" | "look for treasure" | \
                    "look for treasure here" | "search" | "search here" | "search for treasure":
                    if self.treasure_found():
                        typewriter("Congratulations! You found the treasure!", 0.05)
                        print(" ")
                        if self.play_again():
                            self.reset_game()
                            continue
                        else:
                            typewriter("Thank you for playing!", 0.05)
                            break
                    else:
                        typewriter("There is nothing here.", 0.05)
                        self.searched_positions.append(self.player_position) # Mark the spot as searched

                case "light torch" | "light a torch" | "use torch" | "use a torch" | "look around" | \
                    "where am I?" | "where am I" | "I don't know where I am" | "I don't know where I am." | \
                    "check map" | "check my map" | "look at map" | "look at my map" | "look at the map" | \
                    "use map" | "use my map" | "use the map" | "use the map here":
                    self.light_torch()

                case "sweep" | "sweep for treasure" | "sweep here" | "sweep for treasure here" | \
                    "use metal detector" | "use metal detector here" | \
                    "use the metal detector" | "use the metal detector here":
                    self.sweep_for_treasure()

                case "help" | "commands" | "options" | "I don't know what to do" | \
                    "what can I do" | "what can I do?" | "what do I do" | "what do I do?":
                    self.display_commands()
                    monster_should_move = False

                case "cheat" | "debug":
                    print(" ")
                    self.debug()
                    monster_should_move = False

                case _:
                    typewriter(f"I don't know what '{command}' means.", 0.05)
                    print(" ")
                    monster_should_move = False

            if monster_should_move:
                self.monster.move(self.player_position)
                if self.monster.check_if_caught(self.player_position):
                    print(" ")
                    typewriter(f"You were caught by the monster!", 0.05)
                    print(" ")
                    if self.play_again():
                        self.reset_game()
                        continue
                    else:
                        typewriter("Thank you for playing!", 0.05)
                        break

        print(" ")
        typewriter("GAME OVER", 0.5)

# Run the game if this script is executed
if __name__ == '__main__':
    game = Game()
    game.run()