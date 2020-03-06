#Jayson Sandhu, 100659589

#Declare Variables and Initialize with values
partyNames = ['Krogg', 'Glinda', 'Geoffrey']
partyHP = [180, 120, 150]
partyAttack = [20, 5, 15]
partyDefense = [20, 20, 15]
partyDead = [False, False, False]
bossAttack = 25
bossDefense = 25
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
	partyHP  = partyHP + 5
	isPartyDead(partyHP[])
	
	#Once Boss HP is less than 0, output the following statements based in which case is true   
	if (bossHP <= 0):
		print ("The boss is dead. You are victorious!")
	else:
		print ("Your whole party is dead. You lose.")    
    
def isPartyDead(party[]):
"""
	isPartyDeadDead(party[])
	
	This function returns True if the party is dead
	
	@arg party[] The Party's HP in the array we want to check
	"""
	if (party[] <= 0):
		return true
	else:
		return false

def isDead(partyHP[]):
	"""
	isDead(partyHP[])
	
	This function returns True if the character is dead
	
	@arg partyHP[] The character's HP in the party we want to check
	"""
	i=0
	
	if partyHP[i] <= 0:
		return True
	else:
	return False
