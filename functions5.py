import string

def ispangram(input_string):
    # Create a set of all lowercase alphabets
    alphabet_set = set(string.ascii_lowercase)
    
    # Convert the input string to lowercase and create a set of characters
    input_set = set(input_string.lower())
    
    # Check if the alphabet set is a subset of the input set
    return alphabet_set <= input_set

# Test the function with examples
test_strings = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels",
    "Hello world"
]

for test_string in test_strings:
    result = ispangram(test_string)
    print(f"Is the string '{test_string}' a pangram? {result}")
