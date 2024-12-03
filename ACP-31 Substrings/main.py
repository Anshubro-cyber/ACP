def find_substrings(s):
    """Function to find all substrings of a string"""
    substrings = []
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    return substrings

def main():
    
    input_array = input("Enter the list of strings (comma separated): ").split(",")
    
   
    input_array = [s.strip() for s in input_array]
    
  
    for string in input_array:
        print(f"Substrings of '{string}':")
        substrings = find_substrings(string)
        for substring in substrings:
            print(substring)

if __name__ == "__main__":
    main()