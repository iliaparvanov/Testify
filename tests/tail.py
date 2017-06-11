class InvalidNodeError(Exception):
	def __init__(self):
		super().__init__('Attempting to enqueue a None value to the queue is forbidden.')

class Queue:
	def __init__(self):
		self.head = self.tail = None
		self.size = 0
		
	class Node:
		def __init__(self, value):
			self.value = value
			self.prev = None
			
	def enqueue(self, value):
		if value == None:
			raise InvalidNodeError
			
		new_node = Queue.Node(value)
		
		if self.is_empty():
			self.head = self.tail = new_node
		else:
			self.tail.prev = new_node
			self.tail = new_node
			
		self.size += 1
		
	def dequeue(self):
		dequeued_value = None
		
		if self.is_empty():
			dequeued_value = None
		elif self.size == 1:
			dequeued_value = self.head.value
			self.head = self.head.prev
			self.tail = None
		else:
			dequeued_value = self.head.value
			self.head = self.head.prev
			
			
		self.size = (self.size - 1) if self.size > 0 else 0
		
		return dequeued_value
		
	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.head.value
		
	def clear(self):
		self.head = self.tail = None
		self.size = 0
		
	def __iter__(self):
		return Queue.Iterator(self)
		
	class Iterator:
		def __init__(self, queue):
			self.queue = queue
			
		def __next__(self):
			dequeued_value = self.queue.dequeue()
			if dequeued_value == None:
				raise StopIteration
			else:
				return dequeued_value
		
	def __len__(self):
		return self.size
		
	def is_empty(self):
		return self.head == None and self.tail == None
			
def print_queue(q):
	current = q.head
	if current == None:
		return
		
	while current != None:
		print(current.value)
		current = current.prev

def print_info(msg, q):
	print(msg)
	print('queue size: {}'.format(len(q)))
	print_queue(q)
	print()

def dequeue_q(q):
	for value in q:
		print('dequeued: {}'.format(value))

