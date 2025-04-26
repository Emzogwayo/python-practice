def factorial_recursive(number):
    if number == 0:
        return 1 # Base case: factorial of 0 is 1
    else:
        return number * factorial_recursive(number-1) # Recursive step

print("3! = " + str(factorial_recursive(3)))
print("0! = " + str(factorial_recursive(0)))
