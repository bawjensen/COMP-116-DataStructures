from SampleStuff import *

# assuming Python v2.7 (see notes below)

def main():
	
	# make a new object
	stuff = SampleStuff("SampleFile.txt")
	
	
	n = 23
	print "\nIn main(): before passBy n = %d" % (n)
	stuff.passBy(n)
	# nope, Python arguments are pass-by-value 
	print "In main(): after  passBy n = %d\n" % (n)
	# NOTE: if an argument is a mutable object (e.g., a list)
	#       then the argument's contents *do* change 
	
	
	a = 3
	b = 5
	print "In main(): before BasicMath a = %d and b = %d" % (a,b)
	stuff.basicMath(a,b)
	print "In main(): after BasicMath  a = %d and b = %d\n" % (a,b)
	
	print "\n=========================================="
	print "Test FileIO ...\n"
	stuff.fileIO()
	
	print "\n=========================================="
	print "Test making a dictionary of (word, count) pairs ...\n"
	stuff.makeDictionary()
	
	
	print "\n=========================================="
	print "Test 'pickling' a dictionary data structure ...\n"
	stuff.pickle_saveToFile()
	
	print "\n=========================================="
	print "Test loading a pickled data structure ...\n"
	stuff.pickle_loadFromFile()
	
	for nextKey in stuff.WordCounts.keys():
	    print "%s:\t%d" % (nextKey, stuff.WordCounts[nextKey])
	print "\n"
	

		
	# SET A BREAKPOINT HERE and DEBUG!!
	print("\n==========================================")
	print("Test Backtracking ...\n")
	#------------------------------------------------
	# Test your knowledge of recursive backtracing
	S = [ 'c', 's', 'v' ]
	V = [ 'a', 'e', 'i', 'o', 'u' ]
	E = [ 'd', 't', 'w' ]
	
	# list of lists (or 2D array)
	L = [S,V,E]
	
	stuff.backTracking( 0, L, "")
	
	
	
	


#-----------\
# START HERE \
#-----------------------------------------------------------	
if __name__ == '__main__':
	main()

#-----------------------------------------------------