import re

# Define the regex pattern for a valid credit card
pattern = r'^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$'

# Read the number of credit cards
n = int(input())

# Check each credit card number
for _ in range(n):
    card_number = input().strip()
    if re.match(pattern, card_number):
        print("Valid")
    else:
        print("Invalid")
