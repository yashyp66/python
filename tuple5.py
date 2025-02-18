l1=[( ),(2,3.4,6),("yash",1,11),( )]

print(l1)
for i in l1:
    print(len(i))
    if len(i)==0:
        l1.remove(i)
    

print(l1)
