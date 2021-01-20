c=dict({'hey':155,'this':200,'also':11})
print(c.keys())
print('hey' in c)
print(c.values())
print(c.items())
for a,b in c.items():
    print(a,b)

c['hey']=c["hey"]+20
print(c)    