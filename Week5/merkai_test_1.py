import requests

api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

url = "https://api.meraki.com/api/v0/networks/{networkId}"
networkId = 'L_646829496481105433'
payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data=payload)

print(response.text.encode('utf8'))
