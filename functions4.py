def sum_avg(marks):
    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)  # len(marks) will always be 5
    return total, average

# Example usage:
marks = [85, 90, 78, 92, 88]  # Marks of five subjects
total, average = sum_avg(marks)

# Print the results
print(f"Total: {total}")
print(f"Average: {average:.2f}")
