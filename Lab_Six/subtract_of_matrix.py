x=[[10,11,12],
   [13,14,15],
   [16,17,18]]

y=[[1,2,3],
   [4,5,6],
   [7,8,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]


for row in range(len(x)):
    for col in range(len(y)):
        result[row][col]=x[row][col]-y[row][col]

print("Subtract between two matrix: ")
for r in result:
    print(r)