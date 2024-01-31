import requests
import json
import time

url = "http://127.0.0.1:8000/get_image/"

payload2 = {"lat": 41.8982208, "lon": 12.4764804, "zoom": 2, "iter": 1}
payload1 = {"lat": 41.8982208, "lon": 12.4764804, "zoom": 1, "iter": 1}
payload3 = {"lat": 41.8982208, "lon": 12.4764804, "zoom": 3, "iter": 1}
payload4 = {"lat": 41.8982208, "lon": 12.4764804, "zoom": 4, "iter": 1}
payload5 = {"lat": 41.8982208, "lon": 12.4764804, "zoom": 5, "iter": 1}

headers = {"Content-Type": "application/json"}

start = time.time()
response = requests.post(url, json=payload1, headers=headers)
end = time.time()
zoom1 = end - start

start = time.time()
response = requests.post(url, json=payload2, headers=headers)
end = time.time()
zoom2 = end - start

start = time.time()
response = requests.post(url, json=payload3, headers=headers)
end = time.time()
zoom3 = end - start

start = time.time()
response = requests.post(url, json=payload4, headers=headers)
end = time.time()
zoom4 = end - start

start = time.time()
response = requests.post(url, json=payload5, headers=headers)
end = time.time()
zoom5 = end - start


print(response.status_code)
print("zoom1 total time", zoom1)
print("zoom2 total time", zoom2)
print("zoom3 total time", zoom3)
print("zoom4 total time", zoom4)
print("zoom5 total time", zoom5)

# benchmarks taken on my computer running local flask server
# zoom1 total time 0.9312729835510254
# zoom2 total time 2.018310070037842
# zoom3 total time 7.2267210483551025
# zoom4 total time 25.869508028030396
# zoom5 total time 105.61002087593079
