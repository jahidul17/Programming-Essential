num=int(input("Enter a number: "))
sum=0
temp=num

while temp>0:
    digit=temp%10
    # sum=sum+int(digit)*int(digit)*int(digit)
    #or
    sum+=int(digit)**3
    temp=temp/10

if num==sum:
    print(num, "is Armstrong number.")
else:
    print(num,"is not Armstrong.")