# import pandas as pd
# import requests
# import time

# # Read the Excel file
# file_path = 'medicine_identifiers.xlsx'
# df = pd.read_excel(file_path)

# # Print the column names to verify
# print(df.columns)

# # Exponential backoff function
# def exponential_backoff(retries):
#     return min(60, 2 ** retries)  # Cap the maximum wait time to 60 seconds

# # Function to fetch data for a single product ID
# def fetch_product_data(product_id):
#     api_url = f'https://api.blinkpharmacie.ma/api/v3/product_synthesis/{product_id}'
#     retries = 0
#     while True:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json().get('data', {})
#             return {
#                 'id': data.get('id'),
#                 'name': data.get('name'),
#                 'fullname': data['synthesis'][0].get('fullname') if data.get('synthesis') else None,
#                 'breastfeeding_risk': data['synthesis'][0].get('breastfeeding_risk') if data.get('synthesis') else None,
#                 'vigilance_level': data['synthesis'][0].get('vigilance_level') if data.get('synthesis') else None,
#                 'pregnancy_risk': data['synthesis'][0].get('pregnancy_risk') if data.get('synthesis') else None,
#             }
#         elif response.status_code == 429:
#             wait_time = exponential_backoff(retries)
#             print(f"Rate limit exceeded for {product_id}. Waiting for {wait_time:.2f} seconds...")
#             time.sleep(wait_time)
#             retries += 1  # Increment retries
#         else:
#             print(f"Error fetching data for {product_id}: {response.status_code}")
#             return None

# # Initialize an empty list to hold the extracted data
# extracted_data = []

# # Process identifiers one by one with a small batch wait
# for index, identifier in enumerate(df['Identifier']):
#     product_id = identifier.split('/')[-1]
#     print(f"Processing {index + 1}/{len(df)}: {product_id}")
#     result = fetch_product_data(product_id)
#     if result:
#         extracted_data.append(result)
#     # Wait a bit between requests to manage rate limits
#     time.sleep(2)  # Adjust based on how the API responds

# # Convert the extracted data to a DataFrame
# output_df = pd.DataFrame(extracted_data)

# # Save the DataFrame to an Excel file
# output_df.to_excel('extracted_data.xlsx', index=False)

# print("Data extraction complete. Saved to 'extracted_data.xlsx'.")
# import pandas as pd
# import requests
# import time

# # Read the Excel file
# file_path = 'medicine_identifiers.xlsx'
# df = pd.read_excel(file_path)

# # Print the column names to verify
# print(df.columns)

# # Exponential backoff function
# def exponential_backoff(retries):
#     return min(60, 2 ** retries)  # Cap the maximum wait time to 60 seconds

# # Function to fetch data for a single product ID
# def fetch_product_data(product_id):
#     api_url = f'https://api.blinkpharmacie.ma/api/v3/product_synthesis/{product_id}'
#     retries = 0
#     while True:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json().get('data', None)  # Get 'data' and default to None
#             if data is None:  # Check if data is None
#                 print(f"No data found for {product_id}. Response: {response.json()}")
#                 return None
            
#             # Extracting data with nested structures
#             synthesis = data.get('synthesis', None)  # Get synthesis entries
            
#             if synthesis is None:  # Check if synthesis is None
#                 print(f"No synthesis data found for {product_id}. Skipping...")
#                 return None
            
#             # If synthesis is not None, we can safely extract the values
#             # In this case, synthesis will always have data due to the structure
#             if len(synthesis) == 0:
#                 print(f"No synthesis entries found for {product_id}.")
#                 return None
            
#             # If we reach here, synthesis is a list and we can access its first element
#             synthesis = synthesis[0]  # Get the first synthesis entry
#             pregnancy_risk = synthesis.get('pregnancy_risk', [{}])[0]  # Get the first pregnancy risk entry
#             molecule_atc = synthesis.get('molecule_atc', [{}])  # Get all molecule ATC entries
            
