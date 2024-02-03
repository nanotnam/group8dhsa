import pandas as pd

# Read the CSV file into a DataFrame
wide_data = pd.read_csv('/Users/hoangnamvu/Documents/projects/election/survey_2021/wave4_2021_wide.csv')

# Define columns to keep as identifier variables
id_vars = ['id','year_survey','wave']

# Use melt to convert wide to long format
long_data = pd.melt(wide_data, id_vars=id_vars, var_name='var', value_name='val')

# Export the long format DataFrame to a CSV file
long_data.to_csv('/Users/hoangnamvu/Documents/projects/election/survey_2021/wave4_2021_long.csv', index=False)