outfile=open('greeting.txt','w')
outfile.write('many many happy returns of the day!!!\n')
outfile.write('Happy birthday python developer')
outfile.close()

infile=open('greeting.txt','r')
msg=infile.readline()
while(msg):
	print(msg)
	msg=infile.readline()
print('Have a wonderful day!!')
infile.close()

