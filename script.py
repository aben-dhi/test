# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Step 1: Send a request to the website with a User-Agent header
# url = 'https://public.euro-pharmat.com/glossaire-produits.aspx'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Step 2: Parse the HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Step 3: Find the table and extract the rows
#     table = soup.find('table')  # Adjust this if necessary
    
#     # Prepare a list to store the rows
#     data = []

#     # Step 4: Loop through each row in the table
#     for row in table.find_all('tr'):
#         # Get the content of the entire <tr> as text
#         tr_content = row.text.strip()
        
#         # Extract each <td> element's text
#         td_contents = [td.text.strip() for td in row.find_all('td')]
        
#         # Store the full <tr> content in one column and the list of <td> contents in another
#         data.append([tr_content, ', '.join(td_contents)])

#     # Step 5: Create a DataFrame with columns 'Row Content' and 'Cell Contents'
#     df = pd.DataFrame(data, columns=['Row Content', 'Cell Contents'])
    
#     # Step 6: Write the DataFrame to an Excel file
#     df.to_excel('glossary_products.xlsx', index=False)
#     print("Data has been written to glossary_products.xlsx")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")
#     print(response.text)  # Print response content for debugging
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Base URL with placeholder for the initial character
# base_url = 'https://public.euro-pharmat.com/glossaire-produits.aspx?ini={}'

# # Allowed starting characters
# allowed_chars = ['0', '2', '3', '7', 'A', 'B', 'C', 'D', 'E', 'É', 'F', 
#                  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
#                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# # Prepare a list to store the rows from all pages
# all_data = []

# # Iterate through each character in the allowed_chars
# for char in allowed_chars:
#     # Construct the full URL for the current character
#     url = base_url.format(char)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }
    
#     # Step 1: Send a request to the website
#     print(f"Requesting URL: {url}")  # Debugging line
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Step 2: Parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Step 3: Find the table and extract the rows
#         table = soup.find('table')  # Adjust this if necessary
        
#         if table:  # Check if the table exists
#             row_count = 0  # Initialize a counter for the number of rows
#             # Step 4: Loop through each row in the table
#             for row in table.find_all('tr'):
#                 # Skip header rows by checking if they contain <th> elements
#                 if row.find('th'):
#                     # Extract the product name from the <th>
#                     product_name = row.find('th').get_text(strip=True)
#                 else:
#                     continue
                
#                 # Extract additional info from <td>
#                 td_contents = row.find('td')
#                 if td_contents:
#                     # Extract the text from <h2> and <p> tags
#                     comm_and_frn = td_contents.find('h2').get_text(strip=True) if td_contents.find('h2') else ''
#                     description = td_contents.find('p').get_text(strip=True) if td_contents.find('p') else ''
                    
#                     # Only append if there's valid content
#                     if product_name and comm_and_frn:
#                         all_data.append([product_name, comm_and_frn, description])  # Add the row to the data
#                         row_count += 1  # Increment the counter
            
#             print(f"Data scraped from page starting with '{char}': {row_count} rows")
#         else:
#             print(f"No table found on the page starting with '{char}'.")
#     else:
#         print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

#     # Optional: Sleep for a second to avoid rate limiting
#     time.sleep(1)

# # Step 5: Check if any data was collected before proceeding
# if all_data:
#     # Step 6: Create a DataFrame with columns for each extracted column
#     df = pd.DataFrame(all_data, columns=['Product Name', 'Comm et Frn', 'Description'])

#     # Step 7: Write the DataFrame to an Excel file
#     df.to_excel('glossary_products_all.xlsx', index=False)
#     print("All data has been written to glossary_products_all.xlsx")
# else:
#     print("No data was scraped from any of the pages.")

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Base URL with placeholder for the initial character
# base_url = 'https://public.euro-pharmat.com/glossaire-produits.aspx?ini={}'

