import hashlib

# Get user input
input_str = input("Enter the value to encode: ")

# Encode the input string and compute SHA-1 hash
result = hashlib.sha1(input_str.encode()).hexdigest()

# Print the hexadecimal equivalent of SHA-1
print(f"The hexadecimal equivalent of SHA-1 is: {result}")
