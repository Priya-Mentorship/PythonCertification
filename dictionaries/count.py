count = dict()
print("Enter a line of text")
line= input('')
words=line.split( )
for word in words:
    count[word] = count.get(word,0) +1
print(count)