outfile=open('wickets.txt','w')
print('enter bowler and wickets taken')
bowler=input()
wickets=int(input())
while(wickets!=-1 and bowler!=-1):
	outfile.write(bowler+'-'+str(wickets)+'\n')
	print('enter bowler and wickets taken')
	bowler=input()
	
	wickets=int(input())
outfile.close()

