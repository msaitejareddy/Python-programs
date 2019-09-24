#writing a program to display the strings with its length
#saiteja 7
#anu 3
print("Enter a name");
userInput=input();
while(userInput!='q'):
 if(len(userInput)<=5):
     print("Your name is not eligible for competition");
     break;
 print(userInput + ": " +str(len(userInput)));
 print("-----------");
 print("Enter another name");
 userInput=input();
 print(">>>>>>>>>>>>>>>>end");

   
