------------------------------
Remove element from a heap

class Node
	left: Node
	right: Node
	value: Data

def RemoveHead(head):
	left = head.left
	right = head.right

	if left == Null and right == Null:
		return Null
	if left == Null:
		return right
	elif right == Null:
		return left
	
	if left.value >= right.value:
		head.value = left.value
		head.left = RemoveHead(left)
	else:
		tmp = RemoveHead(right)
		if tmp == Null:
			return left
		else
			tmp.left = head.left

	return tmp

															-------------------------------------


def MegreSort(arr)
	length = len(arr)
																if length == 2:
		if arr[0] < arr[1]:
			tmp = arr[0]
			arr[0] = arr[1]
			arr[1] = tmp
		return
	elif length == 1:
		return	
	elif length < 1:
		exception

	new_length = length/2 - 1

	MergeSort(arr[0:new_length])
	MergeSort(arr[new_length+1:length-1]																										i = new_length
	j = length-1														
	new_arr = [0:length-1]
	counter = length-1
	
	while counter >= 0:
	#	if i >= 0 and j >= 0:	
	#		if arr[i] > arr[j] : 
	#			new_arr[counter] = arr[i]
	#			i -= 1
	#		else: 	
	#			new_arr[counter] = arr[j]
	#			j -= 1
		if (i < 0) or (i >= 0 and arr[i] < arr[j]):
			new_arr[counter] = arr[j]
			j -= 1
		elif (j < lew_length+1) or (j >= lew_length+1 and arr[i] > arr[j]):
			new_arr[counter] = arr[i]
			i -= 1
		counter -= 1
													
	for i in range(length):
		arr[i] = new_arr[i]

















