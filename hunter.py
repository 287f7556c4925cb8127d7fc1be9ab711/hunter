import os
from pyhunter import PyHunter

api = "44ac9d0fcf060465933c1591d75c2ace4b1692d8"
hunter = PyHunter(api)


def domain_search(domain):
    result = hunter.domain_search(domain)
    result = result["emails"]
    values = ["first_name", "last_name", "phone_number", "value"]
    keys = ["ad", "soyad", "telefon", "email"]

    for i in range(len(result)):
        for j in range(len(keys)):
            os.system("echo " + keys[j] + " = " + str(result[i][values[j]]) + " >> " + domain + ".txt")
        os.system("echo " + "-----------------------------------------" + " >> " + domain + ".txt")
    print("\nSonuçlar " + domain + ".txt Olarak Kayıt Edildi..")


def email_finder(ad, soyad, domain):
    ad_soyad = ad + " " + soyad
    result = hunter.email_finder(company=domain, full_name=ad_soyad)
    result2 = hunter.email_finder(company=domain, full_name=ad_soyad, raw=True)
    print(result[0])
    print(result2)


def email_verifier(email):
    list = ["mx_records", "smtp_server", "smtp_check"]
    result = hunter.email_verifier(email)
    for i in list:
        os.system("echo " + i + " = " + str(result[i]) + " >> " + email + ".txt")
    print("\nSonuçlar " + email + ".txt Olarak Kayıt Edildi..")


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

elif (choise == "2"):
    domain = input("İlgili Domain/Şirket Giriniz = ")
    ad = input("İlgili Kullanıcı Adı Giriniz = ")
    soyad = input("İlgili Kullanıcı Soyadı Giriniz = ")
    email_finder(domain, ad, soyad)

elif (choise == "3"):
    email = input("İlgili Email Adresini Giriniz = ")
    email_verifier(email)

elif (choise == "0"):
    print("\nNE MUTLU TÜRKÜM DİYENE")

else:
    print("Hatalı Bir Seçim Yaptınız, Tekrar Deneyiniz..")
