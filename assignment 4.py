def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))


fahrenheit = celsius_to_fahrenheit(celsius)


print("Temperature in Fahrenheit:", fahrenheit)
