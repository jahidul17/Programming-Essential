
def smallest(a,b,c):
    if(a<=b and a<=c):
        return a
    elif(b<=a and b<=c):
        return b
    else:
        return c

while True:
    print("-------Are you execute operation?------")
    choice=input("Enter 'y' or 'n' : ")
    choice=choice.casefold()

    if choice=='y':
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        num3=int(input("Enter third number: "))
        print("The smallest number among",num1,',',num2,'and',num3,"is =",smallest(num1,num2,num3))
    else:
        break


