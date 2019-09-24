#by using for loop ,number is taken as user input and factorial is returned.
# 5!=1*2*3*4*5

print('enter a number to find factorial!')
number=int(input())
product=1

for n in range (1,number+1):
	product=product*n

print('factorial of ' + str(number)+ ' is :' + str(product))