cupper=0
clower=0
l1=[]
l2=[]
def count_lower_upper(sample):
    
    for i in sample:
        if i==i.isupper():
            cupper=cupper+1
            l1.append(i)
        elif i==i.islower():
            clower=clower+1
            l2.append(i)
    
    dicti={"upper" : l1,"lower":l2}
    print(dicti)
def main():
    sample=input("Enter the string : ")
    count_lower_upper(sample)
    print(cupper)
    print(clower)
main()