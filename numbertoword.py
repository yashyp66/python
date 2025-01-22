def number_to_word(num):
    
    if num == 0:
        return "Zero"
    elif num == 1:
        return "One"
    elif num == 2:
        return "Two"
    elif num == 3:
        return "Three"
    elif num == 4:
        return "Four"
    elif num == 5:
        return "Five"
    elif num == 6:
        return "Six"
    elif num == 7:
        return "Seven"
    elif num == 8:
        return "Eight"
    elif num == 9:
        return "Nine"
    elif num == 10:
        return "Ten"
    elif num == 11:
        return "Eleven"
    elif num == 12:
        return "Twelve"
    elif num == 13:
        return "Thirteen"
    elif num == 14:
        return "Fourteen"
    elif num == 15:
        return "Fifteen"
    elif num == 16:
        return "Sixteen"
    elif num == 17:
        return "Seventeen"
    elif num == 18:
        return "Eighteen"
    elif num == 19:
        return "Nineteen"
    else:
        return "Out of range"
num=int(input("What's number?"))

number_to_word(num)
print(num,":",number_to_word(num))
