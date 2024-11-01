import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL setup
base_url = 'https://www.medindex.ma/browse-medicines/{}?per_page=50&page={}'

# Define the letters A-Z
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Empty list to store all medicines' information
all_data = []

# Loop through each letter
for letter in letters:
    page = 1  # Start at page 1 for each letter
    
    while True:
        # Construct the URL for the current letter and page
        url = base_url.format(letter, page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
            break
        
        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all product <a> tags
        products = soup.find_all('a', href=True)  # Search for all <a> tags
        
        if not products:
            print(f"No products found on page {page} for letter {letter}. Ending pagination for this letter.")
            break
        
        current_count = len(all_data)  # Count before adding new products
        
        # Extract medicine name and identifier from each product
        for product in products:
            # Find the <p> tag within the <a> tag to get the medicine name
            name_tag = product.find('p', class_='text-med-blue hover:text-[#142B61] font-bold text-base cursor-pointer')
            if name_tag:  # Check if the <p> tag exists
                name = name_tag.text.strip()  # Extract the name from the <p> tag
                identifier = product['href']  # Get the href URL as the identifier

                # Add data to our list
                all_data.append({
                    "Name": name,
                    "Identifier": identifier
                })
        
        print(f"Data scraped from letter '{letter}', page {page}. Found {len(all_data)} products so far.")

        # Check if the count has changed; if not, break the loop
        if len(all_data) == current_count:
            print(f"No new products found on page {page}. Ending pagination for letter '{letter}'.")
            break

        page += 1  # Go to the next page

        # Be polite to the server
        time.sleep(1)

# Save data to a DataFrame and export to Excel
df = pd.DataFrame(all_data)
df.to_excel('medicine_identifiers.xlsx', index=False)
print("Data collection complete. Saved to 'medicine_identifiers.xlsx'.")
print(f"Total products scraped: {len(all_data)}")
