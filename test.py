import requests
import json

url = 'http://127.0.0.1:8000/get_image/'

payload = {
    "lat": 41.8982208,
    "lon": 12.4764804,
    "iter": 3
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)

