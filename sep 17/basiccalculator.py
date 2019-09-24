res=0
print('enter 2 numbers to perform operation')
op1=int(input())
op2=int(input())
print('choose an operator from +/-/*/ / /')
operator=input()

if operator=='+':
	print('result is: \n' , op1+op2)
elif operator=='-':
	print('result is: \n' , op1-op2)
elif operator=='*':
	print('result is: \n' , op1*op2)
elif operator=='/':
	print('result is: \n' , op1/op2)
else:
	print('check your input')







