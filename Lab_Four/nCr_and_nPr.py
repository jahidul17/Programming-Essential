import math

# create factorial function
def fact(x):
    fact=1
    while x>0:
        fact*=x
        x-=1
    return fact

# y=int(input())
# print(fact(y))


while True:
    print("Enter 'x' for exit.")
    nval=input("Enter value of n: ")
    rval=input("Enter value of r: ")

    if nval=='x':
        break
    else:
        n=int(nval)
        r=int(rval)
        npr=math.factorial(n)/math.factorial(n-r)
        ncr=math.factorial(n)/math.factorial(r)*math.factorial(n-r)
        # ncr=npr/math.factorial(r)

        print("nCr = ",ncr)
        print("nPr = ",npr)
        print("\n")

        