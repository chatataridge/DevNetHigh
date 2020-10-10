import requests

url = "https://api.meraki.com/api/v0/organizations"

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': ''
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
