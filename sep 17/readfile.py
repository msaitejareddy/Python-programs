#how to read wickets data without loop from wickets.txt file
#infile=open('wickets.txt','r')
#wickets=infile.readline()
#print(wickets)
#wickets=infile.readline()
#print(wickets)
#wickets=infile.readline()
#print(wickets)

#how to read no of wickets taken by each bowler using while loop from wickets.txt file
infile=open('wickets.txt','r')
wickets=infile.readline()
while(wickets):
	print(wickets)
	wickets=infile.readline()


