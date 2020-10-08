import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'M2EyYzY4ZjctMGRiYS00ZGI1LWI0MGUtOWIwNjhiNzQyNmJmZmQ4NGFjMDktOTc4_PF84_55609b58-8953-4e48-a3e4-f03e857c3ac6'

httpHeaders = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + access_token}


queryParams = {'sortBy': 'lastactivity', 'max': '2'}

response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

print(response.status_code)
print(response.text)

