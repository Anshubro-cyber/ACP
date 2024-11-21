def reverse_bits(number):
    
    reversed_binary = bin(number)[:1:-1]
    return int(reversed_binary, 2)


number = int(input("Enter your original number: "))


reversed_number = reverse_bits(number)

print(reversed_number)