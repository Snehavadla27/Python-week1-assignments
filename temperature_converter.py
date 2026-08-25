def celsius_fahrenheit(celsius):
    fahrenheit=(celsius * 9/5)+32
    return fahrenheit

print("Temperature converter")
celsius=float(input("Enter temperature in celsius:"))
result=celsius_fahrenheit(celsius)
print("temperature in fahrenheit:", result)
