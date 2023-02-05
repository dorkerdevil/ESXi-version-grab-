import requests
import sys 
#from @DD
class TrustAllCertsPolicy:
    def check_validation_result(self, srvPoint, certificate, request, certificate_problem):
        return True

cert_policy = TrustAllCertsPolicy()

target = sys.argv[1]
method = "POST"
endpoint = "/sdk/"
uri = target + endpoint

payload = '<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><Header><operationID>esxui-1ca5</operationID></Header><Body><RetrieveServiceContent xmlns="urn:vim25"><_this type="ServiceInstance">ServiceInstance</_this></RetrieveServiceContent></Body></Envelope>'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"

response = requests.post(uri, data=payload, headers={"User-Agent": user_agent}, verify=False)

print(response.content)
