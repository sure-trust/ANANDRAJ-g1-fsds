# 1. Count the Number of Vowels in a String
def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)
print(count_vowels("Hello World")) 

 # Output: 3
# 2. Rotate a List by a Given Number of Steps
  
def rotate_list(lst, steps):
    steps = steps % len(lst)  # Handle cases where steps > len(lst)
    return lst[steps:] + lst[:steps]
print(rotate_list([1, 2, 3, 4, 5], 2))  
# Output: [3, 4, 5, 1, 2]

# 3. Find the Second Largest Element in a List
def second_largest(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second
print(second_largest([10, 20, 4, 45, 99]))  
# Output: 45

# 4. Merge Two Sorted Lists into One Sorted List
def merge_sorted_lists(lst1, lst2):
    merged = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged
print(merge_sorted_lists([1, 3, 5], [2, 4, 6])) 
 # Output: [1, 2, 3, 4, 5, 6]

# 5. Remove All Duplicate Elements from a List While Preserving Order
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  
# Output: [1, 2, 3, 4, 5]

# 6. Find the Frequency of All Elements in a List
from collections import Counter
def frequency(lst):
    return dict(Counter(lst))
print(frequency([1, 2, 2, 3, 3, 3]))  
# Output: {1: 1, 2: 2, 3: 3}

# 7. Find the Intersection of Two Lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(intersection([1, 2, 3], [2, 3, 4]))  
# Output: [2, 3]

# 8. Find Common Elements Between Two Dictionaries Based on Values 
def common_elements(dict1, dict2):
    values1 = set(dict1.values())
    values2 = set(dict2.values())
    return values1 & values2
print(common_elements({'a': 1, 'b': 2}, {'x': 2, 'y': 3}))  
# Output: {2}

# 9. Flatten a Nested List into a Single List
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
print(flatten([1, [2, [3, 4], 5], 6]))  
# Output: [1, 2, 3, 4, 5, 6]

# 10. Separate Positive and Negative Integers into Two Lists 
def separate_pos_neg(lst):
    pos = [x for x in lst if x >= 0]
    neg = [x for x in lst if x < 0]
    return pos, neg
print(separate_pos_neg([1, -2, 3, -4, 5]))  
# Output: ([1, 3, 5], [-2, -4])

# 11. Find the First Non-Repeated Character in a String
from collections import Counter
def first_non_repeated_char(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None
print(first_non_repeated_char("swiss"))  
# Output: 'w'

# 12. Remove All Spaces from a String 
def remove_spaces(s):
    return ''.join(s.split())
print(remove_spaces(" Hello   World "))  
# Output: "HelloWorld"

# 13. Check if Two Strings are Anagrams 
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))  
# Output: True

# 14. Reverse the Order of Words in a String 
def reverse_words(s):
    return ' '.join(s.split()[::-1])
print(reverse_words("Hello World   "))  
# Output: "  World Hello"

# 15. Check if a String Contains Only Unique Characters 
def has_unique_chars(s):
    return len(s) == len(set(s))
print(has_unique_chars("abcdef"))  
# Output: True
print(has_unique_chars("aabbcc"))  
# Output: False

# 16. Convert a String from camelCase to snake_case 
def camel_to_snake(s):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in s]).lstrip('_')
print(camel_to_snake("camelCaseString"))  
# Output: "camel_case_string"

# 17. Count the Occurrence of Each Word in a String
from collections import Counter
def word_count(s):
    words = s.split()
    return dict(Counter(words))
print(word_count("hello world hello"))  
# Output: {'hello': 2, 'world': 1}

# 18. Encode a String Using a Caesar Cipher
def caesar_cipher(s, shift):
    result = []
    for char in s:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result.append(chr(start + (ord(char) - start + shift) % 26))
        else:
            result.append(char)
    return ''.join(result)
print(caesar_cipher("abc def", 3))  
# Output: "def ghi"

# 19. Convert a String Representation of a Number into an Integer Without Using int()
def str_to_int(s):
    num = 0
    for char in s:
        num = num * 10 + (ord(char) - ord('0'))
    return num
print(str_to_int("1234"))  
# Output: 1234

# Pandas Basics
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['John', 'Anna'], 'Age': [28, 24]}
df = pd.DataFrame(data)

# Read a CSV file into a DataFrame
df = pd.read_csv('file.csv')

# Display the first 5 rows of a DataFrame
print(df.head())

# Display the last 5 rows of a DataFrame
print(df.tail())

# Difference between loc[] and iloc[]
# loc[] uses labels, iloc[] uses integer-based indexing

# Select a single column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Age']])

# Filter rows based on a condition
print(df[df['Age'] > 25])

# Check for missing values
print(df.isnull().sum())

# Fill missing values with a specific value
df.fillna(0, inplace=True)

# Remove rows with missing values
df.dropna(inplace=True)

# Remove columns with missing values
df.dropna(axis=1, inplace=True)

# Replace values
df.replace({'OldValue': 'NewValue'}, inplace=True)

# Rename columns
df.rename(columns={'OldName': 'NewName'}, inplace=True)

