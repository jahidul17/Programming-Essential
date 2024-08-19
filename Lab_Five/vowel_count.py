vowels='aeiou'
string=input("Enter a string: ")
string=string.casefold() #casefold function use for convert small case.

count={}.fromkeys(vowels,0)

for char in string:
    if char in count:
        count[char]+=1
print(count)
