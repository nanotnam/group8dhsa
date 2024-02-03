import pandas as pd

# Read Excel file into a pandas DataFrame
df = pd.read_csv('/Users/hoangnamvu/Documents/projects/data_web_sthsth/wave1_2023_long_final.csv')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', default_handler=str)

# Save JSON data to a file
json_output_path = '/Users/hoangnamvu/Documents/projects/data_web_sthsth/json_final/wave1_2023_long_final.json'
with open(json_output_path, 'w') as json_file:
    json_file.write(json_data)

print(f'Conversion complete. JSON data saved to {json_output_path}')