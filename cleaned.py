import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('cleaned_file.csv')

# Drop duplicate company names
df_unique = df.drop_duplicates(subset='Company Name')

# Save the cleaned DataFrame to a new CSV file
df_unique.to_csv('cleaned.csv', index=False)
