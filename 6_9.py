def IsBalanced(Node):
	return NumberOfLevels(Node)

def NumberOfLevels(node):
	if Node == None:
		return (True, 0)

	left_res = NumberOfLevels(Node.left)
	if left_res[0] == False:
		return (False, 0)
	right_res = NumberOfLevels(Node.right)
	
	if right_res[0] == False or abs(left_res[1] - right_res[1]) > 1:
		return (False, 0)
	
	return (True, max(left, right)+1)

---------------------------------

def IsBalancedNotUsingTuple(Node):
	if NumberOfLevels(Node) == -1:
		return False
	return True

def NumberOfLevels(node):
	if Node == None:
		return 0

	left_res = NumberOfLevels(Node.left)
	if left_res == -1:
		return -1

	right_res = NumberOfLevels(Node.right)
	
	if right_res == -1 or abs(left_res - right_res) > 1:
		return -1
	
	return max(left, right)+1

-----------------------------------
#Find next in-order node 

def FindSuccessorInBST(node):
	
	if node.right != None:
		return FindLeftLeaf(node.right)

	return FindParent(node)


def FindParent(node):

	if node.parent == None:
		return None

	if node.parent.left = node:
		return node.parent

	return FindParent(node.parent)

def FindLeftLeaf(node):

	if node.left == None:
		return node
	return FindLeftLeaf(node.left)

------------------------

# Given 2 nodes, find first ancestor. Not BST

def FindAncestor(head, node1, node2):
	return CheckNode(head, node1, node2)[1]

def CheckNode(cur, node1, node2):
	
	if cur == None:
		return(0, None)
	res1 = 0
	res2 = 0	
	if cur == node1: 
		res1 = 1 # first node found

	if cur == node2:
		res2 = 2 # second node found

	res = res1 + res2
	if res == 3:
		return (res, cur)
	
	resleft = Check(cur.left, node1, node2)
	if resleft[0] == 3:
		return resleft 
		
	resright = Check(cur.right, node1, node2)
	if resright[0] == 3:
		return resright 
	
	search_result = res + resleft[0] + resright[0]

	if search_result == 3: #both nodes found
		return(search_result, cur)

	return(search_result, None)
		
		














