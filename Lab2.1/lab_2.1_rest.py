import sys
import requests
import json
import pprint

host_ip = '10.31.70.210'
login = sys.argv[1]
password = sys.argv[2]

host_url = 'https://' + host_ip + ':55443'

request = requests.post(host_url + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = request.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
request = requests.get(host_url + '/api/v1/interfaces', headers=header, verify=False)
pprint.pprint(request.json())
