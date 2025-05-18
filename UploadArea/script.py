from docx import Document

def read_docx(uploaded_file):
    document = Document(uploaded_file)
    content = []
    for para in document.paragraphs:
        content.append({
            "text": para.text,
            "style": para.style.name  # Useful if already styled!
        })
    return content