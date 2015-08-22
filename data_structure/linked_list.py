#coding:utf-8

'''
	singly linked list
'''

class Node(object):
	
	__slots__ = {'value', '__next'}

	def __init__(self, value=None):
		self.value = value
		self.__next = None

	@property
	def next(self):
		return self.__next

	@next.setter	
	def next(self, x):
		self.__next = x


class LinkedList(object):
	__slots__ = {'__first', '__last', '__size'}

	def __init__(self, seq=None):
		self.__first = None
		self.__last = None
		self.__size = 0

		if seq is None:
			return 

		for item in seq:
			node = Node(item)

			if self.__first is None: # the list is None
				self.__first = node
			else:
				self.__last.next = node
			self.__last = node
			self.__size += 1
		self.__last.next = None	

	#return thr first node of list
	def first(self):
		return self.__first

	#return thr last node of list
	def last(self):
		return self.__last

	#return thr size of list
	def size(self):
		return self.__size

	# Return the index in the list of the first item whose value is x. It is an error if there is 
	# no such item
	def index(self, x):
		current = self.__first
		index = 0
		while current is not None:
			if current.value == x:
				return index
			current = current.next
			index += 1
		raise ValueError('{0} not in the list'.format(x)) #future	


	# Add an item to the right of the list
	def appendright(self, x):
		node = Node(x)
		if self.__first is None: # The list is None
			self.__first = node
		else:
			self.__last.next = node 
		self.__last = node
		self.__size += 1

		return node

	# Add an item to thr first of the list
	def appendleft(self, x):
		node = Node(x)
		node.next = self.__first
		self.__first = node		
		self.__size += 1
		return node			

	# Add an item to the end of the list	
	def append(self, x):
		return self.appendright(x)


	# Extend the list by appending all the items in the given seq
	# seq need to have attribute __iter__
	def extend(self, seq):
		if not hasattr(seq, '__iter__'):
			raise TypeError('the given object is not iterable')
		for value in seq:
			self.appendright(value)
		return self


	# Remove the first left item in the list, and return it.
	def popleft(self):
		if self.__first is None:
			raise IndexError('pop from empty list')
		node = self.__first
		self.__first = node.next
		self.__size -= 1
		return node.value


	# Remove the first right item in the list, and return it.
	# singly linked link is so trouble in this method
	def popright(self): 
		if self.__last is None:
			raise IndexError('pop from empty list')
		if self.__last is self.__first: # Only one item
			return self.popleft()
		current = self.__first
		while current.next.next:
			current = current.next
		node = current.next
		current.next = None
		self.__size -= 1
		return node.value
		

	# Remove the item at the given position in the list, and return it.
	# If no index is specified, a.pop() removes and returns the last item in the list.
	# Note : Don't support a positive index 
	def pop(self, index=None):

		if index is None: # not give position parameter
			return self.popright()
		if not isinstance(index, int):
			raise TypeError('an positive integer is required')	
		if index < 0:
			raise TypeError('an positive integer is required')	
		if index == 0:
			return self.popleft()

		current = self.__first
		prev = current
		for _ in range(index):
			prev = current
			current = current.next
			if current is None:
				raise IndexError('pop index out of range')

		prev.next = current.next
		self.__size -= 1
		return current.value

	# Insert an item at a given position.
	# Note : Don't support a positive index 
	def insert(self, index, x):

		if not isinstance(index, int):
			raise TypeError('an positive integer is required')
		if index < 0:
			raise TypeError('an positive integer is required')	
		if index == 0:
			return self.appendleft(x)
		if index == self.size():
			return self.appendright(x)

		current = self.__first
		prev = current	
		for _ in range(index):
			prev = current
			current = current.next
			if current is None:
				raise IndexError('insert position out of range')

		node = Node(x)
		node.next = prev.next 
		prev.next = node
		self.__size += 1
		return x

	# Return the number of times x appears in the list.
	def count(self, x):
		current = self.__first
		cnt = 0
		while current:
			if current.value == x:
				cnt += 1
			current = current.next
		return cnt


	def __str__(self):
		return '->'.join(str(x) for x in self)

	def __iter__(self):
		current = self.__first
		while current:
			yield current.value
			current = current.next

	def __getitem__(self, index):
		return self._nodeat(index).value
		

	def __setitem__(self, index, value):
		self._nodeat(index).value = value



	# find an node by the given index in the list
	def _nodeat(self, index):
		current = self.__first
		for _ in range(index):
			current = current.next
			if current is None:
				raise IndexError('the given index out of range')
		return current	
						
	

if __name__ == '__main__':
	llist = LinkedList([1,2,3])
	print llist.size()
	print llist
	# print llist.first().value	
	# print llist.append(2).value
	# llist.append(3)
	# print llist
	# print llist.index('a')
	print llist.pop(0)
	print llist
	llist.insert(1,1)
	print llist
	print llist[0]
	llist[2] = 9
	print llist
	llist.append([1,2,3])
	llist.append(9)
	print len(llist[3])

	print llist.extend([1,2,3])
	print llist.extend((1,2,3))
	# print llist.extend(1)
	llist_tmp = LinkedList([1])
	print llist.extend(llist_tmp)
	print llist.count(1)



	

