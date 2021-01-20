c=dict({'z':155,'a':200,'c':11})
t=c.items()
print(sorted(t))    
for a,b in sorted(c.items(),reverse=True):
    print(a,b)