from random import randint

class DiceDict(object):
    """
    List to simulate dictionary. Initializes as empty, and is formatted
    with L[0] = key, L[1] = value.
    """

    def __init__(self):
        """
        Dict is initialized with no components. Format:
        List to simulate the dictionary.
        1st column: "key"
        2nd column: "value"
        --1st column in 2nd column: number of dice of that type
        --2nd column in 2nd column: Die object

        Args:
            Nothing
        """
        self.List = []
    
    def add_or_increment_die(self, dieNumSides):
        """
        Takes one int and, if the die corresponding to that number is present in the list,
        increments the number of those dice, otherwise adds an instance of that die to the poke
        and sets the quantity to 1 - all internally.
        Args:
            dieNumSides - int for number of sides on that die
        Returns:
            Nothing
        """
        
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
        """
        Emulates the .values() function of the built-in Python dictionary. 
        Args:
            Nothing
        Returns:
            A list of the contents of the second column of the "dictionary" list.
        """
        return [sublist[1] for sublist in self.List]
            
class Poke(object):
    """
    An abstract bag that "holds" dice. Implements DiceDict to store information
    and instances of Die class.
    """
    def __init__(self):
        """
        Initializes empty with a new DiceDict and a variable to keep track of
        how many dice it holds (used later for quicker randomized dice
        selection).

        Args:
            Nothing
        """
        self.diceDict = DiceDict()
        self.totalNumDice = 0
    
    def add_die(self, numDieSides):
        """
        Called with one argument, the side of the die to be added, it will then
        call the DiceDict to add it to the list and also increment its running
        total of the currently held number of dice. Exception catching is
        performed at the level of the poke - only integers in the allowed
        list are passed on to the Die method.
        Args:
            numDieSides - int for number of sides of die to be added
        Returns:
            Nothing
        """
        allowedDice = [4, 6, 8, 12, 20]
        
        if numDieSides in allowedDice:
            self.diceDict.add_or_increment_die(numDieSides)
            self.totalNumDice += 1
            
        else:
            print "Invalid number of sides for a die in this poke."
    
    def pick_die(self):
        """
        Randomly returns one Die instance from the poke implementing randint from random module.
        Args:
            Nothing
        Returns:
            Randomly selected die from poke's contents
        """
        r = randint(1,self.totalNumDice)
        
        for eachDieType in self.diceDict.values():
            if r > eachDieType[0]:
                r -= eachDieType[0]
            else:
                return eachDieType[1]
        
    def sample_poke(self):
        """
        Calls pick_die to randomly select a die from the poke and then calls
        roll() on that Die instance to obtain the numerically rolled value,
        returning that to the caller.
        Args:
            Nothing
        Returns:
            Int for the value of the rolled random die
        """
        return self.pick_die().roll()
    
    def print_poke(self):
        """
        Prints the contents of the poke to the console, omitting any slots of
        the poke that have no dice and therefore haven't been initialized in
        the DiceDict yet.
        Args:
            Nothing
        Returns:
            Nothing
        """
        for dieType, value in sorted(self.diceDict.List):
            print str(value[0]), str(dieType) + "-sided dice"
        
class Die(object):
    """
    A simple class to represent a die, upon which can be called only the roll
    method. Uses instance variable for sides and randint.
    """
    
    def __init__(self, sides):
        """
        Initializes with a simple internal value of the number of sides of that
        instance of the Die class.
        Args:
            sides - number of sides for the new Die object
        """
        self.sides = sides
        
    def roll(self):
        """
        Returns a random integer value based on the number of sides on that die.
        Args:
            Nothing
        Returns:
            randomly selected integer in [1, self.sides] range
        """
        return randint(1,self.sides)

def main():
    
    # Initalize the (empty) poke
    poke = Poke()
    
    # A list of the possible dice being used in this particular test.
    possDice = [4,6,8,12,20]
    
    # A testing of the Exploration case of 2 tetra-, 0 hexa-, 3 octa-, 1 dodeca-,
    # and 4 icosa-hedrons. Also testing the catching of unintended inputs.
    # Using the list of possible dice to make assignment easier.
    poke.add_die(possDice[0])
    poke.add_die(possDice[0])
    poke.add_die(possDice[2])
    poke.add_die(possDice[2])
    poke.add_die(possDice[2])
    poke.add_die(possDice[3])
    poke.add_die(possDice[4])
    poke.add_die(possDice[4])
    poke.add_die(possDice[4])
    poke.add_die(possDice[4])
    poke.add_die("fas")
    poke.add_die(17)
    
 
    print "" #Output formatting

    # Testing of the print_poke() poke method and double-checking the 
    # implementation of add_die()
    poke.print_poke()
    
    # Variables for Observed Expected Values
    total = 0.0
    testSize = 1

    print "" #Output formatting
    
    # Iterating through for the three (3) cases for Observed Expected Values
    # and printing the results to the console.
    for i in range(3):
        total = 0.0
        testSize *= 100
    
        for i in range(testSize):
            total += poke.sample_poke()
        
        print "%s's Total: %s" % (testSize, total)
        print "Average: %s " % (total / testSize)

    print "" #Output formatting
    
    # Testing again with another poke (POKE)
    POKE = Poke()
    
    for i in range(1000):
        r = randint(0,4)
        POKE.add_die(possDice[r])
        
    POKE.print_poke()

    print "\nPOKE's sample: %s" % (POKE.sample_poke())
    
    
if __name__ == '__main__':
    main()