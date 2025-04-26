def compute_factorial_loop(number):
    n = 1
    if number == 0:
        return 1 # factorial of 0 is 1
    
    for i in range(1, number + 1):
        n = n * i # Multiply result by i at each step

    return n

print ("3! = " + str(compute_factorial_loop(3))) #example for the number 3
print ("0! = " + str(compute_factorial_loop(0))) #example for the number 0
