def check_evenorsum(number):
    if number % 2 == 0:
        return ("The number " + str(number) + " is even")
    else:
        return ("The number " + str(number) + " is odd")

print (check_evenorsum(12))
print (check_evenorsum(19))
