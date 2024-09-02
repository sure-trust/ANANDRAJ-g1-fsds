# 9. Reverse the Nested List:
l = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i', 'j']]
]

# innermost list first 
nested_l = l[1][6] 
n = len(nested_l) #nested_l =['g', 'h', 'i', 'j']
for i in range(n // 2):
    nested_l[i], nested_l[n - i - 1] = nested_l[n - i - 1], nested_l[i]

# second list
second_l = l[1] 
n = len(second_l) 
for i in range(n // 2):
    second_l[i], second_l[n - i - 1] = second_l[n - i - 1], second_l[i]
   #getting [['g', 'h', 'i', 'j'], 'f', 'e', 'd', 'c', 'b', 'a']
# first list
first_l = l[0]
n = len(first_l)
for i in range(n // 2):
    first_l[i], first_l[n - i - 1] = first_l[n - i - 1], first_l[i]
  ## getting [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# reverse the entire list
n = len(l)
for i in range(n // 2):
    l[i], l[n - i - 1] = l[n - i - 1], l[i]
   ##getting [['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i', 'j']], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

# print the reversed list
print(l)


# Q1) print first 5 element from the list and then store in the touple
# Sample list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Get the first 5 elements from the list
first_five_elements = my_list[:5]

# Convert the sliced list to a tuple
my_tuple = tuple(first_five_elements)

# Print the tuple
print(my_tuple)

#output (10, 20, 30, 40, 50)


## print last 5 element from the list and then store in the touple 
# Sample list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Get the first 5 elements from the list
first_five_elements = my_list[:5]

# Convert the sliced list to a tuple
my_tuple = tuple(first_five_elements)

# Print the tuple
print(my_tuple)
##output (10, 20, 30, 40, 50)


##2Print last five elements from a list and then store in a tuple.
# Sample list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Get the last 5 elements from the list
last_five_elements = my_list[-5:]

# Convert the sliced list to a tuple
my_tuple = tuple(last_five_elements)

# Print the tuple
print(my_tuple)
##output (60, 70, 80, 90, 100)


"""##3. Write program to print below
    * Skips every two elements of the input.
    * Starts with the second element of the input list.
    * Has four elements."""
# Sample list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Skip every two elements starting from the second element
result = my_list[1::3][:4]

# Print the result
print(result)
[20, 50, 80]


"""##4. Create a function mult_five, given a sorted list of integers from 0 to 95, returns a list of multiples of 5.
    * Print multiples of 4 and 6
    * Print multiples of 13"""
def mult_five(nums):
    # Return multiples of 5 from the list
    multiples_of_5 = [num for num in nums if num % 5 == 0]
    return multiples_of_5

def print_multiples(nums, divisor):
    # Print multiples of the given divisor
    multiples = [num for num in nums if num % divisor == 0]
    print(f"Multiples of {divisor}: {multiples}")

# Sample sorted list of integers from 0 to 95
nums = list(range(0, 96))

# Get and print multiples of 5
multiples_of_5 = mult_five(nums)
print("Multiples of 5:", multiples_of_5)

# Print multiples of 4 and 6
print_multiples(nums, 4)
print_multiples(nums, 6)

# Print multiples of 13
print_multiples(nums, 13)

"""##output Multiples of 5: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
Multiples of 4: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]
Multiples of 6: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]
Multiples of 13: [0, 13, 26, 39, 52, 65, 78, 91]"""




