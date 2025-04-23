class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def display(self):
        for row in self.data:
            print(row)
        print()

    def add(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def multiply(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                value = sum(self.data[i][k] * other.data[k][j] for k in range(3))
                row.append(value)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

# Example matrices
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Performing operations
print("Matrix A:")
A.display()

print("Matrix B:")
B.display()

print("A + B:")
A.add(B).display()

print("A * B:")
A.multiply(B).display()

print("Transpose of A:")
A.transpose().display()
