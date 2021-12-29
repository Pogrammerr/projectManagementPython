import requests

url = 'https://pulsar-d67ef-default-rtdb.firebaseio.com/maticIceAsteroids.json'
headers = {'Content-Type': 'application/json'}
response = requests.get(url, headers)

if response.status_code == 200:
    print(response.json())
else:
    print("no")