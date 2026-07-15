from sklearn.metrics.pairwise import cosine_similarity
# from chunking.py import chunk_pd
# from embedder.py import embed_text

# question

def calculate_similarity(question,chunk):

    similarity = cosine_similarity([question],[chunk])

    return similarity