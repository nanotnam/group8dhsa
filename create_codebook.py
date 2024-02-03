import xlwings as xw

# Specifying a sheet
ws1 = xw.Book("data/codebook_23.xlsx").sheets['Sheet1']
ws2 = xw.Book("data/codebook_23.xlsx").sheets['Sheet2']

# select all data in Sheet1 
v1 = ws1.range("A2:D58").value

# select all data in Sheet2
v2 = ws2.range("A2:D578").value


# create the heading for the codebook
html1 = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Code Book</title>
  <style>
    body {
        height: 842px;
        width: 595px;
        /* to centre page on screen*/
        margin-left: auto;
        margin-right: auto;
    }

    </style>
</head>
<body>
    <h1>Code Book</h1>
    <br>
"""

# variables information part of the tables
html2 = """\
  <table bgcolor="black" width="595px" class="center">
    <tr bgcolor="white">
        <th width="119px">Variable:</th>
        <td colspan="2">{variable_name}</td>
    </tr>
    <tr bgcolor="white">
        <th>Label:</th>
        <td colspan="2">{label1}</td>
    </tr>
    <tr bgcolor="white">
        <th>Question:</th>
        <td colspan="2">{question}</td>
    </tr>
    <tr bgcolor="white">
        <th>Wave:</th>
        <td colspan="2">{wave}</td>
    </tr>
    <tr bgcolor="white">
        <th>Value</th>
        <th width="238px">Label</th>
        <th width="238px">Wording</th>
    </tr>
    
"""

# responses part of the tables
html3 = """\
<tr align="center" bgcolor="white">
        <td>{value}</td>
        <td>{label}</td>
        <td>{wording}</td>
    </tr>

"""

# end the tables
html4 = """\
  </table>
  <br>
  <br>
  """

# end the codebook
html5 = """\
    </body>
</html>
"""


html_final = html1
for i in v1:
    html_final+=html2.format(variable_name = i[0], label1 = i[1], question = i[2], wave = str(i[3]))
    for j in v2:
        if i[0] == j[0]:
            html_final+=html3.format(value = int(j[1]), label =j[2], wording = j[3])
    html_final+=html4
html_final+=html5

file_path = 'codebook.html'

# Open the file in write mode and write the HTML content
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_final)

print(f'HTML codebook has been exported to {file_path}')

import os
from pyhtml2pdf import converter

path = os.path.abspath('codebook.html')
converter.convert(f'file:///{path}', 'codebook.pdf')

print(f'PDF codebook has been exported')