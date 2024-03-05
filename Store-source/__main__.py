import requests

url = "https://raw.githubusercontent.com/SCOS-Apps/SCOS-App-Store/main/store-list.ini"

r = requests.get(url)

print(r.content)

if __name__ == "__main__":
    print("hello")
else:
    print("Sorry, you cannot run the store from another app.")