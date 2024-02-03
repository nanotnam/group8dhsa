import csv

# Define the CSV file path
csv_file = '/Users/hoangnamvu/Documents/projects/election/mvp/data/mvp_wave2_2023.csv'

# Define the SQL file path
sql_file = '/Users/hoangnamvu/Documents/projects/election/mvp/sql/mvp_wave2_2023.sql'


# Function to convert empty string to NULL
# Function to convert empty string to NULL
def empty_to_null(value):
    return "NULL" if value == "" else f"'{value}'"

# Open the CSV file for reading
with open(csv_file, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row if it exists

    # Open the SQL file for writing
    with open(sql_file, 'w') as sqlfile:
        # Write the first part of the SQL insert statement
        sqlfile.write("INSERT INTO dutch_election_survey.survey (id, year_survey, wave, var, val, val_string)\n")
        sqlfile.write("SELECT x.id, x.year_survey, x.wave, x.var, x.val, x.val_string FROM (\n")

        # Iterate over rows in the CSV file and write SQL insert statements
        for i, row in enumerate(csvreader):
            # Extract values from the CSV row
            id_value = row[0]
            year_survey = row[1]
            wave = row[2]
            var = row[3]
            val = empty_to_null(row[4])  # Convert empty strings to NULL
            val_string = empty_to_null(row[5])

            # Generate SQL insert statement
            sql_insert = f"SELECT {id_value}, {year_survey}, {wave}, '{var}', {val}, {val_string}"
            
            # Add UNION ALL if it's not the last row
            if i != 1389:  # Adjust this number based on the total rows in your CSV
                sql_insert += " UNION ALL\n"
            else:
                sql_insert += "\n"

            # Write the SQL insert statement to the SQL file
            sqlfile.write(sql_insert)

        # Write the closing part of the SQL insert statement
        sqlfile.write(") AS x (id,year_survey,wave,var,val,val_string);\n")