import csv

def csv_to_sql(csv_file, sql_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        sql_values = []
        for row in reader:
            formatted_row = []
            for cell in row:
                # Check if the cell is empty or not
                if cell.strip() == '':
                    formatted_row.append('null')
                else:
                    # Check if the cell is numeric
                    if cell.strip().isdigit():
                        formatted_row.append(cell.strip())  # If numeric, keep as is
                    else:
                        formatted_row.append(f'"{cell.strip()}"')  # If not numeric, wrap in quotes
            sql_values.append("(" + ",".join(formatted_row) + ")")

    sql_statement = f"INSERT INTO dutch_election_survey.survey select id, year_survey, wave, var, val, val_string from ( values {','.join(sql_values)}) x (id, year_survey, wave, var, val, val_string, test);"
    
    with open(sql_file, 'w') as sql_output:
        sql_output.write(sql_statement)

# Replace 'input.csv' and 'output.sql' with the paths to your CSV file and SQL output file
csv_to_sql('/Users/hoangnamvu/Documents/projects/election/survey_2023/final/wave1_2023_long_final.csv', '/Users/hoangnamvu/Documents/projects/election/survey_2023/sql/wave1_2023_long_final.sql')
