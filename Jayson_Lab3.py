#Jayson Sandhu, 100659589

#Declare Variables and Initialize with values
kroggAttack = 38.5
kroggDefense = 20.0
kroggHP = 200

bossAttack = 25
bossDefense = 12.5
bossHP = 200

round = 1


#Output round sequences while the HP for the Boss or Krogg is greater than 0
while (kroggHP > 0 | bossHP > 0.00): 
    print ("Round", round)
    round = round + 1
    print ("Krogg does", kroggAttack, " points of damage to Boss")
    print ("Boss does", bossAttack, " points of damage to Krogg")
    bossHP = bossHP - kroggAttack
    print ("Boss: ", bossHP)
    kroggHP = kroggHP - bossAttack
    print ("Krogg: ", kroggHP)
    
#Once Boss or Krogg has HP less than 0, output the following statements based in which case is true   
if (kroggHP > bossHP):
    print ("Krogg has won. You are victorious!")
else:
    print ("The Boss has won. You have been defeated!")    