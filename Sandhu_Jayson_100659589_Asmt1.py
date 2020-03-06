"""
Name: Jayson Sandhu
Student ID: 100659589

Partner's Name: Hassan Tariq
Partner's ID: 100657119
    
"""
    
    #Part 1: intersect([1,3,5,7,9,11,13,15,17,19,21,23,25], [1,4,9,16,25])
    #Intersection Function
def intersect (s1,s2):
  '''
  function to intersect two lists of integers
  s1 and s2 are the two lists that will be intersected
  output should be a list of the intersect values
  '''
#create new list with elements from s1 and s2
  s3 = list(s1 + s2)
#final duplicate variable
  resultList = []
#for loop to iterate over len of s3
  for i in range(len(s3)):
#for loop to run 1 ahead of i integer to check ==
    for j in range(i+1, len(s3)):
      if s3[i] == s3[j]:
#append duplicate integer into resultList        
        resultList.append(s3[i])
  return resultList

#Part 2: gregoryLiebniz(10000000)
#PI Function

def gregoryLiebniz(numIterations):
 '''
 function to estimate pi value
 numIterations is the number of time the formula is added
 output should be an estimate of pi
 '''
 formula = 0
 for i in range(numIterations):
#add formula to previous formula (+=)
   formula += ((-1)**i)/(2*(i)+1)
#return the formula multipled by 4 
 return 4*formula
    

    #Part 3
    #RPG Function
    
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
        
    
    def isDead(self):
        """
        isDead(self)
        
        This function returns True if this character is dead
        
        @arg self The character we want to check
        """
        if self.hp <= 0:
            return True
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
    
    
    def gainXP(self, xpGained):
        """"
        gainXP(self, xpGained)    

        This function  will add some amount of experience to the character, 
        possibly leveling them up as well.
        
        @arg self The character that is gaining some amount of experience
        @arg xpGained The amount of experience that will be allocated to existing amount
        """
        
        levels = [2,3,4,5,6]
        levelMinXP = [100,200,300,400,500]
        levelAttackGain = [5,7.5,10,12.5,15]
        levelDefenseGain = [2.5,5,7.5,10,15]
        levelMagicGain = [2,3,5,8,10]
        
        list(zip(levels, levelMinXP, levelAttackGain, levelDefenseGain, levelMagicGain))

        
        xp = self.xp + xpGained            
        
        if xp > levelMinXP:
            
            levels += 1
            levelAttackGain +=1
            
        
        
        