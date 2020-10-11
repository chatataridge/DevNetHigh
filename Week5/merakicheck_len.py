from webexteamssdk import WebexTeamsAPI
import requests


meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

msversion = '11.31'
mrversion = '26.6.1'
mxversion = '15.27'
mvversion = '4.0'
WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vZmIwMWQ2MjAtZGU0Ni0xMWVhLWE3OTMtN2Q3YTJiMWQ1YmNj"
myWebexToken = "" #you will need to put your personal token here

baseurl = "https://dashboard.meraki.com/api/v0/networks/"

payload = {}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": meraki_api_key
}

url = baseurl+/mynetwork/+/devices

#response = requests.request("GET", url, headers=headers, data=payload)

response = requests.get(url, headers=headers, data=payload)

myresponse = response.json()


