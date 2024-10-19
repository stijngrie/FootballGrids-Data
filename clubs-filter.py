import csv
import json
import top_clubs

# Open the CSV file
with open('Raw-Data-20242025\clubs.csv', mode='r', encoding='utf-8') as file:
    # Create a DictReader object
    clubsfile = csv.DictReader(file)

    # Loop over each row in the CSV
    # Filter out rows where 'last_season' is not equal to 2024
    new_rows = [row for row in clubsfile if row['last_season'] == '2024']

    filtered_rows = []
    for row in new_rows:
        # Use dictionary comprehension to remove the unwanted columns
        if (int(row['club_id']) in top_clubs.clubs):
            filtered_row = {key: value for key, value in row.items() if key not in ['stadium_seats', 'national_team_players', 'last_season', 'stadium_name',
                                                                                    'foreigners_number', 'average_age', 'total_market_value', 'foreigners_percentage', 'coach_name', 'net_transfer_record', 'squad_size', 'filename', 'domestic_competition_id']}
            filtered_rows.append(filtered_row)

# Open a new JSON file for writing
with open('Filtered-Data-20242025/clubs.json', mode='w', encoding='utf-8') as jsonfile:
    # Write the filtered rows to the JSON file
    # 'indent=4' makes the JSON output readable
    json.dump(filtered_rows, jsonfile, indent=4, ensure_ascii=False)

print("Filtered data has been saved to 'clubs.json'.")
