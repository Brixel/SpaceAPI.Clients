import json, requests

url = 'http://space.visionsandviews.net/spaceapi/admin'
openUrl = 'http://space.visionsandviews.net/spaceapi/admin/open'
params = dict()
headers = {'user-agent': 'my-app/0.0.1', 'AUTH' : ''}
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print(data)
print("\n")
print("Open space")
openUrl = 'http://space.visionsandviews.net/spaceapi/admin/open'
params = dict()

resp = requests.get(url=openUrl, params=params, headers=headers)

data = json.loads(resp.text)
print(data)
print("\n")
print("Close space")
closeUrl = 'http://space.visionsandviews.net/spaceapi/admin/close'
params = dict()

resp = requests.get(url=closeUrl, params=params, headers=headers)
data = json.loads(resp.text)
print(data)
