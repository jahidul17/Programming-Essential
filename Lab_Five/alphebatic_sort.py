string=input("Enter a string: ")
words=string.split()
words.sort()
#Here sort function first priority capital letter the small letter.
for word in words:
    print(word)