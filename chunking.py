import fitz
from embedder import embed_text
from sklearn.metrics.pairwise import cosine_similarity
pdf = fitz.open("CL_DAV_Rules.pdf")

# print(pdf[0].get_text())
full_text=""
chunk_size=500
chunks=[]

for page_number in range(len(pdf)):
    text=pdf[page_number].get_text()
    full_text+=text

for i in range(0,len(full_text),chunk_size):
    chunk=full_text[i:i+chunk_size]
    clean_chunk = chunk.replace("\n","")
    chunks.append(clean_chunk)

embeddings = embed_text(chunks)
print(embeddings[:10])

