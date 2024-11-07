import math

# Function to calculate LCM
def calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Input from the user
num1 = int(input("Enter Largest number: "))
num2 = int(input("Enter Smallest number: "))

# Calculate LCM
lcm = calculate_lcm(num1, num2)

# Display the result
print("LCM is:", lcm)
