outfile=open('goodwords.txt','w')
outfile.write('never give up\n')
outfile.write('try and try until i win\n')
s='energy and persistence can conquer any thing in the world!!!'
outfile.write(s)
outfile.close()

for line in open('goodwords.txt'):
	print(line,end='')
