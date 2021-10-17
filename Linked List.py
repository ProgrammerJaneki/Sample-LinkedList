#LinkedList - sequence of nodes where each node stores own data and link to the next node
class Node:
	def __init__(self, data, nextt):
		self.data = data
		self.nextt = nextt

class LinkedList:
	def __init__(self): 
		self.head = None

	def add_at_front(self, data):
		self.head = Node(data, self.head)

	def add_at_end(self, data):
		if not self.head:
			self.head = Node(data, None)
			return

		curr = self.head
		while curr.nextt:
			curr = curr.nextt
		curr.nextt = Node(data, None)

	def get_length(self):
		counter = 0
		current = self.head
		while current:
			counter += 1
			current = current.nextt

		return counter

	def remove_at(self, index):
		index = index - 1
		if index < 0 or index >= self.get_length():
			print("Invalid Index")
		elif index == 0:
			self.head = self.head.nextt 
			#It will point the head of your linked list to the next one
			#Python deletes unwated objects so the initial head of the linked list will be free from the memory space
			return
		else:
			count = 0
			current = self.head
			while current:
				if count == index -1:
					current.nextt = current.nextt.nextt
					break
				current = current.nextt
				count += 1

	def add_at(self, index, data):
		index = index - 1
		if index < 0 or index > self.get_length():
			print("Invalid Index")
		elif index == 0:
			self.add_at_front(data)
			return
		else:
			count = 0
			current = self.head
			while current:
				if count == index -1:
					node = Node(data, current.nextt)
					current.nextt = node
					break
				current = current.nextt
				count += 1

	def print_list(self):
		if self.head is None:
			print("List is empty")
		else:
			current_node = self.head
			while current_node != None:
				print(current_node.data, end = " => ")
				current_node = current_node.nextt
			print()
			
			
			
