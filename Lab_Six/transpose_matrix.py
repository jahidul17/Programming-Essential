matrix1=[[1,2],
         [3,4],
         [5,6]]

matrix2=[[0,0,0],
         [0,0,0]]

print(len(matrix1[0]))
print(len(matrix1))

print(len(matrix2[0]))
print(len(matrix2))


for row in range(len(matrix1)):
    for col in range(len(matrix1[0])):
        # print(row,col," ",end='')
        matrix2[col][row]=matrix1[row][col]
    # print()

for r in matrix2:
    print(r)