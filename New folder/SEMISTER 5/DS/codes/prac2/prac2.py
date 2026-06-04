import pandas as pd

csv_file_path = 'DATA SET.csv'
json_file_path = 'ds.json'

df_csv = pd.read_csv(csv_file_path)

df_json = pd.read_json(json_file_path)

print("CSV Data:")
print(df_csv.head())

print("\nJSON Data:")
print(df_json.head())

df_csv_cleaned = df_csv.dropna()
df_json_filled = df_json.fillna(0)

print("\nCleaned CSV Data:")
print(df_csv_cleaned)

print("\nFilled JSON Data:")
print(df_json_filled)

median_value = df_csv['Sales'].median()
mean = df_csv['Sales'].mean()
std = df_csv['Sales'].std()
upper = mean + 2 * std
lower = mean - 2 * std

df_csv['Sales'] = df_csv['Sales'].apply(lambda x: median_value if x > upper or x < lower else x)

filtered_data = df_csv[df_csv['Sales'] > 10]

sorted_data = df_csv.sort_values(by='Sales', ascending=False)

numeric_columns = ['Sales', 'Cost', 'Profit']
grouped_data = df_csv.groupby('Category')[numeric_columns].mean()

print("\nFiltered Data:")
print(filtered_data)

print("\nSorted Data:")
print(sorted_data)

print("\nGrouped Data:")
print(grouped_data)
