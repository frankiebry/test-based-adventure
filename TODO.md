### Todo
- [ ] Add inventory using a dictionary.
- [ ] Allow player to find more items
- [ ] Warn player when monster is close
- [ ] Add `if __name__ == '__main__':`
- [ ] Add a "play again" option.
- [ ] Separate debug into another file?
- [ ] Convert this entire game into a graphical version
- [ ] Player and treasure should be separate classes as well?

### Ideas for changes
- [ ] Instead of treasure, player looks for key to escape dungeon?
- [ ] Monster chases player when torch is lit?
- [ ] Player finds items that protect them from the monster?

### Issues
- [ ] The last icon that is drawn on the map will cover any icon drawn before it.

### Clean Code
- [ ] Comment everything that doesn't have a clear purpose?
- [ ] Functions need to be better named and commented using docstrings?
- [ ] Find a more elegant solution to the following ~

This statement is awkward...
```Python
num_of_torches = light_torch(player_position, monster.position, num_of_torches)
```