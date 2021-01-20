c =dict()
names =['a','b','c']
for name in names:
    if name not in c:
        c[name]=1
    else:
        c[name]=c[name]+1    
print(c[name])
print(c.get('a',0))