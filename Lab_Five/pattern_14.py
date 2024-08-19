n=5
k=1
count=1

for row in range(1,n+1):
    for col in range(0,k):
        print(count," ",end='')
        count+=1
    k+=2
    print()

# 1  
# 2  3  4
# 5  6  7  8  9
# 10  11  12  13  14  15  16
# 17  18  19  20  21  22  23  24  25
