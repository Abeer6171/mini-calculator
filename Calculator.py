print("This is a mini calculator")
print("1-Add")
print("2-Substract")
print("3-Multiply")
print("4-Divide")
print("5-Remainder,Modulus")
print("6-Exponential operator")
option=int(input("Choose an operation:"))
if(option in[1,2,3,4,5,6]):
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number"))
if(option==1):
    result=num1+num2
elif(option==2):
    result=num1-num2
elif(option==3):
    result=num1*num2
elif(option==4):
    result=num1/num2
elif(option==5):
    result=num1%num2
elif(option==6):
    result=num1**num2    
print(f"The result of operation is:{result}")  
print("Thanks for seeing my project")
input("Make sure to give your feedback on my project:")