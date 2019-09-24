print('enter no of hrs worked')
hrs=int(input())
pay=10
if(hrs<40):
   print('gross pay:'+ str(hrs*pay))

if(hrs>40):
   print('extra hrs:'+ str(hrs-40)+'extra pay earned:' str((hrs-40)*2))

  print('gross pay:'+ str(hrs*pay*1.5))
