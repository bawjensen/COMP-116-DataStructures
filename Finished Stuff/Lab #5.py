from random import randint

class Node(object):
	def __init__(self, item=None):
		self.item = item
		self.next = None

class Sequence(object):
	def __init__(self):
		self.head = Node()
		self.tail = self.head
		self.length = 0

	def __str__(self):
		outStr = "["
		node = self.head

		for i in range(self.length):
			outStr += "%s," % str(node.item)
			node = node.next

		outStr.strip(",")

		outStr += "]"

		return outStr

	def append(self, data):
		if self.head.item == None:
			self.head.item = data
		else:
			self.tail.next = Node(data)
			self.tail = self.tail.next

		self.length += 1

	def pop(self):
		removed, self.head = self.head, self.head.next
		self.length -= 1
		return removed.item

class List(Sequence):
	pass
	
class Queue(Sequence):
	
	def enqueue(self, data):
		self.append(data)

	def dequeue(self):
		return self.pop()
	
class Stack(Sequence):

	def push(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node
		self.length += 1


def main():
	Q = Queue()

	print Q

	Q.enqueue(5)

	print Q

	print Q.dequeue()

	"""	Q = Stack()
	W = List()
	E = Queue()

	for i in range(10000):

		Q.push(randint(0,10000))
		W.append(randint(0,10000))
		E.enqueue(randint(0,10000))

	for i in range(Q.length):
		print Q.pop()
		print E.dequeue()

	print W"""




if __name__ == "__main__":
	main()