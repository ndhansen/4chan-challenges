accnumber = input("Please enter an account or credit card number: ")

last_digit = accnumber[-1:]
luhn = accnumber[:-1]
luhn = luhn[::-1]

total = 0
for i in range(len(luhn)):
    digit = int(luhn[i])
    if i % 2 == 0:
        double_digit = digit * 2
        if double_digit > 9:
            double_digit -= 9
        total += double_digit
    else:
        total += digit

if (total % 10 + int(last_digit)) == 10:
    print("This is a valid account number")
else:
    print("Not a valid account number")
