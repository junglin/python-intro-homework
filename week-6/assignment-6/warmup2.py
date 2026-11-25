# Write two functions:
# celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
# fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
# Call each with a few test values and print the results. Use f-strings and round to one decimal place.

# Example output — your test values and wording might differ:

# 0°C = 32.0°F
# 100°C = 212.0°F
# 72°F = 22.2°C

def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius

print(f"{0} °C is {round(celsius_to_fahrenheit(0),1)} °F.")
print(f"{100} °C is {round(celsius_to_fahrenheit(100),1)} °F.")
print(f"{72} °F is {round(fahrenheit_to_celsius(72),1)} °C.")