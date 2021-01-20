
handle = open("/Users/vishnupriya/Desktop/GitProjects/PythonCertification/dictionaries/text.txt")
counts = dict()
for line in handle:
    words = line.split()
    # print(words)
    for word in words:
        counts[word] = counts.get(word,0)+1
        # print(word)
lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)  
lst = sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)
