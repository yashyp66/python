capital=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
small=("abcdefghijklmnopqrstuvwxyz")

string=input("enter the small string : ")
for i in range(len(string)):
    for j in range(len(capital)):
        if string[i]==capital[j]:
            print(small[j],end="")
        elif string[i]==small[j]:
            print(capital[j],end="")
   


