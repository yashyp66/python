s1={'abhi','archi','bhavesh','bharti'}
print(s1)
A=set()
B=set()
for i in s1:
    if i.startswith('a'):
        A.add(i)
    elif i.startswith('b'):
        B.add(i)
print(A,B)
