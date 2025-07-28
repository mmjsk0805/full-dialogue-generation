import csv
import os
from datetime import datetime

def save_to_csv(turns, output_dir="output"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate a timestamped filename
    filename = os.path.join(output_dir, f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

    # Write the list of dialogue turns to CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["speaker", "utterance"])
        writer.writeheader()
        writer.writerows(turns)

    # Return the file path for reference
    return filename
