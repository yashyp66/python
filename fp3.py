import random
l1=[random.randint(-15,15) for _ in range(10)]
l2=list(map(lambda x:x**2,l1))
print(l2)