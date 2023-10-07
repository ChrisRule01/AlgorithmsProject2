import timeit
import random

# Define array and varibles for the loop
def largest(array):
    left = 0
    right = len(array) - 1

    # Creating the midpoint
    while left < right:
        mid = (left + right) // 2

        # Check which half the largest element is in 
        if array[mid] > array[right]:
            left = mid + 1
        else:
            right = mid
    
    # Because I set the loop to have the var left be less than var right, var left should be the largest element once the loop breaks
    return array[left]
    

#Inital Length of Array
n = 20

# Random numbers based on a 'n' length array between -50 and 50.
while n <= 100000000:
    array = [random.randint(-50, 50) for i in range(n)]
    
    #Sorting the array and then shifting it by a random number of points
    array.sort()
    shiftPositions = random.randint(1, 10)
    array = array[-shiftPositions:] + array[:-shiftPositions]
    
    # Timer for the above while loop
    starttime = timeit.default_timer()
    
    # Calling the binary search function
    largest_num = largest(array)

    #End Time and Print to console
    endtime = timeit.default_timer() 
    print(endtime - starttime)

    # Increment n
    n *= 2



