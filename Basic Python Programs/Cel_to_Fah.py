# Program to convert Celsius to Fahrenheit
# This program takes a temperature in Celsius as input from the user and converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. The result is then printed to the console.
# The formula for converting Celsius to Fahrenheit is derived from the fact that the freezing point of water is 0 degrees Celsius and 32 degrees Fahrenheit, and the boiling point of water is 100 degrees Celsius and 212 degrees Fahrenheit. The ratio of the difference in temperature between the freezing and boiling points in Fahrenheit to the difference in temperature in Celsius is 9/5, which is why we multiply the Celsius temperature by 9/5. Finally, we add 32 to shift the scale from Celsius to Fahrenheit.
# For example, if the user enters 25 degrees Celsius, the program will calculate the Fahrenheit equivalent as follows:
# F = (25 * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is: ", fahrenheit)