import requests
import configparser
import os

global config

if os.getcwd != os.path.expanduser("~") + "\\SCOS-Apps":
    try:
        os.chdir(os.path.expanduser("~") + "\\SCOS-Apps")
    except:
        os.mkdir(os.path.expanduser("~") + "\\SCOS-Apps")
        os.chdir(os.path.expanduser("~") + "\\SCOS-Apps")

config = configparser.ConfigParser()

url = "https://raw.githubusercontent.com/SCOS-Apps/SCOS-App-Store/main/store-list.ini"

url2 = "https://raw.githubusercontent.com/SCOS-Apps/SCOS-App-Store/main/"

r = requests.get(url)

content = r.content.decode()

config.read_string(content)

print("This store is managed by: " + config["App-Store"]["store-url"] + ". If the GitHub repo isn't correct, please modify your source.")

print("SCOS Store v1.0")
print("Commands:\n1. Install\n2. Remove\n3. Exit")
while True:
    command = input("> ")
    print(command)
    if (command == "1"):
        req = input("> Install > App: ")
        for x in range(1, int(config["Apps"]["app-list"])):
            if config["Apps"]["name-" + str(x)] == req:
                #print("YES")
                print("Dir: " + config["Apps"]["dir-" + str(x)])
                #exec(requests.get(url2 + "App-source/" + config["Apps"]["dir-" + str(x)] + "/__install__.py").content.decode())
                try: os.mkdir(config["Apps"]["dir-" + str(x)]) except: print("Error 001: App has already been installed.")
    if (command == "3"):
        exit()