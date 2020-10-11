import requests
import json

#url = "https://api.meraki.com/api/v0/networks/L_566327653141856846/devices"
#url = "https://dashboard.meraki.com/api/v0/networks/L_566327653141856846/devices"
baseurl = "https://dashboard.meraki.com/api/v0/networks/"
mynetwork = 'L_646829496481100388/'

url = baseurl + mynetwork + 'devices'

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
#print(response.json)
