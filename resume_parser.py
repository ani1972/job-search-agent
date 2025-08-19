def parse_resume(resume_path):
    """
    Minimal resume parser.
    For now just return hardcoded text (later we can add real PDF/DOCX parsing).
    """
    return """
    Experienced Python Developer with skills in data analysis, machine learning, and AI projects.
    Familiar with Flask, SQL, and automation frameworks.
    """


'''import PyPDF2


def parse_resume(resume_path):
    text = ""
    with open(resume_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text'''
