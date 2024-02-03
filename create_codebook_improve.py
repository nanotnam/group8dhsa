import csv
from jinja2 import Template

# Load the Jinja2 template from the file
with open('codebook_template.html', 'r') as file:
    template_str = file.read()

# Compile the template
template = Template(template_str)

# Load data from CSV files
with open('/Users/hoangnamvu/Documents/projects/election/survey_2021/var_info.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    v1 = list(reader)[1:]

with open('/Users/hoangnamvu/Documents/projects/election/survey_2021/ans_info.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    v2 = list(reader)[1:]

# Create data structure for Jinja2 rendering
data = []

for variable_sheet1 in v1:
    variable_data = {
        'variable_name': variable_sheet1[2],
        'label': variable_sheet1[3],
        'question': variable_sheet1[4],
        'wave': variable_sheet1[5],
        'year_survey': variable_sheet1[0],
        'responses': []
    }
    for variable_sheet2 in v2:
        if variable_sheet1[2] == variable_sheet2[1]:
            variable_data['responses'].append({
                'value': int(variable_sheet2[2]),
                'label': variable_sheet2[3],
                'wording': variable_sheet2[4]
            })
    data.append(variable_data)

# Render the template with the data
html_final = template.render(variables=data)

# Now, html_final contains the HTML code generated from your CSV data using the Jinja2 template
file_path = 'codebook2021.html'

# Open the file in write mode and write the HTML content
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_final)

print(f'HTML codebook has been exported to {file_path}')

import os
from pyhtml2pdf import converter

path = os.path.abspath('codebook2021.html')
converter.convert(f'file:///{path}', 'codebook2021.pdf')

print(f'PDF codebook has been exported')