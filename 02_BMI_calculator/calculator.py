weight = float(input("What is your weight (kg)? "))
height = float(input("What is your height (m)? "))

print("Your BMI is", round(weight / (height ** 2), 1))
