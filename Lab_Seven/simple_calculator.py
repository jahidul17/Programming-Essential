
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:
    print("Select operation within 1 to 5")
    print("1> Addition")
    print("2> Subtraction")
    print("3> Multiplication")
    print("4> Division")

    choice=int(input("Enter choice:"))

    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))

    if choice==1:
        print(num1,"+",num2,"=",add(num1,num2),"\n")
    elif choice==2:
        print(num1,"-",num2,"=",subtract(num1,num2),"\n")
    elif choice==3:
        print(num1,"*",num2,"=",multiplication(num1,num2),"\n")
    elif choice==4:
        print(num1,"/",num2,"=",divide(num1,num2),"\n")
    else:
        print("Invalid Input!")

