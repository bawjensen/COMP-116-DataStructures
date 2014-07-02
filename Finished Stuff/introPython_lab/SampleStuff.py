# SampleStuff.py

"""Provides a sample class to show examples
of Python procedurual and OOP features

v2.7
"""

# uncomment to get v2.x to treat division like in v3.x
# from __future__ import division

import re
import math
import string
import pickle
import os


class SampleStuff(object):
    """A Python class to find to intro a bunch of Python features """
    
    #=====================================================         
    def __init__(self, filename):
        """CTOR
        """
        
	# (initialize) data members
	self.startingFileName = filename
	self.pickleFileName = "pickle_" + filename
	self.answer = 0
	
	self.WordCounts = {}  # dictionary of (word, count) pairs
        
        
    #=====================================================   
    def passBy(self, t):
        """ testing passByRef? do you think Python does passByValue?
	""" 
	
	# does this change the actual arg back in main() ?
        t = 10
        
        
    #=====================================================       
    def basicMath(self, x, y):
	"""testing mathematical operations, etc."""
        
        """ look Ma, a swap in one line! """
        print("\tIn basicMath():")
	print("\t\tbefore: %d and %d" % (x,y))
        x,y = y,x
        print("\t\tafter:  %d and %d\n" % (x,y))
        
        # ------- v2.x specific -----------------------
        # ugh, integer division in v2.x
        z = 5 / 3
        print("\t\t z after division is: %5.1f \n" % z)
        
        """ now uncomment the line at the very top of this file
        from __future__ import division
        and rerun """
	# ------- end v2.x specific -----------------------
        
        # use double // to REALLY mean integer division
        z = 5 // 3
        print("\t\t z after 5/3 INTEGER division is: %d \n" % z)
        
        z = math.sqrt(16)
        b = 2**z
        
        
    #=====================================================       
    def fileIO(self):
        """testing file Input and Output (IO) operations """
	
	somePhrase = raw_input("Enter a word: ")
	somePhrase = somePhrase.lower()
	print("Original word: %s\n" % (somePhrase))
	
	if not os.path.exists(self.startingFileName):
	    print("\nSORRY, the file",self.startingFileName, "does not exist.")
	    print("Try another filename ...")
			
	else:	
	    print("\nReading from file: %s ...\n" % (self.startingFileName))
	    
	    fin = open(self.startingFileName, 'r')
	    
	    for line in fin:
		""" chomp" line -> remove endlines""" 
		sentence = line.rstrip()
		sentence = sentence.lower()
	    
		print("Original line: %s" % (sentence))
	    
		""" remove any char that is NOT a valid letter """
		""" (1) first *make* a regex """
		REpunct = re.compile('[^A-Za-z]')
		""" (2) now substitute nothing ('') for anything matches """
		mashedSentence = REpunct.sub('', sentence)
	    
		""" make a regex that only matches letters included in somePhrase """
		REmatchOnlyTheseLetters = "^[" + somePhrase + "]*$"
	    
		if ( re.match(REmatchOnlyTheseLetters, mashedSentence) ):
		    print("\tMATCH: %s" % (mashedSentence))
		
	    print("\n")
	    fin.close()
	    
	    # end else file opened ok
    
    #=====================================================       
    def makeDictionary(self):
        """create a hash table (Dictionary, Map) of word frequencies """
		
	fin = open(self.startingFileName, 'r')
	
        for line in fin:
	    """ chomp" line -> remove endlines""" 
	    sentence = line.rstrip()
	    sentence = sentence.lower()
	    
	    # ignoring punctuation .... sloppy :(    
	    
	    # split sentence up into individual words
	    # really need a more sophisticated split (than just space) here?
	    allWords = string.split(sentence, " ")
	    
	    for word in allWords:
		if word in self.WordCounts:
		    """  increment that word's count """
		    self.WordCounts[word] = self.WordCounts[word] + 1
		else:
		    self.WordCounts[word] = 1
		    
		    
	print("\nDone loading words into dictionary ...");
	for nextKey in list(self.WordCounts.keys()):
	    print("%s:\t%d" % (nextKey, self.WordCounts[nextKey]))
	print("\n")
	
	
    #=====================================================       
    def pickle_saveToFile(self):
	"""create pickle file of our Dictionary"""
	
	fh = open(self.pickleFileName, 'w')
	pickle.dump(self.WordCounts, fh)
	fh.close()
    
    #=====================================================       
    def pickle_loadFromFile(self):
	"""load our pickle file back into our Dictionary """
	
	fh = open(self.pickleFileName)
	self.WordCounts = pickle.load(fh)
	fh.close()
    
    
    #=====================================================       
    def backTracking(self, k, L, s):
	"""testing Recursion and practice with backtracking"""
	
	""" Starting with the k-th list in L,
	adds letters to the current string s
	"""
	
	# SET A BREAKPOINT HERE and DEBUG!!
	if (k >= len(L) ):
	    print(s)
	else:
	    for i in range(0, len(L[k])):
		self.backTracking( k+1, L, s+L[k][i] )
	
        
