def recur_sum(n):
    print(n,end=' ')
    if n==1 or n==0:
        print()
        return n
    else:        
        return n+recur_sum(n-1)

num=int(input("Enter a number: "))
if(num<0):
    print("Enter a positive number.")
else:
    print("The sum is =",recur_sum(num))   
