import random
import string

def generate_password(length, uppercase, lowercase, digits, special):
    """
    This function generates a random password based on user-defined criteria.
    """
    # Define the character sets
    upper_chars = string.ascii_uppercase if uppercase else ''
    lower_chars = string.ascii_lowercase if lowercase else ''
    digit_chars = string.digits if digits else ''
    special_chars = string.punctuation if special else ''
    
    # Combine the character sets
    all_chars = upper_chars + lower_chars + digit_chars + special_chars
    
    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Prompt the user for input
length = int(input('Enter the desired password length: '))
uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
lowercase = input('Include lowercase letters? (y/n): ').lower() == 'y'
digits = input('Include digits? (y/n): ').lower() == 'y'
special = input('Include special characters? (y/n): ').lower() == 'y'

# Generate the passwords
num_passwords = 1  # You forgot to define this variable
for i in range(num_passwords):
    password = generate_password(length, uppercase, lowercase, digits, special)
    print(f'Password {i+1}: {password}')
