import os
import optparse
from pyhunter import PyHunter

api = "44ac9d0fcf060465933c1591d75c2ace4b1692d8"

"""
def get_user_input():
    parse = optparse.OptionParser()
    parse.add_option("-d", "--domain", dest="domain", help="hedef domain adres")
    return parse.parse_args()
"""


def domain_search(domain):
    result = hunter.domain_search(domain)
    result = result["emails"]
    values = ["first_name", "last_name", "phone_number", "value"]
    keys = ["ad", "soyad", "telefon", "email"]

    for i in range(len(result)):
        for j in range(len(keys)):
            os.system("echo " + keys[j] + " = " + str(result[i][values[j]]) + " >> deneme.txt")
        os.system("echo " + "-----------------------------------------" + " >> deneme.txt")


# def email_finder():


# def email_verifier():

hunter = PyHunter(api)
os.system("figlet TurkHackTeam\n")
print("İstihbarat Tim Osint Hunter Aracına Hoş Geldiniz")
print("""
1 - Domain Arama
2 - Email Bulma
3 - Email Doğrulama
0 - Çıkış
""")
choise = input("Yapmak İstediğiniz İşlemi Seçiniz = ")

if (choise == "1"):
    domain = input("\nHedef Domain Giriniz = ")
    domain_search(domain)

# elif (choise == "2"):

# elif (choise == "3"):

elif (choise == "0"):
    print("\nNE MUTLU TÜRKÜM DİYENE")

else:
    print("Hatalı Bir Seçim Yaptınız, Tekrar Deneyiniz..")
