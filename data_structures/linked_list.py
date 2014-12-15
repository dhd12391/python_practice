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
		node.next = curr.next
		curr.next = node

	def print_LL(self):
		curr = self.head
		list_string = '['
		while curr is not None:
			list_string += str(curr.value)
			if curr.next != None:
				list_string += ','
			else:
				list_string += ']'
			curr = curr.next
		print list_string

	def nthElement(self, n):
		#2nd element = [1] (i.e. head.next)
		i = 1
		curr = self.head
		while i < n:
			curr = curr.next
			i += 1
		return curr

	def recursive_reverse(self,rev):
		pass

	def iterative_reverse(self):
		curr = LinkedList(self.head)
		last = None

		while curr is not None:
			next = curr.next
			curr.next = last
			last = curr
			curr = next
		return LinkedList(last)

if __name__ == "__main__":
	head_node = Node(1)
	linked_list = LinkedList(head_node)
	linked_list.add_node_to_end(Node(2))
	linked_list.print_LL()

	#linked_list.iterative_reverse().print_LL()
	print "%(n)dnd element in list: %(nthelement)d" %\
		{"n": 2, "nthelement": linked_list.nthElement(2).value}
	linked_list.print_LL()

