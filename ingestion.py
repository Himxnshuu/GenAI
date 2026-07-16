import fitz

def load_pdf(file_path):
    if not file_path:
        return "No file path given"

    pdf = fitz.open(file_path)

    pages = []

    for page_number,page in enumerate(pdf):
        pages.append(
            {
                "page": page_number,
                "content":page.get_text()
            }
        )
    pdf.close()

    return pages

    
