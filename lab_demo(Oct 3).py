#Demo

from random import randint

nZombies = 20
round = 1

while nZombies > 0:
    zombies_killed = randint(1,5)
    if zombies_killed <= nZombies:
        print('You have killed', zombies_killed, 'zombie(s) in round', round)
    else:
        print('You have killed the remaining %d zombie(s)' % nZombies)
        
    nZombies -= zombies_killed
    round += 1