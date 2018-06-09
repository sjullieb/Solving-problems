
class Node
	right
	left
	data

def IsBST(node, minleft, maxright):
	if node == None:
		return False	

	if node.left !=  None:
		if node.left.data <= minleft or node.left.data >= node.data:
			return False 	
		
		if IsBST(node.left, minleft, node.data) == False:
			return False

	if node.right !=  None:
		if node.right.data <= node.data or node.right.data >= maxright:
			return False 	
		
		if IsBST(node.right, node.data, maxright) == False:
			return False
	
	return True
    
----------------------
class Node
	data: 
	next: Node

def MergeLinkedLists(l1, l2):

	if l1 == None:
		return l2
	if l2 == None:
		return l1

	if l1.data > l2.data:
		l1.next = MergeLinkedLists(l1.next, l2)
		return l1	
	else:
		l2.next = MergeLinkedLists(l1, l2.next)
		return l2
---------------------	

def MergeLinkedLists(l1, l2):

	if l1 == None:
		return l2
	if l2 == None:
		return l1

	if l1.data > l2.data:
		head = l1
		l1 = l1.next	
	else:
		head = l2
		l2 = l2.next

	cur = head

	while l1 != None or l2 != None:
		
		if l2.data > l1.data: 
			tmp = l1
			l1 = l2
			l2 = tmp

		cur.next = l1
		cur = cur.next
		l1 = l1.next

			

	if l1 == None:
		cur.next = l2
	else l2 == None:
		cur.next = l1
	return head

-----------------------------
Return lists of all nodes on each depth

class ListNode:
	data: TreeNode
	next: ListNode
class NodesList
	def __init__(self):	
		first = None
		current = None

	def AddListNode(self, treenode):
		newListNode = ListNode()
		newListNode.next = self.first
		self.first = newListNode				

	def GetFirst(self):
		return self.first

	def GetStart(self):
		self.current = self.first
		return self.current

	def GetNext(self):
		self.current = self.current.next
		return self.current

def NodesOfEachDepth(Node):
	if Node == None:
		return None 
	
	arr = []
	
	head = NodesList()
	head.AddListNode(Node)
	arr.append(head)

	while True: 
		
		currentList = arr[len(arr) - 1]
		cur = currentList.GetStart
		newList = NodesList()
		while cur != None:
			if cur.data.left != None:
				newList.AddListNode(cur.data.left) 
			if cur.data.right != None:
				newList.AddListNode(cur.data.right) 
			cur = currentList.GetNext
		
		if newList.GetFirst != None:
			arr.append(newList)
		else
			break

	return arr












