import requests
import configparser

global config

config = configparser.ConfigParser()

url = "https://raw.githubusercontent.com/SCOS-Apps/SCOS-App-Store/main/store-list.ini"

r = requests.get(url)

content = r.content.decode()

config.read_string(content)

print("This store is managed by: " + config["App-Store"]["store-url"] + ". If the GitHub repo isn't correct, please modify the file 'auth'.")

print("SCOS Store v1.0")
print("Commands:\n1. Install\n2. Remove\n3. Exit")
while True:
    command = input("> ")
    print(command)
    if (command == "1"):
        req = input("> Install > App: ")
        for x in (config["Apps"]["app-list"]):
            if config["Apps"]["name-" + x] == req:
                print("YES")
                print("Dir: " + config["Apps"]["dir-" + x])
                file = requests.get("https://raw.githubusercontent.com/SCOS-Apps/SCOS-App-Store/main/App-source/" + config["Apps"]["dir-" + x] + "/__install__.py").content
                exec(file.decode())
    if (command == "3"):
        exit()