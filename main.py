from chunking import chunk_pdf
from embedder import embed_text
from similiarity import calculate_similarity

chunks = chunk_pdf("CL_DAV_Rules.pdf",600)
pdf_embeddings = embed_text(chunks)
question="what are the library rules?"
question_embedding = embed_text(question)

similarity_score = []
highest_score_index = 0
highest_score = 0
for i in range(0,len(pdf_embeddings)):
    score = calculate_similarity(question_embedding,pdf_embeddings[i])
    similarity_score.append(score)
    if(score > highest_score):
        highest_score = score
        highest_score_index = i

# print(chunks)
print(f"highest score was {highest_score} and highest score chunk was chunk no.{highest_score_index} and chunk content was {chunks[highest_score_index]}")
# print(similarity_score[:10])