#             return {
#                 'id': data.get('id'),
#                 'name': data.get('name'),
#                 'fullname': synthesis.get('fullname'),
#                 'breastfeeding_risk': synthesis.get('breastfeeding_risk'),
#                 'vigilance_level': synthesis.get('vigilance_level'),
#                 'pregnancy_risk_months': pregnancy_risk.get('months'),
#                 'pregnancy_risk_value': pregnancy_risk.get('value'),
#                 'pregnancy_risk_order': pregnancy_risk.get('order'),
#                 'pregnancy_risk_security_level': pregnancy_risk.get('security_level'),
#                 'molecule_atc': [{'atc_code': m.get('atc_code'), 'name': m.get('name')} for m in molecule_atc]  # List of ATC codes and names
#             }
#         elif response.status_code == 429:
#             wait_time = exponential_backoff(retries)
#             print(f"Rate limit exceeded for {product_id}. Waiting for {wait_time:.2f} seconds...")
#             time.sleep(wait_time)
#             retries += 1  # Increment retries
#         else:
#             print(f"Error fetching data for {product_id}: {response.status_code}, Response: {response.json()}")
#             return None

# # Initialize an empty list to hold the extracted data
# extracted_data = []

# # Process identifiers one by one with a small batch wait
# for index, identifier in enumerate(df['Identifier']):
#     product_id = identifier.split('/')[-1]
#     print(f"Processing {index + 1}/{len(df)}: {product_id}")
#     result = fetch_product_data(product_id)
#     if result:
#         extracted_data.append(result)
#     # Wait a bit between requests to manage rate limits
#     time.sleep(2)  # Adjust based on how the API responds

# # Convert the extracted data to a DataFrame
# output_df = pd.DataFrame(extracted_data)

# # Save the DataFrame to an Excel file
# output_df.to_excel('extracted_data.xlsx', index=False)

# print("Data extraction complete. Saved to 'extracted_data.xlsx'.")

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

# Function to fetch data for a single product ID
def fetch_product_data(product_id):
    api_url = f'https://api.blinkpharmacie.ma/api/v3/product_synthesis/{product_id}'
    retries = 0
    while True:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json().get('data', None)  # Get 'data' and default to None
            
            # Prepare a default result with None values
            result = {
                'id': product_id,  # Store the product ID even if data is None
                'name': None,
                'fullname': None,
                'breastfeeding_risk': None,
                'vigilance_level': None,
                'pregnancy_risk_months': None,
                'pregnancy_risk_value': None,
                'pregnancy_risk_order': None,
                'pregnancy_risk_security_level': None,
                'molecule_atc': []
            }
            
            if data is not None:  # Proceed only if data is present
                result['name'] = data.get('name')
                
                synthesis = data.get('synthesis', None)  # Get synthesis entries
                
                if synthesis is not None and len(synthesis) > 0:  # Check if synthesis is available
                    synthesis = synthesis[0]  # Get the first synthesis entry
                    result['fullname'] = synthesis.get('fullname')
                    result['breastfeeding_risk'] = synthesis.get('breastfeeding_risk')
                    result['vigilance_level'] = synthesis.get('vigilance_level')
                    pregnancy_risk = synthesis.get('pregnancy_risk', [{}])[0]  # Get first pregnancy risk entry
                    result['pregnancy_risk_months'] = pregnancy_risk.get('months')
                    result['pregnancy_risk_value'] = pregnancy_risk.get('value')
                    result['pregnancy_risk_order'] = pregnancy_risk.get('order')
                    result['pregnancy_risk_security_level'] = pregnancy_risk.get('security_level')
                    result['molecule_atc'] = [{'atc_code': m.get('atc_code'), 'name': m.get('name')} for m in synthesis.get('molecule_atc', [])]

            return result  # Always return a result with None values where applicable
            
        elif response.status_code == 429:
            wait_time = exponential_backoff(retries)
            print(f"Rate limit exceeded for {product_id}. Waiting for {wait_time:.2f} seconds...")
            time.sleep(wait_time)
            retries += 1  # Increment retries
        else:
            print(f"Error fetching data for {product_id}: {response.status_code}, Response: {response.json()}")
            return result  # Return the result with None values for this case

# Initialize an empty list to hold the extracted data
extracted_data = []

# Process identifiers one by one with a small batch wait
for index, identifier in enumerate(df['Identifier']):
    product_id = identifier.split('/')[-1]
    print(f"Processing {index + 1}/{len(df)}: {product_id}")
    result = fetch_product_data(product_id)
    extracted_data.append(result)  # Always append the result, even if it's all None
    # Wait a bit between requests to manage rate limits
    time.sleep(1)  # Adjust based on how the API responds

# Convert the extracted data to a DataFrame
output_df = pd.DataFrame(extracted_data)

# Save the DataFrame to an Excel file
output_df.to_excel('extracted_data.xlsx', index=False)

print("Data extraction complete. Saved to 'extracted_data.xlsx'.")
