-------------------------------------------------------
A child can run upstairs with 1, 2, or 3 stairs at a time. Count a number of possible steps on n stairs

def CountStairs(n)
	if n <= 0:
		exception
	arr = []

	arr.append(1)
	arr.append(2)
	arr.append(4)
	
	for i in range(3, n):

		num = 0	
		for j in range(3):
			num += arr[i-j-1]
		arr.append(num)

	return arr[n-1]


----------------------------------------------------------
Find the way on the chess board from upper-left to the lower-right corner if there are obsticals

class Context:
	path = ''
	obs : arr
	n : int

def main:
	obs = [][]
	n
	path = ''
	context = new Context
	context.obs = obs
	context.n = n
	RobotMove(0, 0, context)


def RobotMove(x, y, cont):
	res = False
	if x == cont.n-1 and y == cont.n-1
		return True

	if x+1 < n and cont.obs[x+1, y] == False:
		res = RobotMove(x+1, y, cont)
		if res == False:
			cont.obs[x+1, y] = True
		else: cont.path = 'right ' + cont.path
	if y+1 < n and res == False and cont.obs[x, y+1] == False:
		res = RobotMove(x, y+1, cont)
		if res == False:
			cont.obs[x, y+1] = True
		else: cont.path = 'down ' + cont.path
	return res	

---------------------------------------------------------
Find the element in sorted array which index is equal to its value

def FindIndexValue(arr)
	
	if len(arr) == 0:
		exception
 
	begin = 0
	end  = len(arr) - 1
	while True:
		middle = begin + (end-begin)/2
		if arr[middle] < middle: # right 
			begin = middle + 1
		elif arr[middle] > middle:
			end = middle - 1
		else return middle
	
		if begin >= end:
			return -1
 
--------------------------------------------------------



























