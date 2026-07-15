import fitz

def chunk_pdf(pdf_path:str,chunk_size:int=500):
    pdf = fitz.open(pdf_path)

    # print(pdf[0].get_text())
    full_text=""
    chunks=[]

    for page_number in range(len(pdf)):
        text=pdf[page_number].get_text()
        full_text+=text

    for i in range(0,len(full_text),chunk_size):
        chunk=full_text[i:i+chunk_size]
        clean_chunk = chunk.replace("\n","")
        chunks.append(clean_chunk)

    return chunks

