l1=[(),(1,'yash'),(),('nisha','ramesh'),(12.4,5),()]
print(l1)
print("the list without empty spaces after removing it is : ")
for i in l1:
    if len(i)==0:
        l1.remove(i)
print(l1)
