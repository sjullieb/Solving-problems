--------------------------------------------
Dynamic Array

class DynamicArray
	arr : list
	length : int
	current_index : int

def Initialize(len)
	arr = new array[len]
	length = len
	current_index = 0

def AddElement(data):
	if current_index == length: 
		new_length = length * 2
		new_arr = new array[new_length]
		for i in range(current_index):
			new_arr[i] = arr[i]
		delete arr
		arr = new_arr
		length = length * 2

	arr[current_index] = data
	current_index += 1
--------------------------------------------
Define a class which represents array as a linked list of small arrays

class Node:
	value: array
	next: Node

class DynamicList
	first_el : Node
	last_el : Node
	current_index : int 
	length : int

def Initialize(length):
	first_el = new Node
	first_el.value = new array(length)
	first_el.next = null
	last_el = first_el
	current_index_in_one_arr = 0
	
def AddElement(data)
	if current_index_in_one_arr == length:
		new_el = new Node 
		new_el.value = new array(length)
		new_el.next = null

		last_el.next = new_el
		last_el = new_el
		current_index_in_one_array = 0	

	last_el.value[current_index_in_one_array] = data
	current_index_in_one_array += 1
		
def FindElement(index)
	num_array = int(index / length)
	actual_index = index % length
	
	arr_el = first_el
	for i = 1 in range(num_arr+1):
		if arr_el.next == NULL:
			exception
		arr_el = arr_el.next 
		
	return arr_el.value[actual_index]

-----------------------------------------------------
Breadth-First Search in graph

def BreadthFirstSearch(node, interface):
	que = queue()
	checked_nodes = set()
	cur_node = node	

	enque(node)
	cheched_nodes += node
	while que.empty() == False:
		cur_node = que.dequeue
		interface.call(cur_node)
		while True:
			next_node = cur_node.GetNextChild
			if next_node == null : break
			if next_node not in checked_nodes:
				que.enqueue(next_node)		
				checked_nodes += next_node

						
			







