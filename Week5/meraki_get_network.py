import requests

url = "https://api.meraki.com/api/v0/organizations/681155/networks"

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
