from random import randint
import re

class BigNumList(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None
	
	def __str__(self):
		return self.nice_printing()

	def append(self, data):
		if self.data == None:
			self.data = data
		elif self.next == None:
			self.next = BigNumList(data)
		else:
			self.next.append(data)

	def nice_printing(self):
		lenData = len(str(self.data))
		if lenData < MAX_SIZE:
			prefix = "0" * (MAX_SIZE-lenData)
		else:
			prefix = ""

		if self.next == None:
			return "[%s%s]" % (prefix,self.data)
		else:
			nextPiece = self.next.nice_printing()
			return ("[%s%s]," % (prefix,self.data)) + nextPiece

	def access(self, index):
		if index == -1:
			if self.next == None:
				return self.data
			else:
				return self.next.access(-1)

		if index > 0:
			if self.next == None:
				print "Index out of range, returning None."
				return None

			return self.next.access(index-1)

		else:
			return self.data

	def carry_the_one(self, index):
		if index > 0:
			if self.next == None:
				print "Index out of range, returning None."
				return None

			self.next.carry_the_one(index-1)

		else:
			self.data += 1

	def len(self, length=1):
		if self.next != None:
			return self.next.len(length+1)
		elif self.next == None and self.data == None:
			return 0
		else:
			return length

	def del_from_front(self, num, newListFront=None):
		# Default-correction
		if newListFront == None:
			newListFront = self

		if num != 0:
			return self.del_from_front(num-1, newListFront.next)

		else: #num == 0
			return BigNumber(str(newListFront))


class BigNumber(object):
	def __init__(self, s="0"):
		s = self.strip_and_clean_str(s)

		if len(s) <= MAX_SIZE:
			if s == "":
				s = "0"

			self.BNList = BigNumList(int(s))

		else:
			leftOver = len(s) % MAX_SIZE

			if s[:leftOver] != "":
				self.BNList = BigNumList(int(s[:leftOver]))
				newString = s[leftOver:]
			else:
				self.BNList = BigNumList(int(s[:MAX_SIZE]))
				newString = s[MAX_SIZE:]

			for i in range(len(s) / MAX_SIZE):
				if newString != "":
					self.BNList.append(int(newString[:MAX_SIZE]))
					newString = newString[MAX_SIZE:]

	def __str__(self):
		return "%s" % (re.sub('[\[\],]', "",self.BNList.nice_printing()).lstrip("0"))

	def __add__(self, other):
		lenSelf = self.BNList.len()
		lenOther = other.BNList.len()

		if lenSelf != lenOther:
			if lenSelf > lenOther:
				bigger, smaller = self, other

			else: #lenSelf < lenOther
				bigger, smaller = other, self

			resultBNList = self.add_diff_sizes(bigger, smaller)

		else:
			resultBNList = self.add_same_sizes(self, other)

		stringedList = "%s" % (re.sub('[\[\],]', "",resultBNList.nice_printing()))
		return BigNumber(stringedList)


	def add_diff_sizes(self, bigger, smaller):
		returnList = BigNumList()

		sizeDifference = bigger.BNList.len()-smaller.BNList.len()

		for i in range(sizeDifference):
			returnList.append(bigger.BNList.access(i))

		bigger = bigger.BNList.del_from_front(sizeDifference)

		self.add_same_sizes(bigger, smaller, returnList)

		return returnList


	def add_same_sizes(self, first, second, returnable=None):
		if returnable == None:
			returnable = BigNumList()

		retLen = returnable.len()
		adjustor = 0

		for i in range(first.BNList.len()):

			if first.BNList.access(i)+second.BNList.access(i) >= 10**(MAX_SIZE):
				if retLen + i == 0:
					returnable.append(1)
					adjustor = 1
				else:
					returnable.carry_the_one(retLen+adjustor+i-1)


				returnable.append((first.BNList.access(i) + second.BNList.access(i))%(10**(MAX_SIZE)))

			else:
				returnable.append(first.BNList.access(i) + second.BNList.access(i))

		return returnable

	def strip_and_clean_str(self, string):
		newString = ""
		for let in string:
			if let not in "[], ":
				newString += let

		return newString

def main():
	for blah in range(100000):
		stringForm1 = "361147363132794486"
		#stringForm1 = "".join([str(randint(0,9)) for x in range(randint(1,40))])
		print "SF1: " + stringForm1
		newBigNum = BigNumber(stringForm1)

		stringForm2 = "908233771910149261"
		#stringForm2 = "".join([str(randint(0,9)) for x in range(randint(1,40))])
		print "SF2: " + stringForm2
		newerBigNum = BigNumber(stringForm2)

		print
		print newBigNum
		print newerBigNum
		print

		answer = newBigNum + newerBigNum
		wantedAnswer = str(int(stringForm1) + int(stringForm2))

		print "Addition: " + str(answer)
		print "Wanted:   " + wantedAnswer

		print "Result: ", str(answer) == wantedAnswer
		if str(answer) != wantedAnswer:
			print "Oh no..."
			break

if __name__ == '__main__':
	MAX_SIZE = 9
	main()