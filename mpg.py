import random
import string

def generate_password(length):
    # Define possible characters in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

# User input for the length of the password
length = int(input("Enter the length of the password: "))

# Generate the password
generated_password = generate_password(length)

# Display the generated password
print("Generated password:", generated_password)
