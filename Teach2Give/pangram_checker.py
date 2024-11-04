# Question 3: Write a Python function to check whether a string is a pangram or not.

def is_pangram(s: str) -> bool:
    # Create a set of all letters in the alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Convert the string to lowercase and create a set of characters
    return alphabet <= set(s.lower())

# Test examples
if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  
    print(is_pangram("Hello World"))                                  
