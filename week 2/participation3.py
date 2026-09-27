

class UPCValidator:
    """A class that validates a 12-digit UPC-A code by checking its check digit.
    Date: 9/26/26"""

    def __init__(self, upc):
        """Store the raw UPC string entered by the user."""
        self.upc = upc

    def is_valid_format(self):
        """Returns True if the UPC is properly formatted, or a reason why not."""
        if len(self.upc) != 12:
            return "Must be exactly 12 digits"
        if not self.upc.isdigit():
            return "Must contain only digits"
        return True

    def find_UPC(self):
        """Calculate and return the expected UPC check digit from the first 11 digits."""
        first_11_digits = self.upc[0:11]
        odd_sum = 0
        even_sum = 0

        for i in range(len(first_11_digits)):
            digit = int(first_11_digits[i])
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
        provided_check_digit = int(self.upc[11])
        expected_check_digit = self.find_UPC()

        print("The first 11 digits of the UPC are:", self.upc[0:11])
        print("The provided check digit is:", provided_check_digit)
        print("The expected check digit is:", expected_check_digit)

        if provided_check_digit == expected_check_digit:
            print("The UPC is valid.")
        else:
            print("The UPC is invalid.")


upc_input = input("Enter a 12 digit UPC: ")
validator = UPCValidator(upc_input)
format_check = validator.is_valid_format()

while format_check != True:
    upc_input = input(f"{format_check}! Please enter a 12 digit UPC: ")
    validator = UPCValidator(upc_input)
    format_check = validator.is_valid_format()

validator.is_valid()