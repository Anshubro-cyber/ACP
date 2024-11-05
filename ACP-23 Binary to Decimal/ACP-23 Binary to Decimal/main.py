# Function to convert binary to decimal
def binary_to_decimal(binary):
    # Convert the binary string to a decimal integer
    decimal = int(binary, 2)
    return decimal

# Main program
def main():
    # Ask the user to input a binary number
    binary = input("Enter your Binary: ")
    
    # Convert the binary number to decimal
    decimal = binary_to_decimal(binary)
    
    # Output the result
    print(f"Decimal: {decimal}")

# Call the main function
if __name__ == "__main__":
    main()

