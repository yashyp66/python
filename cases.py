string=input("Enter the string: ")
def small(name):
    for i in string:
        print(chr(ord(i)-32),end="")
small(string)