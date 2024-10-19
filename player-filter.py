import csv
import json

# Open the CSV file
with open('Raw-Data-20242025\players.csv', mode='r', encoding='utf-8') as file:
    # Create a DictReader object
    playersfile = csv.DictReader(file)

    # Loop over each row in the CSV
    # Filter out rows where 'last_season' is not equal to 2024
    new_rows = [row for row in playersfile if row['last_season'] == '2024']

    filtered_rows = [];
    for row in new_rows:
        # Use dictionary comprehension to remove the unwanted columns
        if (row['current_club_domestic_competition_id'] in ['GB1' , 'IT1', 'ES1', 'FR1', 'L1']):
            filtered_row = {key: value for key, value in row.items() if key not in ['market_value_in_eur', 'foot', 'first_name', 'last_name' , 'last_season', 'city_of_birth', 'height_in_cm', 'contract_expiration_date', 'url', 'highest_market_value_in_eur', 'country_of_birth', 'date_of_birth', 'agent_name', 'current_club_domestic_competition_id', 'current_club_name']}
            filtered_rows.append(filtered_row)

# Open a new JSON file for writing
with open('Filtered-Data-20242025/players.json', mode='w', encoding='utf-8') as jsonfile:
    # Write the filtered rows to the JSON file
    json.dump(filtered_rows, jsonfile, indent=4, ensure_ascii=False)  # 'indent=4' makes the JSON output readable

print("Filtered data has been saved to 'players.json'.")
