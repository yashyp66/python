def prime_factor(n,divisor =2):
    if n<divisor:
        return []
    if n%divisor ==0:
        return[divisor]+prime_factor(n//divisor,divisor)
    else:
        return prime_factor(n,divisor+1)
n=int(input("Enter the number:"))
print("prime factors of",n,"are ",prime_factor(n))