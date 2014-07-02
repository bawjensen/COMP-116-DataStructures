class LLNode(object):
	"""
	Node class for LinkedList object.
	"""
	def __init__(self, data=None):
		# Cargo
		self.data = data
		# Link / Pointer
		self.next = None

class SimpleList(object):
	"""
	Simpler version of LinkedList object. Differs in __str__ representation.
	Singly-linked, uses head and tail pointers, uses length counter instead of method.
	"""
	def __init__(self):
		self.head = LLNode()
		self.empty = True
		self.length = 0
		self.tail = self.head

	def append(self, data):
		"""
		Method to add items to list. Uses tail to append items.
		Returns nothing.
		"""

		if self.head.data == None:
			self.head.data = data
		else:
			self.tail.next = LLNode(data)
			self.tail = self.tail.next

		if self.head.data != None:
			self.empty = False

		if data != None:
			self.length += 1

	def append_list(self, linked_list, time):
		"""
		Method to take one LinkedList and append to another. Calls append method.
		Returns nothing.
		"""
		for i in xrange(linked_list.length):
			self.append( (time, linked_list[i]) )


	def pop_first(self):
		"""
		Method to remove and return first item of the list.
		"""
		removed, self.head = self.head.data, self.head.next

		if self.head == None or self.head.data == None:
			self.empty = True

		self.length -= 1

		return removed

	def __getitem__(self, index):
		"""
		Overload for indexing.
		Returns the value at the index.
		"""
		if index >= self.length:
			raise IndexError

		node = self.head
		for i in xrange(index):
			node = node.next

		return node.data

	def __setitem__(self, index, data):
		"""
		Overload for index setting.
		Returns nothing.
		"""
		if index >= self.length:
			raise IndexError

		node = self.head
		for i in xrange(index):
			node = node.next

		node.data = data

	def __str__(self):
		"""
		Formatted output for a list of single items.
		Returns the buffered string.
		"""
		node = self.head
		buff = "["

		while node != None:
			buff += "%s, " % node.data
			node = node.next

		buff = buff.strip(", ")
		buff += "]"

		return buff


class LinkedList(SimpleList):
	"""
	Inherits from SimpleList, overrides only the __str__ method.
	"""
	def __str__(self):
		"""
		Formatted output for a data of a two-tuple.
		Returns the buffered string.
		"""
		node = self.head
		buff = "["

		while node != None:
			buff += "(%s, %s), " % node.data
			node = node.next

		buff = buff.strip(", ")
		buff += "]"

		return buff

#===============================================================================

class ProcessScheduler(object):
	"""
	Class to simulate the process scheduler of a CPU. Can take in variables to add to an
	internal LinkedList for later running. Implements an internal clock.
	"""
	def __init__(self):
		self.clock = 0
		self.list = LinkedList()

	def add_process(self, data):
		"""
		Added processes are appended to the internal LinkedList. Returns nothing.
		"""
		self.list.append(data)

	def run_processes(self, policy, quantumSize=0):
		"""
		Takes the parameter of policy, and if Round Robin, quantumSize parameter also needed.
		"""
		if policy.lower() == "fifo":
			while not self.list.empty:
				self._run(self.list.pop_first())

		elif policy.lower() == "rr":
			while not self.list.empty:
				leftOver = self._run(self.list.pop_first(), limitLen=quantumSize)
				if leftOver != None:
					self.list.append(leftOver)

		elif policy.lower() == "spn":
			self.list = binary_tree_sort(self.list)
			print "Sorted."
			while not self.list.empty:
				self._run(self.list.pop_first())

	def _run(self, data, limitLen=0):

		if limitLen == 0:
			self.clock += data[0]
		else:
			data = (data[0]-limitLen, data[1])
			if data[0] < 0:
				self.clock += limitLen + data[0]
				data = (0, data[1])
			else:
				self.clock += limitLen


		if data[0] > 0:
			#FOUT.write("Data: %6s (tS: %3s) Lim: %i Time: %i.\n" % (data[1], data[0], limitLen, self.clock))
			#FOUT.write("%i\n" % self.clock)
			return data
		else:
			#FOUT.write("Data: %6s (tS: %3s) Lim: %i Time: %i.\n" % (data[1], data[0], limitLen, self.clock))
			FOUT.write("%i\n" % self.clock)
			return None

#===============================================================================

def binary_tree_sort(linked_list):
	b_tree = BinaryTree()

	while not linked_list.empty:
		b_tree.insert(linked_list.pop_first())

	sorted_linked_list = b_tree.list_sort()

	return sorted_linked_list

class BTreeNode(object):
	def __init__(self, time, process):
		self.cargo_time = time
		self.cargo_processes = SimpleList()
		self.cargo_processes.append(process)
		self.left = None
		self.right = None

	def __str__(self):
		return "%s-%s" % (self.cargo_time, self.cargo_processes)

class BinaryTree(object):
	def __init__(self):
		self.root = None

	def insert(self, t):
		time = t[0]
		process = t[1]

		if self.root == None:
			self.root = BTreeNode(time, process)
			return

		node = self.root

		inserted = False
		while not inserted:
			if node.cargo_time == time:
				node.cargo_processes.append(process)
				inserted = True

			elif node.cargo_time > time:
				if node.left == None:
					node.left = BTreeNode(time, process)
					inserted = True
				else:
					node = node.left

			elif node.cargo_time < time:
				if node.right == None:
					node.right = BTreeNode(time, process)
					inserted = True
				else:
					node = node.right

	def list_sort(self):
		buff_list = LinkedList()

		self._recur_sort(buff_list, self.root)

		return buff_list

	def _recur_sort(self, buff_list, node):
		if node.left != None:
			self._recur_sort(buff_list, node.left)
			buff_list.append_list(node.cargo_processes, node.cargo_time)
			if node.right != None:
				self._recur_sort(buff_list, node.right)
		else:
			buff_list.append_list(node.cargo_processes, node.cargo_time)
			if node.right != None:
				self._recur_sort(buff_list, node.right)





#===============================================================================


def quicksort(L, listStart=0, listEnd=None):
	if listEnd == None:
		listEnd = L.length - 1

	if listStart < listEnd:
		index = listStart + (listEnd-listStart) / 2

		newIndex = partition(L, listStart, listEnd, index)

		quicksort(L, listStart, newIndex - 1)

		quicksort(L, newIndex + 1, listEnd)

#===============================================================================

def partition(L, start, end, index):
	splitterValue = L[index]
	L[index], L[end] = L[end], L[index]

	place = start

	for i in range(start, end):
		if L[i] < splitterValue:
			L[i], L[place] = L[place], L[i]
			place += 1

	L[place], L[end] = L[end], L[place]

	return place

#===============================================================================

def main():
	
	fileName = "programsMine_4.txt"

	pScheduler = ProcessScheduler()

	f = open(fileName, 'r')

	for line in f:
		line = line.strip()
		line = line.split(",")
		pScheduler.add_process( (int(line[1]), line[0]) )

	pScheduler.run_processes(policy="rr", quantumSize=200)

if __name__ == '__main__':
	FOUT = open("outputMeanTime.csv", "w")
	main()
	FOUT.close()