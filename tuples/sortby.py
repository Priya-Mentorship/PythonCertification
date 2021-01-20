c=dict({'hey':155,'this':200,'also':11})
temp= list()
for k,v in c.items():
    temp.append((v,k))
print(temp)    
print(sorted(temp))  
print(sorted(temp,reverse=True)) 

#print( sorted( [ (v,k) for k,v in c.items() ], reverse=True ) )

