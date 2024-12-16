import requests,sys

def execute_command(cmd):
	payload = f"""<?xml version="1.0" encoding="UTF-8">
		<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://tempuri.org/" >
			<soap:Body>
				<tns:ExecuteCommandRequest>
					<cmd>{cmd}</cmd>
				</tns:ExecuteCommandRequest>
			</soap:Body>
		</soap:Envelope>
		"""

	headers = {
		"Content-Type":"text/xml; charset=utf-8",
		"SOAPAction": "ExecuteCommand",
	}

	# Sending the Request
	try:
		response = requests.post(url, data=payload, headers=headers)

		# Display the response
		if response.status_code == 200:
			print("Response:")
			print(response.text)
		else:
			print(f"Error: Received HTTP {response.status_code}")
	except Exception as e:
		print(f"An error occured : {e}")

# Example usage 
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Error : URL argument is missing")
		sys.exit(1)
	
	url = sys.argv[1]
	command = input("Please Enter your Command : $ ")
	execute_command(command)
