names=('vishwa','rosy','sony','chandu','ashwin kumar','santhu','vamshi')
min=0

for i in range(1,len(names)):
	if len(names[i])<len(names[min]):
		min=i

length=len(names[min])
print('smallest name is \n' + names[min])
print('length is\n' + str(length) )