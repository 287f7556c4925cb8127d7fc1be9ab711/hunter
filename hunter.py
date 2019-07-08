# -*- coding: utf-8 -*-

import os
from pyhunter import PyHunter


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
    print("\n" + result[0])


def email_verifier(email):
    result = hunter.email_verifier(email)
    if (result["smtp_check"]):
        print("\nsmtp_check = " + str(result["smtp_check"]) + "\t--->\tBöyle Bir Email Adresi Vardır")
    else:
        print("\nsmtp_check = " + str(result["smtp_check"]) + "\t--->\tBöyle Bir Email Adresi Yoktur")


try:
    while (True):
        api = "44ac9d0fcf060465933c1591d75c2ace4b1692d8"
        hunter = PyHunter(api)
        info = (hunter.account_information())
        os.system("clear")
        os.system("figlet TurkHackTeam\n")
        print("\033[94mİstihbarat Tim Osint Hunter Aracına Hoş Geldiniz")

        if (info["calls"]["left"] != 0):
            print("Mevcut Api İçin Kalan Arama Hakkı  = " + info["calls"]["left"])
            print("""
            1 - Domain Arama
            2 - Email Bulma
            3 - Email Doğrulama
            0 - Çıkış
            """)
            choise = input("Yapmak İstediğiniz İşlemi Seçiniz = ")

            if (choise == "1"):
                domain = input("\nHedef Domain Giriniz (turkhackteam.org) = ")
                domain_search(domain)

            elif (choise == "2"):
                domain = input("\nİlgili Domain/Şirket Giriniz (org) = ")
                ad = input("İlgili Kullanıcı Adı Giriniz (emre) = ")
                soyad = input("İlgili Kullanıcı Soyadı Giriniz (öztürk) = ")
                email_finder(domain, ad, soyad)

            elif (choise == "3"):
                email = input("\nİlgili Email Adresini Giriniz (root@turkhackteam.org) = ")
                email_verifier(email)

            elif (choise == "0"):
                print("\n\033[91mNE MUTLU TÜRKÜM DİYENE")
                break

            else:
                print("Hatalı Bir Seçim Yaptınız, Tekrar Deneyiniz..")

        else:
            print("\nMevcut Api Arama Hakkı Bitti")
            print("""
                1 - Yeni Api Eklemek
                0 - Çıkış Yapamk
                """)

            choise = input("Yapmak İstediğiniz İşlemi Seçiniz = ")

            if (choise == "1"):
                api = input("\nYeni Api Değerini Giriniz = ")
            elif (choise == "0"):
                print("\n\033[91mNE MUTLU TÜRKÜM DİYENE")
                break
            else:
                print("Hatalı Bir Seçim Yaptınız, Tekrar Deneyiniz..")


except(KeyboardInterrupt):
    print("\nÇıkış Yaptınız..")
except:
    print("\nBir Hata Oluştu..")
finally:
    print("\nposew7@turkhackteam.org")
