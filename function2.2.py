def decimal_2_binary(n):
    if n==0:
        return "0"
    binary= ""
    while n>0:
        binary=str(n%2) + binary
        n=n//2
    return binary
def main():
    n=int(input("Enter the number you want to convert it to binary : "))
    binary = decimal_2_binary(n)
    print(binary)
main()