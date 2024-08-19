lower=int(input("Enter lower range: "))
upper=int(input("Enter upper rnage: "))

print("Prime numbers between ",lower," and ",upper," are:")

prime_count=0
for num in range(lower,upper):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num,"is prime number.")
            prime_count=prime_count+1
    elif (num==1 or num==0):
        print(num," is not prime number.")
    else:
        print(num," is negative number.")

print("Total prime number between",lower,"to",upper,"is = ",prime_count)

