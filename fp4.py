from functools import reduce
lst=['madam','python','malayalam',12321]
def is_palindrome(x):
    x_str=str(x)
    return x_str==x_str[::-1]
l2=list(filter(is_palindrome,lst))
print(l2)