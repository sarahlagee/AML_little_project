import requests
import json
import time

url = "https://api.etherscan.io/api"

payload={"module": "account",
         "action": "txlist",
         "address": "0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC",
         "startblock": 15000000,
         "endblock": 15000099,
         "page": 1,
         "sort": "desc",
         "apikey": ""}
headers = {
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

result = json.loads(response.text)['result']
target = 16000000
store = []
cnt = 0
while(payload["startblock"] <= target):
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)['result']
    store += result
    payload["startblock"] = payload["startblock"] + 100
    payload["endblock"] =  payload["startblock"] + 99
    cnt += 1
    if(cnt % 5 == 0):
        time.sleep(1)
    print(len(store))

print(len(store))
