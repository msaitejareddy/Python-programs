outfile=open('dummy.txt','w')
outfile=open("dummy.txt", 'w');
outfile.write("Hello! This is testing")
outfile.write("Testing confirmed")


outfile.close()

infile=open('dummy.txt','r')
Reader=infile.readline()
print(Reader)
while (Reader):
	print(Reader)
      Reader=infile.readline()
print('banti')

