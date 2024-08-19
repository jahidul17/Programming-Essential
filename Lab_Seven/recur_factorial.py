def recur_fact(n):
    if n==1:
        return n #Base case must be need for recurson.
    else:
        return n*recur_fact(n-1)
    
num=int(input("Enter a number: "))

if num<0:
    print("Sorry! Factorial does not exit for negative numbers.")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is =",recur_fact(num))
