# Question 5: Write a program that accepts a string as input, capitalizes the first letter of each word in the string.

def capitalize_words(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split())

# Test examples
if __name__ == "__main__":
    print(capitalize_words("hi"))                     
    print(capitalize_words("i love programming"))     