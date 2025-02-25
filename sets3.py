import itertools
s1=set()
names=['yash','nisha','krishna','gopal','radhe']
for i in names:
    s1.add(i)
print(s1)
for i in itertools.islice(s1,1):
    s1.remove(i)
    s1.add('Kanha')

print(s1)
for i in range(2):

    for j in itertools.islice(s1,1):
    
        s1.remove(j)
print(s1)