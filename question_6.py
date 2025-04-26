def sum_digits_number(number):
    n = 0
    while number > 0:
        n += number % 10  # Extract the last digit and add it to the sum
        number = number // 10  # Remove the last digit
    return n

print("Sum of the digits of 943563: " + str(sum_digits_number(943563)))