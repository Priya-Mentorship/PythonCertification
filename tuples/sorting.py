c=dict({'z':155,'a':200,'c':11})
t=c.items()
# print(sorted(t,reverse=True))    
for a,b in sorted(c.items(),reverse=True):
    print(b,a)