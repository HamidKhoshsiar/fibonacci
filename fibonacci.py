z = int(input('how many? '))
i,j,k,j2 = 2,0,1,1
print('1 = 0')
print('2 = 1')
while i <= z :
	j2 = k + j
	print(i, '=',j2)
	j = k
	k = j2
	i += 1

