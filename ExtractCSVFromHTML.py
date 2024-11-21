from bs4 import BeautifulSoup
import csv


def html_table_to_csv(input_html_file, output_csv_file):
    # Read the HTML content from the file
    with open(input_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table
    table = soup.find('table')

    if not table:
        print("No table found in the HTML content.")
        return

    # Open the CSV file for writing
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Process table rows
        for row in table.find_all('tr'):
            # Extract cells (either <td> or <th>)
            cells = row.find_all(['td', 'th'])
            # Write the row to CSV
            writer.writerow([cell.get_text(strip=True) for cell in cells])

    print(f"CSV file '{output_csv_file}' has been created successfully.")


# Specify the files HTML file and output CSV file
input_html_file = 'model_performance_html_list'  # Replace with your HTML file
output_csv_file = 'output.csv'  # The CSV file to generate

# Call the function to convert the HTML table to CSV
html_table_to_csv(input_html_file, output_csv_file)
