import csv

def csv_to_sql(csv_file, sql_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        sql_values = []
        for row in reader:
            sql_values.append("(" + ",".join(['null' if cell.strip() == '' else f'"{cell.strip()}"' for cell in row]) + ")")

    sql_statement = f"INSERT INTO dutch_election_survey.survey select id, year_survey, wave, var, val, val_string from ( values {','.join(sql_values)}) x (id, year_survey, wave, var, val, val_string, test);"
    
    with open(sql_file, 'w') as sql_output:
        sql_output.write(sql_statement)

# Replace 'input.csv' and 'output.sql' with the paths to your CSV file and SQL output file
csv_to_sql('/Users/hoangnamvu/Documents/projects/election/survey_2023/final/wave1_2023_long_final.csv', '/Users/hoangnamvu/Documents/projects/election/survey_2023/sql/wave1_2023_long_final.sql')