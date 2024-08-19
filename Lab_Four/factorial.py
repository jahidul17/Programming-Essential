num=int(input("Enter a number: "))
fact=1
temp=num
if num<0:
    print("Sorry! Factorial does not exist for negative numbers.")
elif num==0:
    print("The factorial of 0 is = 1")

else:
    # while(num>0):
    #     fact*=num
    #     num-=1
    # print("The factorial of {0} is {1}".format(temp,fact))

    # another way
    
    for i in range (1,num+1):
        fact=fact*i
    print("The factorial of {0} is {1}".format(num,fact))