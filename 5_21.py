XML file: transfer data to 2 dementional grid

str = raw_input()
begin = str.find('<tr>')
end = str.find('</tr>')

while begin != -1:
	substr = str[begin + 4:end]
	str = str[end + 6:len(str)]
	val_begin = substr.find('<val>')
	val_end = substr.find('</val>')
	list_value = []
	while val_begin != -1:
		val = substr[val_begin + 5:val_end]
		list_value.append(val)
		subval = substr[end + 7: len(substr)]
		val_begin = subval.find('<val>')
		val_end = subval.find('</val>')

	arr.append(list_val)
	begin = str.find('<tr>')
	end = str.find('</tr>')
print arr

---------------------------------
Calculator: Calculate a string with numbers and operators

str = raw_input()
arr1 = ()
operation = {'+', '-', '*', '/'}
num = ''
for i in range(len(n)):
	if str[i] in operations:
		if isnumeric(num) == True:
			arr1.append(float(num))
			arr1.append(str[i])
			num = ''
		else:
			exception 'Not a number'
	else
		num += str[i]
if num != '':
	arr1.append(num)

arr2 = ()
res = 0
flag = True
for i in range(len(arr1)):
    if flag == True
	if arr1[i] in {'*', '/'}:
		if arr[i] = '*':
			res = res * arr[i+1]	
		else:
			res = res / arr[i+1]
		flag = False
	elif arr1[i] in {'+', '-'):
		flag = True
		arr2.append(res)	
		arr2.append(arr1[i])
		res = 0
	else:
		Flag = Ture
		res = arr[i]
    flag = True
if res == 0:
	res = arr1[len-1]	
arr2.append(res)	

res = arr2[0]
for i in range(1, len(arr2), 2):
	if arr1[i] in {'+', '-'}:
		if arr[i] = '+':
			res = res + arr[i+1]	
		else:
			res = res - arr[i+1]
print res	





	val_begin = substr.find('<val>')
	val_end = substr.find('</val>')
	list_value = []
	
#	val_begin = 0
	while True:   # CHECK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		val_begin = substr.find('<val>')
		val_end = substr.find('</val>')
		if val_begin == -1:
			break 
		val = substr[val_begin + 5:val_end]
		list_value.append(val)
		subval = substr[end + 7: len(substr)]

------------------------------------
Through coin to get 1000 times one of k equal possibilities.

(n, k)

counter = 0
coins = 0

while True:
	res = 0
	for i in range(k):
		coins += 1
		res += 2 ** i * (rand % 2)
		if res > n:
			break
	if res <= n:
		counter += 1
	if counter >= 1000
		break
print coins


---------------------------------------
Rotate an image of n*n size 90 degree to the right

arr

for i in range (n/2 - 1):
	for j in range(i, n - i)
		tmp = arr(i, j)
		arr(i, j) = arr(n-1 - j, i)
		arr(n-1 - j, i) = arr(n-1 - i, n-1 - j)
		arr(n-1 - i, n-1 - j) = arr(j, n-1 - i)
		arr(j, n-1 - i) = tmp




Coordinates

		arr(i, j)
		arr(j, n-1 - i)
		arr(n-1 - i, n-1 - j)
		arr(n-1 - j, i) 

