#arithmetic = + addition
#                   - subtraction
#                   * multiplication
#                   / division (returns a float)
#                   // integer division (returns an integer)
#                   % remainder (modules)

friends = 16
enemies = 20
dogs = 8
cats = 9
birds = 9
remaining_friends = friends % 3
#friends = friends + 15
friends += 3 # shortcut for adding
#enemies = enemies - 1
enemies -= 1 # augmented shortcut for subtraction
#dogs = dogs * 8
dogs *= 9 # augmented shortcut for multiplication
#cats = cats / 3
cats /= 3 # augmented shortcut for division (float)
#birds = birds // 3
birds //= 3 # augmented shortcut for division (integer)
print(friends)
print(enemies)
print(dogs)
print(cats)
print(birds)
print(remaining_friends)