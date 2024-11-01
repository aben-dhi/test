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

# Function to fetch indication methods data
def fetch_indication_methods_data(molecule_id):
    api_url = f'https://api.blinkpharmacie.ma/api/v3/indecation-methods/{molecule_id}'
    retries = 0
    while True:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json().get('data', {})
            
            # Prepare a default result with None values
            result = {
                'molecule_id': molecule_id,
                'Indications': None,
                'Posologie': None,
                'Modalités_d_administration': None
            }
            
            # Extract relevant fields, defaulting to None
            result['Indications'] = data.get('Indications', None)
            result['Posologie'] = data.get('Posologie', None)
            result['Modalités_d_administration'] = data.get('Modalités d\'administration du traitement', None)

            return result
            
        elif response.status_code == 429:
            wait_time = exponential_backoff(retries)
            print(f"Rate limit exceeded for {molecule_id}. Waiting for {wait_time:.2f} seconds...")
            time.sleep(wait_time)
            retries += 1
        else:
            print(f"Error fetching data for {molecule_id}: {response.status_code}, Response: {response.json()}")
            return result

# Initialize an empty list to hold the extracted data
extracted_data = []

# Process identifiers one by one with a small batch wait
for index, identifier in enumerate(df['Identifier']):
    molecule_id = identifier.split('/')[-1]  # Adjust if the identifier format is different
    print(f"Processing molecule {index + 1}/{len(df)}: {molecule_id}")
    
    # Fetch indication methods data
    indication_result = fetch_indication_methods_data(molecule_id)
    extracted_data.append(indication_result)  # Append indication data
    
    time.sleep(2)  # Adjust based on how the API responds

# Convert the extracted data to a DataFrame
output_df = pd.DataFrame(extracted_data)

# Save the DataFrame to an Excel file
output_df.to_excel('indication_methods_data.xlsx', index=False)

print("Data extraction complete. Saved to 'indication_methods_data.xlsx'.")
