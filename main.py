from chunking import chunk_doc
from ingestion import load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
from preprocessor import retrieve_text
from embedder import embed_text
from similiarity import calculate_similarity


cleaned_text = retrieve_text("data/CL_DAV_Rules.pdf")
raw_text = load_pdf("data/CL_DAV_Rules.pdf")
cleaned_chunks = chunk_doc(cleaned_text)

embeddings = embed_text(cleaned_chunks)
question = input("Enter your Question:")
embedded_question = embed_text(question)

similiarity_list = []
highest_score = 0
highest_score_chunk_index = 0
for chunk in range(len(cleaned_chunks)):
    score=calculate_similarity(embeddings[chunk],embedded_question)
    similiarity_list.extend(score)
    if score>highest_score:
        highest_score = score
        highest_score_chunk_index = chunk
print(f"max vector similarity :{max(similiarity_list)}")
print(f"best chunk is at index {highest_score_chunk_index}")
print(f"while the best chunk itself is : {cleaned_chunks[highest_score_chunk_index]}")
