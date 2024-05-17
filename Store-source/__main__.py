import requests
import configparser
import os

global config

print("Loading Directories...")
if os.getcwd != os.path.expanduser("~") + "\\SCOS-Apps":
    try:
        os.chdir(os.path.expanduser("~") + "\\SCOS-Apps")
    except:
        os.mkdir(os.path.expanduser("~") + "\\SCOS-Apps")
        os.chdir(os.path.expanduser("~") + "\\SCOS-Apps")

config = configparser.ConfigParser()
fileRead = configparser.ConfigParser()
fileRead.read("store.ini")

url = "https://raw.githubusercontent.com/" + fileRead["Info"]["storeManager"] + "/main/store-list.ini"

url2 = "https://raw.githubusercontent.com/" + fileRead["Info"]["storeManager"] + "/main/"

try:
    print("Loading Store Source...")
    r = requests.get(url)
except:
    print("Connection error, check Wi-Fi settings.")
    exit(1)

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
                try:
                    os.mkdir(config["Apps"]["dir-" + str(x)])
                except:
                    print("Error 001: App has already been installed.")
                else:
                    try:
                        for x in requests.get(url2 + "App-source/" + config["Apps"]["dir-" + str(x)] + "/__install__.py").content.decode():
                            open("__install__.py").write(x)
                    except:
                        print("Error 002: Installation error. (Check connection or remaining space.)")
    elif command == "2":
        req = input("> Remove: ")
        try:
            print("Removing Files for app " + req + "...")
            os.rmdir(req)
        except:
            print("Error 003: ")
    if (command == "3"):
        exit()