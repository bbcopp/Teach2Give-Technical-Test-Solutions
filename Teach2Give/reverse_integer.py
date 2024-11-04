# Question 4: Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_integer(n: int) -> int:
    # Converting the integer to a string, reverse it, and handle the sign
    reversed_str = str(abs(n))[::-1]
    # Converting back to integer and apply the original sign
    reversed_int = int(reversed_str) * (-1 if n < 0 else 1)
    return reversed_int

# Test examples
if __name__ == "__main__":
    print(reverse_integer(500))  
    print(reverse_integer(-56))   
    print(reverse_integer(-90))   
    print(reverse_integer(91))   