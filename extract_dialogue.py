from bs4 import BeautifulSoup
import pandas as pd

# Path to the input HTML file and output CSV
html_path = "dialogues/dialogue1.html" 
output_csv = "dialogues/parsed_dialogue.csv"

def extract_dialogue_from_html(html_file):
    # Read and parse the HTML file using BeautifulSoup
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Extract all <textarea> values with name="patient[]" and name="therapist[]"
    patient_lines = [p.get_text(strip=True) for p in soup.find_all("textarea", {"name": "patient[]"})]
    therapist_lines = [t.get_text(strip=True) for t in soup.find_all("textarea", {"name": "therapist[]"})]

    # Match up the lines by index (truncate to shortest list to avoid mismatch)
    min_len = min(len(patient_lines), len(therapist_lines))
    pairs = list(zip(patient_lines[:min_len], therapist_lines[:min_len]))

    # Convert to a DataFrame with appropriate column names
    df = pd.DataFrame(pairs, columns=["Patient", "Therapist"])
    return df

if __name__ == "__main__":
    # Run the extraction and save to CSV
    df = extract_dialogue_from_html(html_path)
    df.to_csv(output_csv, index=False)
    print(f"✅ Extracted {len(df)} dialogue pairs to {output_csv}")
