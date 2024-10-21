import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = 'https://public.euro-pharmat.com/glossaire-produits.aspx'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Find the table and extract the rows
    # Adjust the 'table' tag if needed, e.g., using 'class_' or 'id' if the table has a specific identifier
    table = soup.find('table')  # You might need to specify {'class': 'your-table-class'} if there's a class name
    
    # Prepare a list to store the rows
    data = []

    # Step 4: Loop through each row in the table
    for row in table.find_all('tr'):
        # Get the content of the entire <tr> as text
        tr_content = row.text.strip()

        # Extract each <td> element's text
        td_contents = [td.text.strip() for td in row.find_all('td')]

        # Store the full <tr> content in one column and the list of <td> contents in another
        data.append([tr_content, ', '.join(td_contents)])  # Combine <td> contents into a single string for the column

    # Step 5: Create a DataFrame with columns 'Row Content' and 'Cell Contents'
    df = pd.DataFrame(data, columns=['Row Content', 'Cell Contents'])
    
    # Step 6: Write the DataFrame to an Excel file
    df.to_excel('glossary_products.xlsx', index=False)
    print("Data has been written to glossary_products.xlsx")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
