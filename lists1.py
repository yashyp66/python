import random 
l1=[]
for i in range(5):
    l1.append(random.randrange(1,100,2))
print(l1)

l2=[]
for i in range(4):
    l2.append(random.randrange(1,100)*2)
print(l2)
l1[2]=l2
print(l1)