def longest_consecutive_ones(n):
    count = 0  
    max_count = 0 
    while n > 0:
       
        count += 1
        n = n & (n << 1)  
        
        max_count = max(max_count, count)
        
    return max_count


num = int(input("Enter your number: "))


result = longest_consecutive_ones(num)
print(f"Longest consecutive 1's length: {result}")
