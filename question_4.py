def reverse_string(og_string):
    reversed_string = ""

    for i in range(len(og_string)-1, -1, -1):
        reversed_string += og_string[i]

    return reversed_string


print (reverse_string("programming"))