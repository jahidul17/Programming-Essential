sum=0
number=int(input("Please enter the value number: "))
while number>0:
    temp=number%10
    sum=sum+int(temp)
    number=number/10
print("Summation of the digits is = ",sum)
