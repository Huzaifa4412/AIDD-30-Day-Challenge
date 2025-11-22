from pypdf import PdfReader

def extract_text(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file: The PDF file object.

    Returns:
        The extracted text as a string.
    """
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
