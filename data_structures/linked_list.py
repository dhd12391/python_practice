#Practicing Linked List 

class Node():
	def __init__(self, value, node=None):
		self.value = value 
		self.next = node

class LinkedList():
	def __init__(self, head):
		self.head = head 	#head node ref. nodes list

	def add_node_to_end(self, node):
		curr = self.head
		while(curr.next is not None):
			curr = curr.next
		curr.next = node

if __name__ == "__main__":
	head_node = Node(1)
	linked_list = LinkedList(head_node)
	linked_list.add_node_to_end(Node(2))


