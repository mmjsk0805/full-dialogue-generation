from bs4 import BeautifulSoup
import pandas as pd

html_path = "dialogues/dialogue1.html" 
output_csv = "dialogues/parsed_dialogue.csv"

def extract_dialogue_from_html(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    patient_lines = [p.get_text(strip=True) for p in soup.find_all("textarea", {"name": "patient[]"})]
    therapist_lines = [t.get_text(strip=True) for t in soup.find_all("textarea", {"name": "therapist[]"})]

    # Ensure lengths match
    min_len = min(len(patient_lines), len(therapist_lines))
    pairs = list(zip(patient_lines[:min_len], therapist_lines[:min_len]))

    df = pd.DataFrame(pairs, columns=["Patient", "Therapist"])
    return df

if __name__ == "__main__":
    df = extract_dialogue_from_html(html_path)
    df.to_csv(output_csv, index=False)
    print(f"✅ Extracted {len(df)} dialogue pairs to {output_csv}")
