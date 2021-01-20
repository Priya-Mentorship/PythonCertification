count =dict()
names =['a','b','c','a','b','c','a','b','c']
#print(names['a'])
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1    
print(count[name])
print(count.get('a',0))