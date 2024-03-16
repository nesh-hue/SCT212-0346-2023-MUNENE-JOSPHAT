def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

number = int(input("Enter a number: "))

result = sum_of_digits(number)

print("The sum of digits of", number, "is:", result)
