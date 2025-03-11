def create_array(dim1, dim2, dim3, initial_value):
    # Create a 3D array using list comprehensions
    array = [[[initial_value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
    return array

# Example usage:
dim1, dim2, dim3 = 3, 4, 5
initial_value = 10
array = create_array(dim1, dim2, dim3, initial_value)

# Print the created 3D array
print("Created 3D Array:")
for layer in array:
    for row in layer:
        print(row)
