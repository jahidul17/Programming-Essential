terms=int(input("How many terms: "))


n1=0
n2=1
# count=0
count=2
if terms<=0:
    print("Please enter a positive number.")
elif terms==1:
    print(n1)
else:
    print("Fibonacci sequence upto",terms,": ")
    print(n1,',',n2,end=' , ')
    
    while count<terms:        
        n3=n2+n1
        print(n3,end=' , ')
        n1=n2
        n2=n3        
        count+=1

        # another way

        # print(n1,end=' , ')
        # n3=n1+n2
        # n1=n2
        # n2=n3
        # count+=1
  

