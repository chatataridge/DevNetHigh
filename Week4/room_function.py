import requests

apiUrl = 'https://webexapis.com/v1/rooms'
apiUrl2 = 'https://webexapis.com/v1/messages'

access_token = 'M2EyYzY4ZjctMGRiYS00ZGI1LWI0MGUtOWIwNjhiNzQyNmJmZmQ4NGFjMDktOTc4_PF84_55609b58-8953-4e48-a3e4-f03e857c3ac6'

httpHeaders = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + access_token
}



def createroom():
    body = {'title': 'DevNet High 2020'}

    response = requests.post(url=apiUrl, json=body, headers=httpHeaders)
    text = response.json()
    roomid = text["id"]

    print(roomid)
    print(response.status_code)
    print(response.text)
    return roomid

def message():
    roomid2 = createroom()
    body = {'text':'My first post to a room using an API','roomId':roomid2}
    response = requests.post(url=apiUrl2, json=body, headers=httpHeaders)
    print(response.status_code)
    print(response.text)


message()


