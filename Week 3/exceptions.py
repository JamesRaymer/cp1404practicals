"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- The ValueError will occur when an invalid number is entered as the
numerator or denominator.

2. When will a ZeroDivisionError occur?
- The ZeroDivisionError will occur when 0 is entered as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
-
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero.")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
