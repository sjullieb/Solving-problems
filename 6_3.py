Generate 7 random numbers with 5 random number generator

def Generate:
	
	while True:
		try1 = rand()
		try2 = rand()
		
		res = (try1 - 1) * 5 + (try2 - 1) 
		if res < 21:
			break
			
	return res mod 7 + 1

-------------------------------------------

If a string has only unique characters

def UniqueChar(str):
	
	if len(str) > 256 :
		return False

	arr[0..255] = 0

	res = True
	for char in str:
		if arr[char] == 1:
			res = False
			break
		else 
			arr[char] = 1
	
	return res
--------------------------------------------------

def UniqueCharWithoutAdditionalDataStructure(str):

 	length = len(str)
	if  > 256:
		return False

	str.sort()

	prev = str[0]
	for char in str[1:length]:
		if prev == char:
			return False
		else:
			prev = char				

	return True

--------------------------------------------------

def IsPermitation(str1, str2):
	
	if len(str1) != len(str2):
		return False

	arr[0..255] = 0

	for char in str1:
		arr[char] += 1

	for char in str2:
		arr[char] -= 1

	for i in range(256):
		if arr[i] != 0:
			return False
	
	return True

-------------------------
def ReplaceSpacesWith20(str):
	
	length = len(str)
	right_char_found = False
	right_index = length - 1

	for i in range(length - 1, -1, -1):
		if str[i] != ' ' and right_char_found == False:
			right_char_found = True

		if str[i] == ' ' and right_char_found = True:
			str[right_index - 2: right_index] = '%20'
			right_index -= 3
		elif str[i] != ' ':
			str[right_index] = str[i]
			right_index -= 1
	
	return str
		
---------------------------
def StringCompression(st)

	length = len(st)
	prev = str[0]
	count = 1
	new_st = ''

	for char in st[1:length - 1]:
		if prev == char:
			count +=1
		else:
			new_str += prev + str(count)
			prev = char
			count = 1
	
	new_str += prev + str(count)							
	return new_str
	
--------------------------------

def Matrix(arr, m, n):
	
	columns = [0..n-1] = 0
	rows = [0..m-1] = 0

	for row in range(m):
		for col in range(n):
			if arr[row][col] == 0:
				columns[col] = 1
				rows[row] = 1

	for row in range(m):
		for col in range(n):
			if rows[row] == 1 or columns[col] == 1:
				arr[row][col] = 0


               ------------ set --------------
	columns = {}
	rows = {}

	for row in range(m):
		for col in range(n):
			if arr[row][col] == 0:
				columns = columns + col
				rows = rows + row

	for row in range(m):
		for col in range(n):
			if row in rows or col in columns:
				arr[row][col] = 0

	return arr

---------------------------------------------
2 arrays given. Find 2 elements, one from each arrays, such that swapping them makes the sums of arrays eqial 

def FindAndSwap(arr1, arr2):

	numbers = {}
	sum1 = 0
	sum2 = 0
		

	for num in arr1:
		sum1 += num
		numbers += num


	for num in arr2:
		sum2 += num
		
	for num in arr2:
		if num - (sum2 - sum1) / 2 in numbers:
			return num, num - (sum2 - sum1) / 2 

------------------------------------------

class Node:
	def __init__(self, data)
		self.data = data
		self.next = None

def MergreLists(list1, list2)

	if list1 == None:
		return list2
	if list2 == None:
		return list1

	if list1.data >= list2.data:
		list1.next = Merge(list1.next, list2)
		return list1
	else:
		list2.next = Merge(list2.next, list1)
		return list2

	------------------

	if list1.data >= list2.data:
		head = list1
		l1 = list1.next
		l2 = list2
	else:
		head = list2
		l1 = list2.next
		l2 = list1

	current = head


	while l1 != None and l2 != None:		
		if l1.data >= l2.data:
			current.next = l1
			l1 = l1.next
		else:
			current.next = l2
			l2 = l2.next
		current = current.next

------------

	current = None
	head = None

	while l1 != None and l2 != None:		
		if l1.data >= l2.data:
			if head == None:
				head = l1
			else:
				current.next = l1
			current = l1
			l1 = l1.next
		else:
			if head == None:
				head = l2
			else:
				current.next = l2
			current = l2
			l2 = l2.next

		


------------
	if l1 == None:
		current.next = l2
	elif l2 == None:
		current.next = l1
	
	return head
	







































	
























  