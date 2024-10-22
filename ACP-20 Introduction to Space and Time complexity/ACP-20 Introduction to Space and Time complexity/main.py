def multiply_one_iteration(a, b):
    """Multiplies a and b using direct multiplication."""
    return a * b

def multiply_n_iterations(a, b):
    """Multiplies a and b using repeated addition (N iterations)."""
    result = 0
    for _ in range(a):
        result += b
    return result

# Input values
a = int(input("Enter 'a' for a*b: "))
b = int(input("Enter 'b' for a*b: "))

# Calculate results
result_one_iteration = multiply_one_iteration(a, b)
print(f"1 iteration: {result_one_iteration}")

result_n_iterations = multiply_n_iterations(a, b)
print(f"N iteration: {result_n_iterations}")