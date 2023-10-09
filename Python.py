import csv

# Specify the CSV file containing campaign data
csv_file_name = "servey.csv"

# Create an empty list to store the campaign data
campaign_data = []

# Read data from the CSV file
with open(servey.csv, mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        campaign_data.append(row)

# Display the campaign data
for campaign in campaign_data:
    print(f"Topic: {campaign['public']}, Message: {campaign['Right to vote']}")
