x=[[12,7,3],
   [4,5,6],
   [7,8,9]]

y=[[5,8,1],
   [6,7,3],
   [4,5,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

# print((len(x)))
# print((len(y)))
for row in range(len(x)):
    for col in range(len(y)):
        # print(x[row][col]," ",y[row][col],end='')
        # print(x[row][col]+y[row][col]," ",end='')
        result[row][col]=x[row][col]+y[row][col]
        
    # print()

print("Summation between two matrix: ")
for r in result:
    print(r)
