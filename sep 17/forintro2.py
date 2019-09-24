print('enter your sweet name:')
str=input()     
count=0
vowels=['a','e','i','o','u']
 
for i in str:
	if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
		count=count+1
	

print('the number of vowels in ur name is:',count)
if(count==0):
	print('its amazing!! there are no vowels!')	