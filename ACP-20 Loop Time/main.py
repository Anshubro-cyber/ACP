def myfunction(n):
    # First Loop: Runs from 0 to n, so O(n)
    for i in range(0, n + 1):
        print("First Loop")
    
    # Second Loop: Doubles j each time, so O(log n)
    j = 1
    while(j <= n + 1):
        print("Second Loop", j)
        j = j * 2
    
    # Third Loop: Always runs 100 times, so O(1)
    for i in range(0, 100):
        print("Third Loop")

# Example usage
myfunction(5)

# Total Time Complexity: 
# O(n) + O(log n) + O(1) = O(n)
