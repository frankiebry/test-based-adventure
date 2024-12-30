### Todo
- [ ] More immersive writing

### Ideas for changes/improvements
- [ ] Use colorized text to highlight keywords.
- [ ] Add combat and HP (change "caught" to "encounter")
- [ ] If player digs, and the key isn't there, chance to find more torches or other items
- [ ] Allow player to find more items, helpful items like torches and score items like gems
- [ ] Add high score
- [ ] Warn player when monster is close
- [ ] Monster chases player when torch is lit?
- [ ] Player finds items that protect them from the monster?
- [ ] Introduce rare item that lights up cave completely, and reveals treasure on map, but monster moves faster and/or beelines for the player
- [ ] Convert this entire game into a graphical version
- [ ] Add more color to text
- [ ] Add additional commands that display text but do nothing (e.g. "bang on door" -> "there is no response")

### Bugs/Issues
- [ ] The key doesn't disappear from the map when it's found, and the player just keeps getting more keys in their inventory if they dig in the same spot
- [ ] The alt codes for the icons on the map are different sizes and make the map look wonky. Find a set that are all the same dimensions
- [ ] Metal detector doesn't seem to work properly sometimes. I'll be standing one tile next to the treasure and it's silent? But other playthroughs it works perfectly...
- [ ] The player, monster and treasure can stack, and the last icon that is drawn on the map will cover any icon drawn before it.

### Clean Code
- [ ] All strings should use '' instead of ""? Or at least just be consistent
- [ ] Comment everything that doesn't have a clear purpose or needs to be explained?
- [ ] Functions need to be better named and commented using docstrings?
- [ ] Find a more elegant solution to the following ~

This statement is awkward...
```Python
remaining_torches = light_torch(player_position, monster.position, remaining_torches)
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