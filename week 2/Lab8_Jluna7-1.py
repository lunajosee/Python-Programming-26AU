"""
Python Programming 26AU W04L
Author: Jose Luna
Purpose:This program calculates the check digit for a UPC code and verifies if the provided UPC is valid.
Resources: Written from scratch. UPC-A algorithm reference: https://en.wikipedia.org/wiki/Universal_Product_Code
Date: September 20, 2026
"""

def find_UPC(digits):
    """Calculate and return the expected UPC check digit from first 11 digits."""
    odd_sum = 0
    even_sum = 0

    for i in range(len(digits)):
        digit = int(digits[i])
        if (i + 1) % 2 != 0:
            odd_sum = odd_sum + digit
        else:
            even_sum = even_sum + digit

    odd_sum = odd_sum * 3
    total = odd_sum + even_sum
    check_digit = (10 - (total % 10)) % 10
    return check_digit

upc = input("Enter a 12 digit UPC: ")

while len(upc) != 12 or not upc.isdigit():
    print("Invalid input. Please enter a 12 digit UPC.")
    upc = input("Enter a 12 digit UPC: ")

first_11_digits = upc[0:11]
provided_check_digit = int(upc[11])

expected_check_digit = find_UPC(first_11_digits)

print("The first 11 digits of the UPC are:", first_11_digits)
print("The provided check digit is:", provided_check_digit)
print("The expected check digit is:", expected_check_digit)

if int(provided_check_digit) == int(expected_check_digit):
    print("The UPC is valid.")
else:
    print("The UPC is invalid.")