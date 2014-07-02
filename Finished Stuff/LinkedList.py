class LinkedList(object):
	def __init__(self):
		self.head = LLNode()

class LLNode(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None