# # Allowed starting characters
# allowed_chars = ['0', '2', '3', '7', 'A', 'B', 'C', 'D', 'E', 'É', 'F', 
#                  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
#                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# # Prepare a list to store the rows from all pages
# all_data = []

# # Iterate through each character in the allowed_chars
# for char in allowed_chars:
#     # Construct the full URL for the current character
#     url = base_url.format(char)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }
    
#     # Step 1: Send a request to the website
#     print(f"Requesting URL: {url}")  # Debugging line
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Step 2: Parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Step 3: Find the table and extract the rows
#         table = soup.find('table')  # Adjust this if necessary
        
#         if table:  # Check if the table exists
#             row_count = 0  # Initialize a counter for the number of rows
#             # Step 4: Loop through each row in the table
#             for row in table.find_all('tr'):
#                 # Skip header rows by checking if they contain <th> elements
#                 if row.find('th'):
#                     # Extract the product name from the <th>
#                     product_name = row.find('th').get_text(strip=True)
#                 else:
#                     continue
                
#                 # Extract additional info from <td>
#                 td_contents = row.find('td')
#                 if td_contents:
#                     # Extract the text from <h2> and <p> tags
#                     comm_and_frn = td_contents.find('h2').get_text(strip=True) if td_contents.find('h2') else ''
#                     description = td_contents.find('p').get_text(strip=True) if td_contents.find('p') else ''
                    
#                     # Combine comm_and_frn and description into one column
#                     combined_info = f"{comm_and_frn} - {description}" if comm_and_frn and description else comm_and_frn or description
                    
#                     # Only append if there's valid content
#                     if product_name and combined_info:
#                         all_data.append([product_name, combined_info])  # Add the row to the data
#                         row_count += 1  # Increment the counter
            
#             print(f"Data scraped from page starting with '{char}': {row_count} rows")
#         else:
#             print(f"No table found on the page starting with '{char}'.")
#     else:
#         print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

#     # Optional: Sleep for a second to avoid rate limiting
#     time.sleep(1)

# # Step 5: Check if any data was collected before proceeding
# if all_data:
#     # Step 6: Create a DataFrame with columns for each extracted column
#     df = pd.DataFrame(all_data, columns=['Product Name', 'Combined Info'])

#     # Step 7: Write the DataFrame to an Excel file
#     df.to_excel('glossary_products_all.xlsx', index=False)
#     print("All data has been written to glossary_products_all.xlsx")
# else:
#     print("No data was scraped from any of the pages.")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL with placeholder for the initial character
base_url = 'https://public.euro-pharmat.com/ficheevaluationsclinique.aspx?ini={}'

# Allowed starting characters
allowed_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'V']

# Prepare a list to store the rows from all pages
all_data_single_column = []

# Iterate through each character in the allowed_chars
for char in allowed_chars:
    # Construct the full URL for the current character
    url = base_url.format(char)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # Step 1: Send a request to the website
    print(f"Requesting URL: {url}")  # Debugging line
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Step 2: Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Step 3: Find the spans containing the data
        spans = soup.find_all('span', id=lambda x: x and x.startswith('ctl00_Contentplaceholder1_rptDenos_ctl'))
        
        # Step 4: Extract text from each span and add it to the list
        for span in spans:
            span_text = span.get_text(strip=True)
            if span_text:  # Check if the span has valid text
                all_data_single_column.append([span_text])  # Append as a list for DataFrame format
        
        print(f"Data scraped from page starting with '{char}': {len(spans)} rows")
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

    # Optional: Sleep for a second to avoid rate limiting
    time.sleep(1)

# Step 5: Check if any data was collected before proceeding
if all_data_single_column:
    # Step 6: Create a DataFrame with a single column
    df_single_column = pd.DataFrame(all_data_single_column, columns=['Product Name'])

    # Step 7: Write the DataFrame to an Excel file
    df_single_column.to_excel('glossary_products_single_column.xlsx', index=False)
    print("All data has been written to glossary_products_single_column.xlsx")
else:
    print("No data was scraped from any of the pages.")
