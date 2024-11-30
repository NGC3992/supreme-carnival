import temp

print("Celsius to Farenheit to Kelvin coverter.")
valid_units = ("celsius","farenheit","kelvin")
symbols = ('C', 'F', 'K')

while True:
	fromUnit = (input("What is the unit that has to be converted (Celsius/Farenheit/Kelvin): ")).lower()
	toUnit = (input("What unit should it be converted to (Celsius/Farenheit/Kelvin): ")).lower()

	if fromUnit not in valid_units or toUnit not in valid_units or fromUnit==toUnit:
		print("Please choose from the available values and ensure the units are different.")
	else:
		break

val = float(input("Enter the value of the temperature: "))

if fromUnit == "celsius" and toUnit == "farenheit":
	r = temp.celcfar(val)

elif fromUnit == "celsius" and toUnit == "kelvin":
	r = temp.celckel(val)

elif fromUnit == "farenheit" and toUnit == "celsius":
	r = temp.farcelc(val)

elif fromUnit == "farenheit" and toUnit == "kelvin":
	r = temp.farkel(val)

elif fromUnit == "kelvin" and toUnit == "celsius":
	r = temp.kelcelc(val)

elif fromUnit == "kelvin" and toUnit == "farenheit":
	r = temp.kelfar(val)

print(f'The temperature is {r} {symbols[valid_units.index(toUnit)]}.')
