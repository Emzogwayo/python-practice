# This is the solution for summing elements of a list
mylist = [23, 34, 54, 1, 654] # List of numbers to add

def sumlist(mylist): #function to return the sum of the numbers in the list
    x=0  # Initialize sum to 0
    for y in mylist:
        x=x+y # Add each element to the total
    return x

total = sumlist(mylist) # Call the function and store the result in 'total'
print ("The sum of this 23, 34, 54, 1 and 654 is = " + str(total)) # Print the result
