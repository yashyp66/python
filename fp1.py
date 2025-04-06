def fun():
    print("this is fun function : ")
def disp():
    print("this is disp function  : ")
def msg():
    print("this is msg function : ")
def main():
    functions_lst=[fun,disp,msg]
    for func in functions_lst:
        func()
main()