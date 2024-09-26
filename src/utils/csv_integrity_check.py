import csv

def check_csv_integrity(file_path, expected_delimiter=','):
    """
    Check the integrity of a CSV file.

    :param file_path: Path to the CSV file
    :param expected_delimiter: The delimiter expected in the CSV file (default is ',')
    :return: A report on any issues found
    """
    issues = []
    
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=expected_delimiter)
            header = next(reader, None)
            
            if not header:
                issues.append("Header is missing.")
                return issues 

            num_columns = len(header)
            
            for line_number, row in enumerate(reader, start=2):  # Start at 2 to account for header line
                if not row:  # Skip empty lines
                    continue
                
                if len(row) != num_columns:
                    issues.append(f"Line {line_number}: Expected {num_columns} columns, found {len(row)} columns.")
                
                if any(expected_delimiter not in line for line in row):
                    issues.append(f"Line {line_number}: Delimiter '{expected_delimiter}' not found or inconsistent.")

    except Exception as e:
        issues.append(f"Error reading file: {e}")

    if not issues:
        return "CSV file integrity check passed."
    else:
        return issues

# Usage example:
file_path = '/Users/hans/Desktop/airportPipeline/car_prices.csv'
report = check_csv_integrity(file_path)

if isinstance(report, list):
    for issue in report:
        print(issue)
else:
    print(report)


