import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/hoangnamvu/Documents/projects/election/survey_2021/wave4_2021_long.csv')

# Create a new column 'val_string' to store non-numeric string values
df['val_string'] = ''
df['test'] = ''

# Iterate through each row
for index, row in df.iterrows():
    # Check if the value in 'val' column is a string
    if isinstance(row['val'], str):
        # Try to convert the string value to a numeric value
        try:
            numeric_val = float(row['val'])  # Use float for both int and float values
            # If conversion is successful, keep the value in 'val' column
            df.at[index, 'val'] = numeric_val
        except ValueError:
            # If conversion fails, move the string value to 'val_string' column
            df.at[index, 'val_string'] = row['val']
            # Set the 'val' column to None for non-numeric strings
            df.at[index, 'val'] = None

# Save the modified DataFrame back to CSV
df.to_csv('/Users/hoangnamvu/Documents/projects/election/survey_2021/wave4_2021_long_final.csv', index=False)