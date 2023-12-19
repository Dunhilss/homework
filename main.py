number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 >= number2 and number1 >= number3:
    print(f"Highest number is: {number1}")
elif number2 >= number1 and number2 >= number3:
    print(f"Highest number is: {number2}")
elif number3 >= number1 and number3 >= number2:
    print(f"Highest number is: {number3}")
else: print(f"Try again...")

if number1 <= number2 and number1 <= number3:
    print(f"Highest number is: {number1}")
elif number2 <= number1 and number2 <= number3:
    print(f"Highest number is: {number2}")
elif number3 <= number1 and number3 <= number2:
    print(f"Highest number is: {number3}")
else: print(f"Try again...")