# Maurice Davis
# lab 10 check prtection.
# 4-28-2025
'''This program securely formats and validates check amounts to prevent fraud.
#   It prompts the user to enter a dollar amount for a paycheck and ensures that
#   the input is within a specified valid range. If the input is valid, it
#   formats the amount with commas and two decimal places, then applies a 
#   check-protection mechanism by padding the amount with leading asterisks (*) 
#   in a fixed-width field of 10 characters.
'''

def main():
    print(" You Have Entered The Check Protection System")
    SENTINEL = -1  # User can enter -1 to quit
    MIN_PAY = 0.01
    MAX_PAY = 999999.99  

    while True:
        check_amount = getValidNum("Enter check payable amount (or -1 to quit):\n ", MIN_PAY, MAX_PAY,  SENTINEL)
        if check_amount == SENTINEL:
            print("Exiting program.")
            break

        # Format and protect the amount
        formatted_amount = f"{check_amount:,.2f}"  # adds commas and keeps 2 decimal places
        protected_amount = f"{formatted_amount:*>10}"  # inserts asterisks to fill 10 characters
        print(f'Payment Amount:${protected_amount}')

# Function to get a float from user input
def get_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Function to check if a value is invalid based on range and sentinel
def isInvalid(value, l, h, sent):
    '''returns True if value is invalid (bad data)
    returns False if value is valid (good data)
    '''
    if value == sent:
        return False  # Sentinel is always valid
    if value < l or value > h:
        return True
    return False

# Function to get a valid number within range or accept sentinel
def getValidNum(msg, low, high, sentinel):
    value = get_float(msg)
    #validate the user's input using isInvalid() to check conditions
    while isInvalid(value, low, high, sentinel):
        print(f'Invalid number! Please enter a value between ${low} and ${high}, or, {sentinel}, to quit.')
        value = get_float(msg)
    return value


# Run the main function
main()