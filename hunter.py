from pyhunter import PyHunter

api = "44ac9d0fcf060465933c1591d75c2ace4b1692d8"

hunter = PyHunter(api)

result = hunter.domain_search("ankara.edu.tr")
result = result["emails"]

for i in range(len(result)):
    print("-----------------------------------------")
    print("|  ad = ", result[i]["first_name"])
    print("|  soyad = ", result[i]["last_name"])
    print("|  telefon = ", result[i]["phone_number"])
    print("|  email = ", result[i]["value"])
    print("-----------------------------------------")
    print("\n")
