name=['Mahbub','Mahi','Mahdi','Samsul','Mahfuz','Tahsin','Zahidul islam']

with open('abc.txt',"w") as myfile:
    for c in name:
        myfile.write("%s\n"%c)
# content=open('abc.txt')
# print(content.read())

        
