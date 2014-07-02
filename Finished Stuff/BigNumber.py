from random import randint
from time import time

class LinkedList(object):
	"""
	LinkedList (without node implementation) to manipulate numbers larger than 10**maxSize.
	All functionality of shifting and addition built into list, as opposed to BigNumber.
	NOTE: First slot of list is last "chunk" of BigNumber. Designed as such for easier addition.
	"""
	# Personal descision to store the max length constant of any "int" storage
	# inside the LinkedList, not the BigNumber itself. Note: the BigNumber will
	# grab this value on construction.
	maxSize = 9
	maxInt = 10**maxSize


	"""
	Initializes with a defaulting value of 0, or a value passed in as string or int.
	NextIndex of list is initialized with a marker value for emptiness (currently 0).
	"""
	def __init__(self, data=0):
		self.data = int(data)

		self.nextIndex = 0


	"""
	Main method to add values to list. Using recursion, will add data as the current slot's data if
	empty and recursively call append on its nextIndex if not - note if nextIndex == 0 (marker value)
	then it will simply set it to a new LinkedList with the data.
	"""
	def append(self, data):
		if self.data == 0: # If nothing in data
			self.data = int(data) # Store value in

		elif self.nextIndex == 0: # If at end of list
			self.nextIndex = LinkedList(data) # Extend list by list-ception

		else:
			self.nextIndex.append(data) # Recursion through to the end

	"""
	Recursive method to iterate over list and return the formatted string. List Comprehension used to fill in any
	missing values of any index's data (ie. number = 4321, converts to 00004321).
	Then strips 0's off the left for proper output.
	"""
	def __str__(self):
		if self.nextIndex != 0:
			return ( str(self.nextIndex) + "".join(["0" for i in range(self.maxSize-len(str(self.data)))]) + str(self.data) ).lstrip("0")
		else:
			return ( "".join(["0" for i in range(self.maxSize-len(str(self.data)))]) + str(self.data) ).lstrip("0")
	"""
	Override of + operator, calling a recursive function. Separate method is called for recursion
	for easier implementation of future case catching.
	"""
	def __add__(self, other):
		return self.recurAdd(other)

	"""
	Recursive addition. Much case catching to handle cases of uneven lengths of lists.
	"""
	def recurAdd(self, other, newList=None, carry_one=0):
		if newList == None: # Defaulting to a new LinkedList
			newList = LinkedList()

		listSlot = self.data + other.data + carry_one # Data to be put onto newList next

		if listSlot >= self.maxInt: # If the value is too large for one int
			newList.append(listSlot%self.maxInt) # Remove the first number (via %) and append
			carry_one = 1 # Marker var for needing to carry 1
		else:
			newList.append(listSlot)
			carry_one = 0



		if self.nextIndex == 0 and other.nextIndex == 0: # If both lists are iterated out
			newList.append(carry_one) # Just add the 1 onto the front of the list (remember 0 will act as an empty list)
			return newList # Returns the newList back through the recursion

		elif self.nextIndex == 0: # If self has run out of values but other has yet more
			newList.append_dump(other.nextIndex, carry_one) # Dump the values of other into newList
			return newList # Returns the newList back through the recursion

		elif other.nextIndex == 0: # If other has run out of values but self has yet more
			newList.append_dump(self.nextIndex, carry_one) # Dump the values of self into newList
			return newList # Returns the newList back through the recursion

		else:
			return self.nextIndex.recurAdd(other.nextIndex, newList, carry_one) # Recursion call with returning back


	"""
	Dumps all data from one list into the list this method is called on. Accepts a optional
	argument of the case of needing to carry one (from addition).
	"""
	def append_dump(self, dumpingList, leftOverData=0):
		self.append(dumpingList.data+leftOverData)

		if dumpingList.nextIndex != 0:
			self.append_dump(dumpingList.nextIndex)

	"""
	Arithmetic left-shift. Will add a 0 onto the far right of the first number slot, and carry the 
	overflow values up through the list. Uses recursion to do so. Default value of 0 for addTo for initial
	call, and explicit from then on.
	"""
	def shift_left(self, addTo=0):
		takenOff = self.data // 10**(self.maxSize-1) # Stores the value that will be taken off
		self.data = ( self.data % 10**(self.maxSize-1) * 10 )  + addTo # Takes off that value and "shifts" it by *10
		if self.nextIndex != 0:
			self.nextIndex.shift_left(takenOff)
		else:
			self.append(takenOff)
	
	"""
	Arithmetic right-shift. Uses takenOff to store the value that will be truncated, and recurses down to the bottom
	before returning those values back up, adding it on as necessary.
	"""
	def shift_right(self):
		if self.nextIndex != 0:
			takenOff = self.data % 10 # Value to be truncated
			self.data = (self.data // 10) + (10**(self.maxSize-1))*self.nextIndex.shift_right() # Truncating value and then adding 
																								# on the value of the previous truncation
		else:
			takenOff = self.data % 10 # Value to be truncated
			self.data = self.data // 10 # If at the end, just truncate

		return takenOff

class BigNumber(object):
	"""
	Shell class for LinkedList. Allows for minimal interaction and almost entirely passes on method calls to 
	the internal stored LinkedList.
	"""
	maxSize = -1 # Initialized and actual value stolen from LinkedList

	"""
	Almost the entirety of BigNumber, initializes and constructs the LinkedList storage.
	"""
	def __init__(self, s="0"):
		if type(s) == LinkedList: # If passed value is already in the correct form, just store and done.
			self.list = s 
			self.maxSize = self.list.maxSize # Fetch the maxSize from LinkedList class

		else:
			self.list = LinkedList() # Make new List
			self.maxSize = self.list.maxSize # Fetch the maxSize from LinkedList class

			if s == "": # If an empty string is passed, defaults to "0"
				s = "0"

			if len(s) % self.maxSize == 0: # If the input string will fit perfectly into a LinkedList
				for i in range(len(s)/self.maxSize, 0, -1): # Iterates backwards - front of list is back of number
					self.list.append(s[self.maxSize*(i-1):self.maxSize*(i)]) # Append with slicing

			else:
				leftOver = len(s) % self.maxSize # The "extra" that doesn't fit exactly with the LinkedList

				for i in range((len(s)-leftOver)/self.maxSize, 0, -1): # Iterates through backwards - back of List is front of number
					self.list.append(s[(self.maxSize*(i-1))+leftOver:(self.maxSize*(i))+leftOver]) # Uglier slicing to incorporate the leftOver

				self.list.append(s[:leftOver])
				
	"""
	Passes the call on to the LinkedList - easier implementation. Case-catching for the special case of list only containing
	0's (necessary due to the .lstrip("0") from __str__ in LinkedList)
	"""
	def __str__(self):
		if self.list.data == 0:
			string = "0"
		else:
			string = str(self.list)
		return string

	"""
	Passes the call on to the LinkedList, with case catching.
	"""
	def __add__(self, other):
		if self.list.data == 0 and other.list.data == 0: # If both lists are 0, then return
			result = 0
		elif (self.list.data != 0 and other.list.data != 0): # If neither are 0, then add as normal
			result = self.list + other.list
		elif self.list.data != 0: # If self is empty, then return the other
			result = str(self.list)
		elif other.list.data != 0: # If other is empty, return self
			result = str(other.list)

		return BigNumber(str(result)) # Convert answer to BigNumber and return
	

	"""
	Passes call on to LinkedList (no case catching necessary - yet)
	"""
	def shift_left(self):
		return self.list.shift_left()

	"""
	Passes call on to LinkedList (no case catching necessary - yet)
	"""
	def shift_right(self):
		return self.list.shift_right()


def main():
	for i in range(10000):
		numStr1 = "".join([str(randint(0,9)) for x in range(randint(0,50))])
		numStr2 = "".join([str(randint(0,9)) for x in range(randint(0,50))])
		
		BN1 = BigNumber(numStr1)
		BN2 = BigNumber(numStr2)

		if len(numStr1) == 0:
			numStr1 = "00"
		if len(numStr2) == 0:
			numStr2 = "00"
		L1 = long(numStr1)
		L2 = long(numStr2)
		


		print "\nStart: %s" % BN1

		BN1.shift_right()
		BN1.shift_left()
		BN1.shift_right()

		print "End:   %s" % BN1
		print "Wanted:%s" % numStr1[:-1]



		print "\nStart: %s" % BN2

		BN2.shift_left()

		print "End:   %s" % BN2
		print "Wanted:%s" % (numStr2+"0")



		n = 2

		iTime = time()
		for i in range(n):
			BN3 = BN1 + BN2
		print "\nTime for %i additions of BigNumber: " %n, time() - iTime

		iTime = time()
		for i in range(n):
			L3 = L1 + L2
		print "Time for %i additions of Long: " %n, time() - iTime



		print "\nGot:     %19s" % (BN1 + BN2)
		print "Wanted:  %19s" % (int(numStr1)/10 + int(numStr2+"0"))

		if str(BN1 + BN2) == str(int(numStr1)/10 + int(numStr2+"0")):
			print "\nSuccess.\n"
		else:
			print "\n\nNOPE.\n\n"
			break # Breaking out of the 10000 tests.



if __name__ == '__main__':
	main()