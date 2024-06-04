import csv
import json

# Define input and output filenames
csv_filename = "fear.csv"
json_filename = "fear.json"

# Open CSV file for reading and JSON file for writing
with open(csv_filename, "r") as csvfile, open(json_filename, "w") as jsonfile:
  # Create a CSV reader object
  csv_reader = csv.DictReader(csvfile)

  # Create an empty list to store video data
  data = []

  # Loop through each row in the CSV file
  for row in csv_reader:
    # Add a dictionary to the data list with video information from each row
    data.append({
      "link": row["link"],
      "title": row["title"],
      "author": row["author"],
      "video_id": row["video_id"],
    })

  # Write the data list to the JSON file with indentation
  json.dump(data, jsonfile, indent=4)

print(f"CSV data converted to JSON and saved to {json_filename}")
