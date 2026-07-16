from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

def chunk_doc(processed_text):
    cleaned_chunks = []

    for content in processed_text:
        chunk = text_splitter.split_text(content)

        cleaned_chunks.extend(chunk) 

    return cleaned_chunks




