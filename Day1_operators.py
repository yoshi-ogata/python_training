print("operators")

#Modulus
print(9 % 2) #1
#Exponentiation
print(2 ** 3) #8
# Floor Division
print(7 // 2) #3.5 -> 3

#Task 
#Area of circle - 
#Expectated output
#Please tell me the radius of the circle? 2
#Area of the circle 12.56

# radius = input("Please tell me the radius of the circle?")
# output = int(radius)
# n = 3.14
# area = output ** 2 * n
# print("Area of the circle", area)

# #Task2 1.2
# radius = input("Please tell me the radius of the circle?")
# output = int(radius)
# n = 3.14
# print(f"Area of the circle is {output ** 2 * n}.")

# Task 2: With f-string
# Fahrenheit to Celcius
# Please provide your Fahrenheit: 98.6
# The 98.6°F is 37°C

# Fahrenheit = input("Please tell me the degrees of Fahrenheit?")
# degrees = float(Fahrenheit)
# Celcius = (degrees - 32) * (5 / 9)
# print(f"The {Fahrenheit}°F is {Celcius}°C.")

# Task 2.2: With f-string
# Fahrenheit to Celcius
# Please provide your Fahrenheit: 100
# The 100°F is 37.78°C'

#snake_case
fahrenheit = input("Please tell me the degrees of Fahrenheit?")
degrees = float(fahrenheit)
celsius = (degrees - 32) * (5 / 9)
C = round(celsius, 2)
print(f"The {fahrenheit}°F is {C}°C.")

