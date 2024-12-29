### Todo
- [ ] Add inventory using a dictionary.
- [ ] Allow player to find more items
- [ ] Warn player when monster is close
- [ ] Add `if __name__ == '__main__':`
- [ ] Add a "play again" option.
- [ ] Separate debug into another file?
- [ ] Convert this entire game into a graphical version
- [ ] Player and treasure should be separate classes as well?
- [ ] Allow player to type more commands that do the same thing (e.g. "go north", "move north", "go up", etc)
- [ ] More immersive writing
- [ ] More commands

### Ideas for changes/improvements
- [ ] Instead of treasure, player looks for key to escape dungeon?
- [ ] Monster chases player when torch is lit?
- [ ] Player finds items that protect them from the monster?
- [ ] If player digs, and treasure isn't there, chance to find more torches or other items
- [ ] Introduce rare item that lights up cave completely, and reveals treasure on map, but monster moves faster and/or beelines for the player

### Bugs/Issues
- [ ] Metal detector doesn't seem to work properly sometimes. I'll be standing one tile next to the treasure and it's silent? But other playthroughs it works perfectly...
- [ ] The last icon that is drawn on the map will cover any icon drawn before it.

### Clean Code
- [ ] Repeated distance calculations (e.g., in sweep_for_treasure and Monster.is_near_player) could be centralized.
- [ ] Better solution to making all variables global in reset_game() function, it looks clunky
- [ ] I had to remove variables from settings.py and put them in main.py, and pass them to the monster class, in order for reset_game() to work properly. The statement that initializes the monster object (line 206) now looks inelegant... find out if and how settings.py can still be used... update settings.py dynamically?
- [ ] Create "randomize()" function that returns a tuple of random values? Then use this function anytime a position needs to be reset or randomize?
- [ ] All strings should use '' instead of ""? Or at least just be consistent
- [ ] Comment everything that doesn't have a clear purpose?
- [ ] Functions need to be better named and commented using docstrings?
- [ ] Find a more elegant solution to the following ~

This statement is awkward...
```Python
num_of_torches = light_torch(player_position, monster.position, num_of_torches)
```

Also this code block is used twice...
```Python
# Ask if the player wants to play again
if play_again():
    reset_game()  # Reset the game state
    continue  # Restart the game loop
else:
    typewriter("Thank you for playing!", 0.05)
    break
```