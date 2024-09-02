# # 1 Given a string, how would you convert it into a list of characters?
# input_string = "Anand Raj"
# char_list = []
# for char in input_string:
#     char_list.append(char)
# print(char_list)


# # 2 type conversion
# a = "12.2"
# b=float(a)
# t= type(b)
# print(t)


# # 3. Indexing and Slicing
# # How do you access the last three elements of a list? Write the code.
# list2 = [1, 2, 3, 4, 5, 6, 7,8,9,10]
# last_3_element = []
# for i in range(len(list2) - 3, len(list2)):
#     last_3_element.append(list2[i])
# print(last_3_element)


# # 4. Write a code snippet to reverse a list using slicing.
# list4 = [1, 2, 3, 4, 5,6,7,8,9,10]
# rev_lsit = []
# for i in range(len(list4) - 1, -1, -1):
#     rev_lsit.append(list4[i])
# print(rev_lsit)

# # 5. Write a code snippet to reverse a list using slicing.
# list4 = ["anand","raj"]
# rev_lsit = []
# for i in range(len(list4) - 1, -1, -1):
#     rev_lsit.append(list4[i])
# print(rev_lsit)

# # 6. Accessing Nested Lists
# # how do you access the element 'j'?
# l = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i', 'j']]]
# print(l[1][6][3])

# # 7. Modifying Nested Lists
# # Change the element 'h' to 'H' in the nested list l.
# l = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i', 'j']]]
# l[1][6][1]="H"
# print(l)

# 8. Nested List Length
# Calculate the total number of elements in the entire nested list structure.

# l = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],['a', 'b', 'c', 'd', 'e', 'f', ['g', 'h', 'i', 'j']]]
# lenth_l=len(l[0])+len(l[1][:6])+len(l[1][6])
# print(lenth_l)


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

# first list
first_l = l[0]
n = len(first_l)
for i in range(n // 2):
    first_l[i], first_l[n - i - 1] = first_l[n - i - 1], first_l[i]

# reverse the entire list
n = len(l)
for i in range(n // 2):
    l[i], l[n - i - 1] = l[n - i - 1], l[i]
# print the reversed list
print(l)


# # 10. Find the minimum , maximum and average value in the list
# list1 = [5, 8, 12, 20, 3, 7]

# # Step 1: Find the maximum value
# max_value = list1[0]
# for k in list1:
#     if k > max_value:
#         max_value = k
# print("max value :",max_value)

# # Step 2: Find the minimum value
# min_value = list1[0]
# for k in list1:
#     if k < min_value:
#         min_value = k
# print("min value:",min_value)

# # Step 3: Calculate the average
# total_sum = 0
# count = 0
# for k in list1:
#     total_sum = total_sum+k
#     count = count+1
# average = total_sum / count
# print("average value :", average)

# # Step 4: Count the number of elements greater than the average
# count_greaterthan_average = 0
# for k in list1:
#     if k > average:
#         count_greaterthan_average += 1
# print("value greater than average alue :", count_greaterthan_average)


# Dictnory
# 11.
# squares_dict = {}
# i = 1
# j = 10
# for num in range(i, j + 1):
#     squares_dict[num] = num ** 2
# print("Dictionary of numbers and their squares:")
# print(squares_dict)


# # 12.
# # list of key value pair
# pairs = [("apple", 10),("banana", 5),("cherry", 15),("date", 7)]

# # Creating dictionary
# dict = {}
# for key, value in pairs:
#     dict[key] = value

# # maximum value
# max_key = None
# max_value = -float('inf')  # Initialize to small value
# for key in dict:
#     if dict[key] > max_value:
#         max_value = dict[key]
#         max_key = key
# print("Maximum Key:", max_key)

# # minimum value
# min_key = None
# min_value = float('inf')  # Initialize to a very large value
# for key in dict:
#     if dict[key] < min_value:
#         min_value = dict[key]
#         min_key = key
# print("Minimum Key:", min_key)
# # average value
# total_sum = 0
# count = 0
# for key in dict:
#     total_sum += dict[key]
#     count += 1
# average_value = total_sum / count
# print("Average Value:", round(average_value, 2))
# # count greater than the average
# count = 0
# for key in dict:
#     if dict[key] > average_value:
#         count += 1
# print("Coun greter than average:", count)



# # 13. Merge Two Dictionaries
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# merged_dict = dict1.copy()  # Create a copy to avoid modifying the original
# for key in dict2:
#     merged_dict[key] = dict2[key]

# print(merged_dict)


# # 14. Count Occurrences of Values
# data = {
#     'list1': [1, 2, 2],
#     'list2': [2, 3],
#     'list3': [3, 3, 4]
# }

# occurrences = {}
# for key in data:
#     for value in data[key]:
#         if value in occurrences:
#             occurrences[value] += 1
#         else:
#             occurrences[value] = 1

# print(occurrences)


# # 15. Find the Key with the Maximum Value
# scores = {'Alice': 85, 'Bob': 90, 'Charlie': 88}

# max_key = None
# max_value = -float('inf')
# for key in scores:
#     if scores[key] > max_value:
#         max_value = scores[key]
#         max_key = key

# print(max_key)


# # 16.Remove Keys with Specific Value
# grades = {'math': 90, 'english': 80, 'science': 90}
# value_to_remove = 90

# keys_to_remove = [key for key in grades if grades[key] == value_to_remove]

# for key in keys_to_remove:
#     del grades[key]

# print(grades)


# # 17. Invert a Dictionary
# original_dict = {'a': 1, 'b': 2, 'c': 3}

# inverted_dict = {}
# for key in original_dict:
#     inverted_dict[original_dict[key]] = key

# print(inverted_dict)


# # 18.  Sum Values of a Dictionary
# expenses = {'rent': 1000, 'utilities': 300, 'groceries': 150}

# total = 0
# for value in expenses.values():
#     total += value

# print(total)


# # 19.Filter Dictionary by Value Range
# data = {
#     'a': 10,
#     'b': 25,
#     'c': 30,
#     'd': 45,
#     'e': 50
# }
# lower_bound = 20
# upper_bound = 40

# filtered_dict = {}
# for key in data:
#     if lower_bound <= data[key] <= upper_bound:
#         filtered_dict[key] = data[key]

# print(filtered_dict)


# # 20. Merge Dictionaries and Track Conflicts
# dict1 = {'x': 1, 'y': 2, 'z': 3}
# dict2 = {'y': 5, 'z': 6, 'a': 7}

# merged_dict = {}

# for d in (dict1, dict2):
#     for key in d:
#         if key in merged_dict:
#             if isinstance(merged_dict[key], list):
#                 merged_dict[key].append(d[key])
#             else:
#                 merged_dict[key] = [merged_dict[key], d[key]]
#         else:
#             merged_dict[key] = d[key]

# print(merged_dict)


# # 21    .Find Common Keys with Value Mismatch
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict2 = {'b': 2, 'c': 5, 'e': 6}

# common_keys_mismatch = {}

# for key in dict1:
#     if key in dict2 and dict1[key] != dict2[key]:
#         common_keys_mismatch[key] = (dict1[key], dict2[key])

# print(common_keys_mismatch)



# 20/8/2024
# Q1 Write a function that counts the number of vowels in a given string.

# def count_vowel(intput_string):
#     vowel = "aeiouAEIOU"
#     Count = 0
#     for k in intput_string:
#         if k in vowel:
#             count += 1
#     return Count
# input_string = "my name is anand raj"
# vowel_count = count_vowel(input_string)
# print(count_vowel) 