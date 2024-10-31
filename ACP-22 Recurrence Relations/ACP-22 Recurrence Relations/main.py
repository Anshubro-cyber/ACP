def myfunction2(n):
    # Example implementation of myfunction2
    if n > 0:
        print("In myfunction2:", n)

def myfunction1(n):
    if n > 0:  # Base case for positive n
        return
    for i in range(0, n + 1):
        print("Akshat")
    myfunction1(n // 2)  # Recursive call with integer division
    myfunction2(n // 3)   # Call to myfunction2 with integer division

def myfunction(n):
    if n <= 1:  # Base case
        return
    print("Akshat")  # Print "Akshat"
    myfunction(n - 1)  # Recursive call with n-1

# Example usage
myfunction1(-5)  # Example to test myfunction1
myfunction(5)     # Example to test myfunction


