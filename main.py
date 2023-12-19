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

print(f"The arithmetic mean: {(number1 + number2 + number3) / 3}")

metrs = int(input("Enter number of meters:"))
print(f"Miles: {metrs * 0.00062137119609836} \nInches: {metrs * 39.370078740157} \nYards: {metrs * 1.0936132983377}")