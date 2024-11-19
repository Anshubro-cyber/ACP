def find_rightmost_set_bit(n):
    # The rightmost set bit is found using n & -n
    # This isolates the rightmost set bit
    if n == 0:
        return -1  # No set bits in 0
    position = (n & -n).bit_length()  # bit_length() gives the position of the rightmost set bit
    return position

# Input from the user
number = int(input("Enter a number: "))

# Find the position of the rightmost set bit
position = find_rightmost_set_bit(number)

if position == -1:
    print("No set bits in the number")
else:
    print(f"Position of the rightmost set bit: {position}")
