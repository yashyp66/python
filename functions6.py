def generate_tuples(ending_value):
    # Create a list of tuples (x, x^2, x^3) for all x between 1 and ending_value
    result = [(x, x**2, x**3) for x in range(1, ending_value + 1)]
    return result

# Example usage:
ending_value = 5
result = generate_tuples(ending_value)

# Print the result
print(result)
