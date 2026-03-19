
n=int(input("Please enter the any number :"))

mini=float("inf")
while n>0:
    digit=n%10
    if digit < mini:
        mini=digit
    n=n//10
print(mini)
