#enter a number for its multiples(table)

#2*1=22*2=43*1=3



print('enter a number')
number=int(input())
for i in range(1,11):
	
	res=number*i
	
	print(str(number) + '*' + str(i) + str('=') + str(res))
	


	