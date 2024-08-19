
year=int(input("Please enter the value of year: "))
if(((year%4==0) and (year%100!=0) or (year%400==0))):
    print("This year {} is leap year.".format(year))
else:
    print(year,"year is not leap year")


