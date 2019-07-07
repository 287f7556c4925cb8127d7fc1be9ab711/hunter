import os

try:
    os.system("apt-get install python-pip3")
    os.system("apt-get install figlet")
    os.system("pip3 install pyhunter")
except:
    os.system("pkg install python-pip3")
    os.system("pkg install figlet")
    os.system("pip3 install pyhunter")
