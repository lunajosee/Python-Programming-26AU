"""
Rewrite UPC validator as a class for the class participation activity 3
9/26/26
"""

class UPCValidator:
    """A class that validates a 12-digit UPC-A code by checking its digit."""

    def __init__(self, upc):
        """Store the full UPC string and split it into its two parts."""
        self.upc = upc
        self.first_11_digits = upc[0:11]
        self.provided_check_digit = int(upc[11])

    def find_UPC(self):
        """Calculate and return the expected UPC check digit from the first 11 digits."""
        odd_sum = 0
        even_sum = 0

        for i in range(len(self.first_11_digits)):
            digit = int(self.first_11_digits[i])
            if (i + 1) % 2 != 0:
                odd_sum = odd_sum + digit
            else:
                even_sum = even_sum + digit

        odd_sum = odd_sum * 3
        total = odd_sum + even_sum
        check_digit = (10 - (total % 10)) % 10
        return check_digit

    def is_valid(self):
        """Compare the provided check digit to the expected one and report the result."""
        expected_check_digit = self.find_UPC()

        print("The first 11 digits of the UPC are:", self.first_11_digits)
        print("The provided check digit is:", self.provided_check_digit)
        print("The expected check digit is:", expected_check_digit)

        if self.provided_check_digit == expected_check_digit:
            print("The UPC is valid.")
        else:
            print("The UPC is invalid.")


upc = input("Enter a 12 digit UPC: ")

while len(upc) != 12 or not upc.isdigit():
    print("Invalid input. Please enter a 12 digit UPC.")
    upc = input("Enter a 12 digit UPC: ")

validator = UPCValidator(upc)
validator.is_valid()