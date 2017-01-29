temp = float(input("Pleas enter the temperature: "))
windspeed = float(input("Pleas enter the windspeed: "))

windchill = 13.12 + 0.6215 * temp - 11.37 * windspeed**0.16 + 0.3965 * temp * windspeed**0.16
print("The windchill is", round(windchill, 1), "C.")
