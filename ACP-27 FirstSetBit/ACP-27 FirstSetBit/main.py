def find_rightmost_set_bit(n):
    
    if n == 0:
        return -1  
    position = (n & -n).bit_length()  
    return position

number = int(input("Enter a number: "))


position = find_rightmost_set_bit(number)

if position == -1:
    print("No set bits in the number")
else:
    print(f"Position of the rightmost set bit: {position}")
