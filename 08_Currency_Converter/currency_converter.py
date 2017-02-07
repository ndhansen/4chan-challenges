import requests
import json

def get_data(base, target):
    r = requests.get('http://api.fixer.io/latest?base=' + base + "&symbols=" + target)
    return json.loads(r.content.decode("utf-8"))

while True:
    print("1. Convert")
    print("2. Available Currencies")
    print("3. Close")
    choice = int(input("> "))

    if choice == 1:
        currency = input("What is the currency you want to convert from? ")
        amount = float(input("How much " + currency + " are cou converting? "))
        target_currency = input("What is the currency you want to convert to? ")
        data = get_data(currency, target_currency)
        if "error" in data:
            print("ERROR")
            print(data["error"])
            break
        result = amount * data["rates"][target_currency]
        print(amount, currency, "=", result, target_currency)

    elif choice == 2:
        r = requests.get('http://api.fixer.io/latest')
        data = json.loads(r.content.decode("utf-8"))
        for key, value in data["rates"].items():
            print(key)
          
    elif choice == 3:
        break
