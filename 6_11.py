Generate execution order of projects

class Node:
	def __init__(self, id):
		self.id = id
		self.isroot = False
		self.visited = False
		self.children = []

	def AddChild(self, child):
		self.children.append(child)

class Context:
	def __init__():
		ids = ()

def Execution order(ids, edges = tuple()):
	
	ctx = Context()
	
	for id in ids:
		if ctx.ids.haskey(id) == False:
			ctx[id] = Node(id)
		
	for edge in edges:
		ctx.ids[edge[0]]


----------------------------------------
One tree is a subtree of another

def FindRoot2(t1, t2):

	res = None

	if t1 == None:
		return None
	if TreesAreIdentical(t1, t2) == True:
		return t1

	res = FindRoot(t1.left, t2)
		if res != None:
			return res
	res = FindRoot(t1.right, t2)
	return res

def IsSubTree(t1, t2):

	if t1 == None or t2 == None:
		exception
	
	root = FindRoot(t1, t2)

	if root != None:
		return True
	return False


def TreesAreIdentical(t1, t2):	
	
	if t1 == None and t2 == None:
		return True
	elif t1 == None or t2 == None or t1.data != t2.data:
		return False

	res = TreesAreIdentical(t1.left, t2.left)
	if res == False:
		return False
	return TreesAreIdentical(t1.right, t2.right)


-------------------------------------
One tree is a subtree of another using hash

def CalculateAndCompareHash(t, t2, t2_hash):
	if t == None:
		return (0, False)
	
	left = CalculateAndCompareHash(t.left, t2_hash)
	if left[1] == True:
		return left

	right = CalculateAndCompareHash(t.right, t2_hash)
	if right[1] == True:
		return right

	res = t.data + left[0] + right[0]
	if res == t2_hash and  and TreesAreIdentical(t, t2):
		return (res, True)
	
	return res, False

def CalculateHash(t):
	if t == None:
		return 0
	
	return t.data + CalculateHash(t.left) + CalculateHash(t.right)

def IsSubTreeHash(t1, t2):
	if t2 == None:
		return True

	t2_hash = CalculateHash(t2)

	return CalculateAndCompareHash(t1, t2, t2_hash)[1]
	






















	