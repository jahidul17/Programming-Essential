input_set=[]
input_num=0

while(input_num>=0):
    input_num=int(input("Enter a number or -1/negative value to finish: "))
    if(input_num<0):
        break
    input_set.append(input_num)
print(input_set)

largest=input_set[0]
# for i in range(0,len(input_set)): # or
for i in range(0,len(input_set)):
    if input_set[i]>largest:
        largest=input_set[i]
print("Largest number is: ",largest)

smallest=input_set[0]
# for i in range(0,len(input_set)): # or
for i in range(0,len(input_set)):
    if input_set[i]<smallest:
        smallest=input_set[i]
print("Smallest number is: ",smallest)
