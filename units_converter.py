temperature = input("Enter the temperature in format (11F, 24C, 11R) :")
convert_to = input("What to convert temperature to? (C,F,R) :")

num_temp = int(temperature[:-1])  # take all numbers except last symbol
convert_from = temperature[-1]

if convert_from.upper() == "C" and convert_to.upper() == 'F':
    res = int(round((num_temp * (9/5) + 32)))
elif convert_from.upper() == "C" and convert_to.upper() == 'R':
    res = int(round((num_temp + 273.15) * (9/5)))
elif convert_from.upper() == "F" and convert_to.upper() == 'C':
    res = int(round((num_temp - 32) * 5 / 9))
elif convert_from.upper() == "F" and convert_to.upper() == 'R':
    res = int(round(num_temp + 459.67))
elif convert_from.upper() == "R" and convert_to.upper() == 'C':
    res = int(round((num_temp - 491.67) * 5 / 9))
elif convert_from.upper() == "R" and convert_to.upper() == 'F':
    res = int(round(num_temp - 459.67))
else:
    print("Input proper convention.")
    quit()

print("You converted", temperature, "to", str(res)+convert_to)
