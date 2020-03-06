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


class Character:
    """
    Character
    
    This class represents all of the data and behaviour of a character in our game.
    """
   
    def __init__(self, name, hp, xpGained, attack, defense, magic=0):
        """
        __init__(self, name, hp, attack, defense, magic)
        
        This constructor initializes all of the instance variables of our class
        
        @arg self The character object being initialized
        @arg name The name of the character
        @arg hp The remaining hitpoints of the character
        @arg xp The amount of xp that has been collected so far, which is initialized to 0
        @arg xpGained The XP that would be gained by defeating the character
        @arg attack The attack power of the character
        @arg defense The defense power of the character
        @arg magic The magic power of the character (optional, default: 0)
        @arg level The current level of the character, which is initialized to 1
        """
        self.name = name
        self.hp = hp
        self.xp = 0
        self.xpGained = xpGained
        self.maxhp = hp
        self.attackpower = attack
        self.defensepower = defense
        self.magic = magic
        self.level = 1

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
    
    
     def attack(self, otherCharacter):
        """
        attack(self, otherCharacter)
        
        This function simulates an attack from this character ('self') to 'otherCharacter'.
        The other character's HP is updated with the damage taken.
        
        @arg self The character that is attacking
        @arg otherCharacter The target of the attack 
        """
        if self.isDead():
            print(self.name, 'cannot attack because he/she is dead.')
        else:
            damage = self.attackpower - otherCharacter.defensepower
            otherCharacter.hp -= damage
            if otherCharacter.hp < 0:
                otherCharacter.hp = 0
            print(self.name, 'does', damage, 'points of damage to', otherCharacter.name)
        
    def heal(self, party):
        """
        heal(self, party)
        
        This function simulates a healing spell.  The HP of the entire party is updated.
        
        @arg self The character that is healing
        @arg party The list of party members being healed 
        """
        if self.isDead():
            print(self.name, 'cannot heal because he/she is dead.')
        else:
            for partyMember in party:
                if not partyMember.isDead():
                    partyMember.hp += self.magic
                    if partyMember.hp > partyMember.maxhp:
                        partyMember.hp = partyMember.maxhp
                    print(self.name, 'heals', self.magic, 'hp for', partyMember.name)
    
    def __str__(self):
            """
            __str__(self)
            
            This function returns a string representation of our character
            
            @arg self The character that is being represented
            
            @return The string representation of the character
            """
            return self.name + ' has ' + str(self.hp) + ' HP.'
            return self.name + ' has ' + str(self.maxhp) + ' max HP.'
            return self.name + ' has ' + str(self.attackpower) + ' attack power.'
            return self.name + ' has ' + str(self.defensepower) + ' defense power.'
            return self.name + ' has ' + str(self.magic) + ' magic points.'
            return self.name + ' has gained ' + str(self.xpGained) + ' XP.'