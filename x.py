while True:
    try:
        
        user_input = int(input("Please enter an integer: "))
       
        print(f"You entered the integer: {user_input}")
        
        reversed_number = int(str(user_input)[::-1])
        print(f"The reversed number is: {reversed_number}")
        break
    except ValueError:
      
        print("Invalid input! Please enter a valid integer.")
