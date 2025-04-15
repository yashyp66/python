def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer ")
        
def main():
    x=get_int("what's x ?")
    print(f"x is {x}")
main()