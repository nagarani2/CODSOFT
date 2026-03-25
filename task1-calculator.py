print('Simple calculator')
num1=float(input('Enter first number:'))
num2=float(input('Enter second number:'))
operator=input("enter the operator: ")
if operator=='+':
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    if num2!=0:
        result=num1/num2
    else:
        print('Cannot divide by zero ')    
else:
    result='invalid' 
print("Result=",result)               

