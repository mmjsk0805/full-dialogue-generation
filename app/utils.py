import PyPDF2
import io

def extract_text_from_pdf(file_bytes) -> str:
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def format_prompt(chapter_text: str, starter_dialogue: str) -> str:
    return f"""Use the following therapy manual chapter and starter dialogue to continue a realistic patient-therapist conversation.

### Therapy Manual:
{chapter_text}

### Starter Dialogue:
{starter_dialogue}

### Continue the dialogue:
"""
