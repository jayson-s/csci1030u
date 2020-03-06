#Jayson Sandhu, 100659589

#Declare Variables and Initialize with values
partyNames = ['Krogg', 'Glinda', 'Geoffrey']
partyHP = [180, 120, 150]
partyAttack = [20, 5, 15]
partyDefense = [20, 20, 15]

bossAttack = 25
bossDefense = 15
bossHP = 500

round = 1

#Output round sequences while the HP for the Boss is greater than 0
while (bossHP > 0 or partyHP == 0): 
    print ("Round", round)
    round = round + 1
    print ("Krogg does", partyAttack [0], " points of damage to Boss")
	bossHP = bossHP - partyAttack [0]
    print ("Geoffrey does", partyAttack [2], " points of damage to Boss")
    bossHP = bossHP - partyAttack [2]
	partyHP = partyHP + 5
    
	
    
#Once Boss HP is less than 0, output the following statements based in which case is true   
if (bossHP <= 0):
    print ("The boss is dead. You are victorious!")
else:
    print (" You have been defeated!")    