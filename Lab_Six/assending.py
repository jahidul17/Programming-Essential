data_list=[5,-2,15,20,23,-6,27,47]

new_list=[]
# while data_list:
#or
for i in range(len(data_list)):
    minimum=data_list[0]
    
    for x in data_list:
        if minimum>x:
            minimum=x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)

