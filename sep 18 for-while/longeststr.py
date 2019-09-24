names=('vishwa','rosy','sony','chandu','ashwin kumar','santhu','vamshi')
max=0

for i in range(1,len(names)):
	if len(names[i])>len(names[max]):
		max=i

length=len(names[max])
print('longest name is \n' + names[max])
print('length is\n' + str(length) )