In a directed graph determine whether there is a path between 2 nodes.

class Node:
	data
	arr()
	visited

def PathInGraphBetween2Nodes(Node1, Node2):
	
	for nd in Node1.arr:
		if nd.visited == 1:
			continue
		nd.visited = 1	

		if nd == Node2:
			return True
		res = PathInGraphBetween2Nodes(nd, Node2)	
		if res == True:
			return True

	return False

visited = {}
def PathInGraphBetween2Nodes(Node1, Node2, visited):
	
	for nd in Node1.arr:
		if nd in visited:
			continue
		visited += nd	

		if nd == Node2:
			return True
		res = PathInGraphBetween2Nodes(nd, Node2)	
		if res == True:
			return True

	return False

--------------------------------------------------

class Node:
	left: Node
	right: Node

def CreateBinarySearchTreeFromArray(arr, begin, end):

	middle_node = Node()
	
	if begin == end:
		middle_node.data = arr[begin]
		return middle_node

	middle = (end + begin) / 2

	middle_node.data = arr[middle]
	
	if begin != middle:
		middle_node.left = CreateBinarySearchTreeFromArray(arr, begin, middle-1)

	if end != middle:
		middle_node.right = CreateBinarySearchTreeFromArray(arr, middle+1, end)
	
	return middle_node 

--------------------------------------------------

Given a binary tree. Create a linked list for all notes of each depth

class List_Node:
	tree_node:node
	next = none

def LinkedListsFromBiTree(node, counter, arr)

	list_node = List_Node() 	
	list_node.tree_node = node
	if counter + 1 > len[arr]:
		arr.append(list_node)
	else:
		list_node.next = arr[counter]
		arr[counter] = list_node

	if node.left != None:
		LinkedListsFromBiTree(node.left, counter+1, arr)
	if node.right != None:
		LinkedListsFromBiTree(node.right, counter+1, arr)

	---------------- without recursion ---------------


def LinkedListsFromBiTree(node):

	arr = []
	list_node = List_Node()
	list_node.tree_node = node

	arr.append[list_node]

	depth = 0	
	
	while depth+1 <= len(arr):

		depth_list = arr[depth]
		depth += 1

		while True:

			list_node_left = List_Node()
			list_node_left.tree_node = node.left

			list_node_right = List_Node()
			list_node_right.tree_node = node.right
			list_node_right.next = list_node_left

			if len(arr) = 
			arr.append[list_node_right]
	





	
	list_node = List_Node() 	
	list_node.tree_node = node
	if counter + 1 > len[arr]:
		arr.append(list_node)
	else:
		list_node.next = arr[counter]
		arr[counter] = list_node

	if node.left != None:
		LinkedListsFromBiTree(node.left, counter+1, arr)
	if node.right != None:
		LinkedListsFromBiTree(node.right, counter+1, arr)

	









































































