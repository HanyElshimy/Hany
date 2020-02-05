"""
note: to be able to use this file, make sure you have downloaded the following
* pip install requests
"""


import requests
import json

key = "ENTER_YOUR_KEY_HERE"

url = "https://gender-api.com/get?"

while True:
        name = input("enter name: ").strip()
        if name == 'q':
                break
        params = {
        "key" : key,
        "name":name
        }
        res = requests.get(url, params=params)
        res = json.loads(res.text)
        print(res['gender'])


