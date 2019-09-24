n=4
outfile=open('rating.txt','w')
for i in range(1,n+1):
	print('enter name of restaurant\n',end='')
	rest=input()
	outfile.write(rest + '\n')
	print('rating out 0f 10\n',end='')
	rating=int(input())
	outfile.write(str(rating) + '\n')
outfile.close

	


 