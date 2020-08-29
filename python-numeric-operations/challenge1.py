# celsius = (fahrenheit - 32) * 5 / 9

print('What is the temperature in fahrenheit?')

ftemp = input()

if ftemp.isnumeric():
    celsius = round((int(ftemp) - 32) * 5 / 9)
    celsius=(celsius).__str__()
    print("Temperature in celsius is: " + celsius)
    exit()

else:
    print('Input is not a number.')

    