# Q1 Find the sum of elements in a list.

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
sum_of_list_a = sum(float(item) for item in list_a if isinstance(item, (int, float)))
print("Sum of list_a in the list:", sum_of_list_a)

# Q2 Find the Largest Element

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
numeric_list = [float(item) for item in list_a if isinstance(item, (int, float))]
largest = numeric_list[0]
for num in numeric_list:
    if num > largest:
        largest = num
print("Largest element :", largest)

# Q2.2 Find the Smallest Element

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
numeric_list = [float(item) for item in list_a if isinstance(item, (int, float))]
smallest = numeric_list[0]
for num in numeric_list:
    if num < smallest:
        smallest = num
print("Smallest element :", smallest)

# 3. Write a program to find the index of '1'.

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
try:
    index_of_one = list_a.index('1')
    print("The index of '1' is:", index_of_one)
except ValueError:
    print("'1' is not in the list.")

# 4. Write a program to separate all data type objects and store it in different collections.

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
integers = []
floats = []
strings = []
others = [] 
for item in list_a:
    if isinstance(item, int):
        integers.append(item)
    elif isinstance(item, float):
        floats.append(item)
    elif isinstance(item, str):
        strings.append(item)
    else:
        others.append(item)

print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
print("Others:", others)

# 5. Write a program to find duplicate items in the list. Print all items which are not duplicates.

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
seen = set()
duplicates = set()
for item in list_a:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
non_duplicates = [item for item in list_a if item not in duplicates]

print("Duplicate items:", duplicates)
print("Non-duplicate items:", non_duplicates)


# 6. Write a program to find the frequency of each element in the list.

list_a = [1, 2, 36.7, 0.9, '1', 9, 27, 31, 0, 1.1, 34, 2, 3.4, 7, 3, 2]
frequency_dict = {}
for item in list_a:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

for item, frequency in frequency_dict.items():
    print(f"Element: {item} - Frequency: {frequency}")


