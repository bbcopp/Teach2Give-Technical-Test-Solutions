# Question 2: Write a Python function that checks whether a word or phrase is palindrome or not.

def is_palindrome(phrase: str) -> bool:
    # Remove spaces and make the phrase lowercase
    clean_phrase = ''.join(phrase.lower().split())
    # Check if the phrase reads the same backward
    return clean_phrase == clean_phrase[::-1]

# Test examples
if __name__ == "__main__":
    print(is_palindrome("madam"))           
    print(is_palindrome("nurses run"))      
    print(is_palindrome("hello"))           
