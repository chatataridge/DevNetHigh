import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'M2EyYzY4ZjctMGRiYS00ZGI1LWI0MGUtOWIwNjhiNzQyNmJmZmQ4NGFjMDktOTc4_PF84_55609b58-8953-4e48-a3e4-f03e857c3ac6'

httpHeaders = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + access_token}

body = {'toPersonEmail': 'nfeingold@ceriumnetworks.com', 'description':'title', 'title': 'DevNetTest', 'text': 'Hello'}

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)
text = response.json()
roomid = text["id"]

print(roomid)
print(response.status_code)
print(response.text)

apiUrl = 'https://webexapis.com/v1/rooms'

test = requests.post()

messages = [
     '**Warning!!!**',
     '_Warning!!!_',
     '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
]

for message in messages:

     body = {'toPersonEmail': 'gifbot@webex.bot', 'markdown': message}
     response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

     print(response.status_code)
     print(response.text)



