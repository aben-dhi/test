import pandas as pd
import requests
import time

# Read the Excel file
file_path = 'medicine_identifiers.xlsx'
df = pd.read_excel(file_path)

# Print the column names to verify
print(df.columns)

# Exponential backoff function
def exponential_backoff(retries):
    return min(60, 2 ** retries)  # Cap the maximum wait time to 60 seconds

# Function to fetch active molecule data
def fetch_active_molecule_data(identifier):
    api_url = f'https://api.blinkpharmacie.ma/api/v3/active_molecules/{identifier}'
    retries = 0
    while True:
        response = requests.get(api_url)
        if response.status_code == 200:
            try:
                data = response.json().get('data', {}).get('molecules', [])
                
                # Prepare a default result with None values
                result = {
                    'Identifier': identifier,
                    'Name': None,
                    'Title': None,
                    'IUPAC': None,
                    'Synonyms': None,
                    'Defined Daily Dose': None
                }
                
                if data:
                    # Assuming we're interested in the first molecule if multiple exist
                    molecule = data[0]
                    result['Name'] = molecule.get('name')
                    result['Title'] = molecule.get('title')
                    result['IUPAC'] = molecule.get('iupac')
                    result['Synonyms'] = molecule.get('synonyms')
                    result['Defined Daily Dose'] = molecule.get('defined_daily_dose')

                return result
                
            except ValueError:
                print(f"Error decoding JSON for {identifier}: Response content is not valid JSON.")
                return {'Identifier': identifier, 'error': 'Invalid JSON'}
            
        elif response.status_code == 429:
            wait_time = exponential_backoff(retries)
            print(f"Rate limit exceeded for {identifier}. Waiting for {wait_time:.2f} seconds...")
            time.sleep(wait_time)
            retries += 1
        else:
            print(f"Error fetching data for {identifier}: {response.status_code}, Response: {response.text}")
            return {'Identifier': identifier, 'error': response.status_code}

# Initialize an empty list to hold the extracted data
extracted_data = []

# Process identifiers one by one with a small batch wait
for index, identifier in enumerate(df['Identifier']):
    print(f"Processing molecule {index + 1}/{len(df)}: {identifier}")
    
    # Fetch active molecule data
    molecule_result = fetch_active_molecule_data(identifier)
    extracted_data.append(molecule_result)  # Append molecule data
    
    time.sleep(2)  # Adjust based on how the API responds

# Convert the extracted data to a DataFrame
output_df = pd.DataFrame(extracted_data)

# Save the DataFrame to an Excel file
output_df.to_excel('active_molecule_data.xlsx', index=False)

print("Data extraction complete. Saved to 'active_molecule_data.xlsx'.")
