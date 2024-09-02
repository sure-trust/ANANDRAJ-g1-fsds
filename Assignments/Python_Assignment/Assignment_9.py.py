import pandas as pd
import numpy as np
# 1.  Data Loading:
df = pd.read_csv('./Mobiles_Dataset.csv')
# 2. Data Inspection:
# print(df.head(5))

# 3. Column Information:
# print(df.info())
# 4. Missing Values:
# print(df.isnull().sum())
# 5. Data Cleaning:

df['Actual price'] = df['Actual price'].replace('NIL', np.nan)
# print(df.head(5))
# # 6. Data Conversion:

df['Actual price'] = df['Actual price'].str.replace('₹', '').str.replace(',', '').str.strip().replace('', np.nan).astype(float)
df['Discount price'] = df['Discount price'].str.replace('₹', '').str.replace(',', '').str.strip().replace('', np.nan).astype(float)

# print(df.head())   
# # 7. Filtering Data: How do you filter the DataFrame to show only the rows where the 
# 'Stars' rating is greater than 4.0?
filtered_df = df[df['Stars'] > 4.0]
# print(filtered_df)
# # 8. Sorting Data: How can you sort the DataFrame by 'Discount price' in ascending 
# order?
sorted_df = df.sort_values(by='Discount price', ascending=True)
# print(sorted_df)
# 9. Grouping Data: How do you group the DataFrame by 'RAM (GB)' and calculate the 
# average 'Discount price' for each group?
grouped_df = df.groupby('RAM (GB)')['Discount price'].mean()
# print(grouped_df)
# 10. Aggregation: How can you find the total number of reviews for each unique 'Product 
#Name'?
total_reviews = df.groupby('Product Name')['Reviews'].sum()
# print(total_reviews)
#  11. String Operations: How do you extract the numeric part of the 'Rating' column and 
# convert it to an integer?
numeric_rating = df['Rating'] = df['Rating'].str.extract(r'(\d+)').astype(int)


# print(numeric_rating)
#  12. Data Merging:  If you have another DataFrame with additional mobile specifications, 
# how can you merge it with the current DataFrame on 'Product Name'?
# merged_df = pd.merge(df, other_df, on='Product Name')
# print(merged_df)
#  13. Data Visualization: How can you create a bar plot showing the average 'Stars' 
# rating for each 'RAM (GB)' category?
import matplotlib.pyplot as plt
df.groupby('RAM (GB)')['Rating'].mean().plot(kind='bar')
plt.xlabel('RAM (GB)')
plt.ylabel('Average Stars')
plt.title('Average Stars Rating by RAM (GB)')
# plt.show()

# 14. Conditional Selection: How do you select rows where the 'Storage (GB)' is greater 
# than 128 GB and the 'Stars' rating is above 4.0?
df['Storage (GB)'] = pd.to_numeric(df['Storage (GB)'].replace('NIL', pd.NA), errors='coerce')
df['Stars'] = pd.to_numeric(df['Stars'].replace('NIL', pd.NA), errors='coerce')
filtered_df = df[(df['Storage (GB)'].replace('NIL', pd.NA) > 128) & (df['Stars'] > 4.0)]
# print(filtered_df)

#  15. Removing Duplicates: How can you remove duplicate rows based on the 'Product 
# Name' column?
df_cleaned = df.drop_duplicates(subset='Product Name')
# print(df_cleaned)

# 16. Data Export: How do you export the cleaned DataFrame to a new CSV file?
# df_cleaned.to_csv('cleaned_data.csv', index=False)

#  17. Handling Outliers: How can you identify and handle outliers in the 'Discount price' 
# column?
# Calculate IQR
Q1 = df['Discount price'].quantile(0.25)
Q3 = df['Discount price'].quantile(0.75)
IQR = Q3 - Q1

# Define outliers
outliers = (df['Discount price'] < (Q1 - 1.5 * IQR)) | (df['Discount price'] > (Q3 + 1.5 * IQR))

# Handle outliers by removing them
df_no_outliers = df[~outliers]

# Print DataFrame without outliers
# print(df_no_outliers)

# 18. Pivot Table: How do you create a pivot table that shows the average 'Discount price' 
# for each combination of 'RAM (GB)' and 'Storage (GB)'?
pivot_table = df.pivot_table(values='Discount price', index='RAM (GB)', columns='Storage (GB)', aggfunc='mean')
# print(pivot_table)

# 19. Data Imputation: How can you fill missing values in the 'Stars' column with the 
# mean value of the column?
mean_stars = df['Stars'].mean()
df['Stars'].fillna(mean_stars)
# print(df)

#  20. Custom Functions: How do you apply a custom function to create a new column 
# that categorizes mobiles into 'High-end', 'Mid-range', and 'Budget' based on their 
# 'Discount price'?
def categorize_discount_price(discount_price):
    if discount_price > 20000:
        return 'High-end'
    elif discount_price > 10000:
        return 'Mid-range'
    else:
        return 'Budget'

df['Category'] = df['Discount price'].apply(categorize_discount_price)

# Print DataFrame with new category column
print(df)


   