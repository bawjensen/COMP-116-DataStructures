from random import randint

class DiceDict(object):
    def __init__(self):
        # List to simulate the dictionary.
        # List[0] is the key
        # List[1] is the value (often a list itself)
        self.List = []
    
    def add_or_increment_die(self, dieNumSides):
        if len(self.List) > 0:
            for i in range(len(self.List)):
                if (self.List[i])[0] == dieNumSides:
                    self.List[i][1][0] += 1
                    break
            else:
                key = dieNumSides
                value = [1, Die(dieNumSides)]
                self.List.append([key, value])
        
        else:
            key = dieNumSides
            value = [1, Die(dieNumSides)]
            self.List.append([key, value])
            
    def values(self):
        return [sublist[1] for sublist in self.List]
    
class Poke(object):
    def __init__(self):
        self.diceDict = DiceDict()
        self.totalNumDice = 0
    
    def add_die(self, numDieSides):
        self.diceDict.add_or_increment_die(numDieSides)
        self.totalNumDice += 1
    
    def pick_die(self):
        
        r = randint(1,self.totalNumDice)
        
        for eachDieType in self.diceDict.List:
            if r > eachDieType[0]:
                r -= eachDieType[0]
            else:
                return eachDieType[1]
        
    def sample_poke(self):
        r = randint(1,len(self.numDiceDict))
        
        return numDiceDict[r]
    
    def print_poke(self):
        for dieType, value in sorted(self.diceDict.List):
            print str(value[0]), str(dieType) + "-sided dice"
    
class Die(object):
    from random import randint
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self):
        from random import randint
        return randint(1,self.sides)