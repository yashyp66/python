while True:
    try:
        # Ask for user input
        user_input = int(input("Please enter an integer: "))
        # If input is valid, break the loop
        print(f"You entered the integer: {user_input}")
        
        # Reverse the number
        reversed_number = int(str(user_input)[::-1])
        print(f"The reversed number is: {reversed_number}")
        break
    except ValueError:
        # If input is not an integer, print an error and continue the loop
        print("Invalid input! Please enter a valid integer.")
