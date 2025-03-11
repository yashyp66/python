def ispalindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
test_strings = [
    "A man a plan a canal Panama",  # A famous palindrome
    "Racecar",                      # Another palindrome
    "Hello World"                  # Not a palindrome
]

for test_string in test_strings:
    result = ispalindrome(test_string)
    print(f"Is the string '{test_string}' a palindrome? {result}")
