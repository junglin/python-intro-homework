fahrenheit = input("Hello, please enter the temperature in Fahrenheit: ")
official_fahrenheit = float(fahrenheit)
celsius = (official_fahrenheit - 32) * 5 / 9
official_celsius = round(celsius, 1)
print(f"{official_fahrenheit}°F in Celsius is {official_celsius}°C.")
