def check_password_complexity(password):
    # Define criteria for password complexity
    criteria = {
        'length': 8,
        'uppercase': False,
        'lowercase': False,
        'digits': False,
        'special_chars': False
    }
    
    # Check password length
    if len(password) < criteria['length']:
        return False, "Password must be at least {} characters long.".format(criteria['length'])
    
    # Check for uppercase characters
    criteria['uppercase'] = any(char.isupper() for char in password)
    
    # Check for lowercase characters
    criteria['lowercase'] = any(char.islower() for char in password)
    
    # Check for digits
    criteria['digits'] = any(char.isdigit() for char in password)
    
    # Check for special characters
    special_chars = "!@#$%^&*()-_+=~`[]{}|;:,.<>?/"
    criteria['special_chars'] = any(char in special_chars for char in password)
    
    # Check if all criteria are met
    if all(criteria.values()):
        return True, "Password meets complexity requirements."
    else:
        return False, "Password does not meet complexity requirements."


# Test the function
password = input("Enter password to check complexity: ")
is_complex, message = check_password_complexity(password)
print(message)
