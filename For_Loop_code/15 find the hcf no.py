num1=int(input("Please enter the number :"))
num2=int(input("Please enter the number :"))

for i in range(1,num2+1):
    if (num2 !=0):
        num1,num2=num2,num1%num2
print(num1)