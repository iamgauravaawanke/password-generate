import random
import string

def generate_password(length, num_uppercase, num_lowercase, num_digits, num_special):
    if length < num_uppercase + num_lowercase + num_digits + num_special:
        raise ValueError("Length is too short for the specified character counts")

    uppercase = ''.join(random.choice(string.ascii_uppercase) for _ in range(num_uppercase))
    lowercase = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_lowercase))
    digits = ''.join(random.choice(string.digits) for _ in range(num_digits))
    special = ''.join(random.choice(string.punctuation) for _ in range(num_special))

    password = uppercase + lowercase + digits + special
    password = ''.join(random.sample(password, len(password)))  # Shuffle the characters
    remaining_length = length - len(password)
    password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    password = ''.join(random.sample(password, len(password)))  # Shuffle the entire password

    return password

# Set the desired lengths of different character types
length = 16
uppercase_count = 2
lowercase_count = 4
digit_count = 4
special_char_count = 2

# Generate the password
generated_password = generate_password(length, uppercase_count, lowercase_count, digit_count, special_char_count)
print("Generated Password:"," gau" )