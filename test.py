import os
from pyhunter import PyHunter

api = "44ac9d0fcf060465933c1591d75c2ace4b1692d8"
hunter = PyHunter(api)






email = "zakkaya@ankara.edu.tr"
list = ["mx_records", "smtp_server", "smtp_check"]
result = hunter.email_verifier(email)
for i in list:
    os.system("echo " + i + " = " + str(result[i]) + " >> " + email + ".txt")