# Convert a column's data type
df['Age'] = df['Age'].astype(float)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# Change the index to a specific column
df.set_index('Name', inplace=True)

# Sort by a specific column
df.sort_values(by='Age', inplace=True)


# Check if two strings are anagrams:
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print("Are they anagrams?:", are_anagrams(s1, s2))
# Reverse the order of words in a string:

   
def reverse_words(s):
    words = s.split()
    return ' '.join(reversed(words))


user_input = input("Enter a string: ")
print("Reversed word order:", reverse_words(user_input))
# Check if a string contains only unique characters:

  
  
def has_unique_characters(s):
    return len(set(s)) == len(s)


user_input = input("Enter a string: ")
print("Contains only unique characters?:", has_unique_characters(user_input))
# Convert a string from camelCase to snake_case:

  
  
def camel_to_snake(s):
    import re
    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s)
    return s.lower()


camel_case_str = input("Enter a camelCase string: ")
print("Converted to snake_case:", camel_to_snake(camel_case_str))
# Count the occurrence of each word in a string:

  
  
def word_count(s):
    from collections import Counter
    words = s.split()
    return dict(Counter(words))


user_input = input("Enter a string: ")
print("Word frequencies:", word_count(user_input))
# Encode a string using a basic Caesar cipher:

  
  
def caesar_cipher(s, shift):
    result = []
    for char in s:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


user_input = input("Enter a string to encode: ")
shift = int(input("Enter the shift value: "))
print("Encoded string:", caesar_cipher(user_input, shift))
# Convert a string representation of a number into an integer without using int():

  
  
def string_to_int(s):
    num = 0
    for char in s:
        num = num * 10 + (ord(char) - ord('0'))
    return num


str_num = input("Enter a string representing a number: ")
print("Converted to integer:", string_to_int(str_num))


# Pandas Questions and Operations
# Create a pandas DataFrame from a dictionary:

  
  
import pandas as pd

# Example dictionary
data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)
print(df)
# Read a CSV file into a pandas DataFrame:

  
  
import pandas as pd

# Make sure to provide the correct file path
file_path = input("Enter the path to the CSV file: ")
df = pd.read_csv(file_path)
print(df.head())  # Display the first 5 rows
# Display the first 5 rows of a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
print(df.head())  # Display the first 5 rows
# Display the last 5 rows of a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
print(df.tail())  # Display the last 5 rows
# Difference between loc[] and iloc[]:

# loc[] is label-based, so you use the actual labels of rows/columns.
# iloc[] is integer-location based, so you use numerical indices.
# Select a single column from a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
column_name = input("Enter the column name to select: ")
print(df[column_name])
# Select multiple columns from a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
columns = input("Enter the column names separated by commas: ").split(',')
print(df[columns])
# Filter rows based on a condition:

  
  
import pandas as pd

# Assuming df is already defined
condition = input("Enter the condition for filtering (e.g., 'ColumnName > 5'): ")
print(df.query(condition))
# Check for missing values in a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
print(df.isnull().sum())
# Fill missing values with a specific value:

  
  
import pandas as pd

# Assuming df is already defined
value = input("Enter the value to fill missing values: ")
df_filled = df.fillna(value)
print(df_filled)
# Remove rows with missing values:

  
  
import pandas as pd

# Assuming df is already defined
df_dropped_rows = df.dropna()
print(df_dropped_rows)
# Remove columns with missing values:

  
  
import pandas as pd

# Assuming df is already defined
df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols)
# Replace values in a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
to_replace = input("Enter the value to replace: ")
value = input("Enter the new value: ")
df_replaced = df.replace(to_replace, value)
print(df_replaced)
# Rename columns in a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
old_name = input("Enter the old column name: ")
new_name = input("Enter the new column name: ")
df_renamed = df.rename(columns={old_name: new_name})
print(df_renamed)
# Convert a column's data type:

  
  
import pandas as pd

# Assuming df is already defined
column_name = input("Enter the column name to convert: ")
new_type = input("Enter the new data type (e.g., 'int', 'float', 'str'): ")
df[column_name] = df[column_name].astype(new_type)
print(df)
# Drop duplicates in a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
df_dedup = df.drop_duplicates()
print(df_dedup)
# Reset the index of a DataFrame:

  
  
import pandas as pd

# Assuming df is already defined
df_reset = df.reset_index(drop=True)
print(df_reset)
# Change the index of a DataFrame to a specific column:

  
  
import pandas as pd

# Assuming df is already defined
column_name = input("Enter the column name to set as index: ")
df.set_index(column_name, inplace=True)
print(df)
# Sort a DataFrame by a specific column:

  
  
import pandas as pd

# Assuming df is already defined
column_name = input("Enter the column name to sort by: ")
df_sorted = df.sort_values(by=column_name)
print(df_sorted)
# Sort a DataFrame by multiple columns:

  
  
import pandas as pd

# Assuming df is already defined
columns = input("Enter column names to sort by, separated by commas: ").split(',')
df_sorted = df.sort_values(by=columns)
print(df_sorted)
