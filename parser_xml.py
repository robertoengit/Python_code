import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML file
tree = ET.parse('export.xml')
root = tree.getroot()

# Create a list to store running data
running_data = []

# Iterate through each record in the XML
for record in root.findall('Record'):
    if record.attrib['type'] == 'HKQuantityTypeIdentifierDistanceWalkingRunning':
        # Extract relevant attributes
        start_date = record.attrib['startDate']
        end_date = record.attrib['endDate']
        distance = record.attrib['value']
        
        # Append to running_data list
        running_data.append({
            'start_date': start_date,
            'end_date': end_date,
            'distance_km': float(distance) / 1000  # Convert meters to kilometers
        })

# Convert the running_data list to a DataFrame
df = pd.DataFrame(running_data)

# Save the DataFrame to a CSV file
df.to_csv('running_data.csv', index=False)

print("Running data extracted and saved to running_data.csv")