for hour in range(24):
    if hour ==0:
        print("12 AM(midnight)")
    elif hour == 12:
        print("12 PM (noon)")
    elif hour<12:
        print(f"{hour} AM")
    else:
        print(f"{hour-12} PM ")