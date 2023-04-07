import requests
from time import sleep
from colorama import *
import os
import time
from colorama import Fore
init(autoreset=True)
var = lambda: os.system('cls')
print(Fore.GREEN+"                                                                                                                                                                                                     ")
time.sleep(.2)
time.sleep(.2)
print(Fore.RED+     "  /$$$$$$            /$$       /$$                                 /$$$$$$$$                                  ")
time.sleep(.2)
print(Fore.YELLOW+  " /$$__  $$          |__/      | $$                                |__  $$__/                                  ")
time.sleep(.2)
print(Fore.GREEN+   "| $$  \__/  /$$$$$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$                | $$     /$$$$$$   /$$$$$$  /$$$$$$/$$$$ ")
time.sleep(.2)
print(Fore.RED+     "|  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$               | $$    /$$__  $$ |____  $$| $$_  $$_  $$")
time.sleep(.2)
print(Fore.YELLOW+  " \____  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \__/               | $$   | $$$$$$$$  /$$$$$$$| $$ \ $$ \ $$")
time.sleep(.2)
print(Fore.GREEN+   " /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$                     | $$   | $$_____/ /$$__  $$| $$ | $$ | $$")
time.sleep(.2)
print(Fore.RED+     "|  $$$$$$/| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$                     | $$   |  $$$$$$$|  $$$$$$$| $$ | $$ | $$")
time.sleep(.2)
print(Fore.YELLOW+  " \______/ | $$____/ |__/ \_______/ \_______/|__/                     |__/    \_______/ \_______/|__/ |__/ |__/")
time.sleep(.2)
print(Fore.GREEN+   "          | $$                                                                                                ")
time.sleep(.2)
print(Fore.RED+     "          | $$                                                                                                ")
time.sleep(.2)
print(Fore.YELLOW+  "          |__/                                                                                                ")
time.sleep(.2)
print(" ")
print(Fore.GREEN + "                              Welcome inside the spider")
print("")
time.sleep(2)
print(Fore.RED+"[Hint] Make sure the urls are inside the urls.txt file!")
file_urls = open("urls.txt",'a')
file_urls.close()
lines = os.path.getsize("urls.txt")
while True:
    number = 0
    ask = input("Are you ready to start the filtering process ( y / n ): ")
    lines = os.path.getsize("urls.txt")
    if ask.lower() == "n":
        break
    elif ask.lower() == "y":
        if lines == 0:
            print(Fore.RED + "[Error] The urls file is empty You have to write the subdomain inside the urls.txt file")
            continue
        status_200 = 0 ; status_300 = 0 ; status_400 = 0 ; others = 0
        while True:

            with open('urls.txt', 'r') as fin:
                x = fin.readline()
            with open('urls.txt', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('urls.txt', 'w') as fout:
                fout.writelines(data[1:])
            lines = os.path.getsize("urls.txt")
            if lines == 0:
                number += 1
                print("The number of sites whose status code contains 200 is:       " + Fore.GREEN+str(status_200))
                print("The number of sites whose status code contains 300 is:       " + Fore.BLUE+str(status_300))
                print("The number of sites whose status code contains 400 is:       " + Fore.RED+str(status_400))
                print("The number of sites whose status code contains not found is: " +Fore.YELLOW+str(others))
                print("the work is done")
                sleep(60)
                break
            #sleep(speed)
            x = str(x.replace("\n",""))
            if x[0:8] == "https://":
                x = x.replace("https://",'')
            if x[0:7] == "http://":
                x = x.replace("http://", '')
            try:
                response = requests.get("https://"+x)
            except:
                others += 1
                print(Fore.YELLOW + "--------------------------------------------\nsubdomain is: " + x)
                print(Fore.YELLOW + "status code is :   [  not found  ]\n" + "number subdomains is: " + str(others) + "\n--------------------------------------------")
                file_300 = open("not_found_site_site.txt", 'a')
                file_300.write(x+"\n")
                file_300.close()
                continue
            status = response.status_code
            if int(status) >= 200 and int(status) < 300:
                status_200 += 1
                print(Fore.GREEN+"--------------------------------------------\nsubdomain is: "+x)
                print(Fore.GREEN+"status code is :   [  "+str(status)+"  ]\n"+"number subdomains is: "+str(status_200)+"\n--------------------------------------------")
                domain = f"{x.split('.')[-2]}_status_code_200.txt"
                file_200 = open(domain,'a')
                file_200.write(x+"\n")
                file_200.close()
                continue
            elif int(status) >= 300 and int(status) < 400:
                status_300 += 1
                print(Fore.BLUE+"--------------------------------------------\nsubdomain is: "+x)
                print(Fore.BLUE+"status code is :   [  "+str(status)+"  ]\n"+"number subdomains is: "+str(status_300)+"\n--------------------------------------------")
                domain = f"{x.split('.')[-2]}_status_code_300.txt"
                file_300 = open(domain, 'a')
                file_300.write(x+"\n")
                file_300.close()
            elif int(status) >= 400 and int(status) < 500:
                status_400 += 1
                print(Fore.RED+"--------------------------------------------\nsubdomain is: "+x)
                print(Fore.RED+"status code is :   [  "+str(status)+"  ]\n"+"number subdomains is: "+str(status_400)+"\n--------------------------------------------")
                domain = f"{x.split('.')[-2]}_status_code_400.txt"
                file_300 = open(domain, 'a')
                file_300.write(x+"\n")
                file_300.close()
            else:
                others += 1
                print(Fore.YELLOW+"--------------------------------------------\nsubdomain is: "+x)
                print(Fore.YELLOW+"status code is :   [  not found  ]\n"+"number subdomains is: "+str(others)+"\n--------------------------------------------")
                file_300 = open("not_found_site_site.txt", 'a')
                file_300.write(x+"\n")
                file_300.close()
    else:
        continue
    if number == 1:
        break