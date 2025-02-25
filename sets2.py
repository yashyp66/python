import random
l1=[]
for i in range(10):
    l1.append(random.randint(15,45))
print(set(l1))
count=0
for i in l1:
    if i<30:
        count+=1
print(count)
for i in l1:
    if i>35:
        l1.remove(i)

s1=set(l1)
print(s1)