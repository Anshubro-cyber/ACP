def circuit_output(a, b, c):

    d = a & b
    e = b | c
    f = b & c
    g = e & f
    q = d & g

    return q

# Example usage:
a = 6
b = 9
c = 4

output = circuit_output(a, b, c)
print("Output:", output)  # Output: 1