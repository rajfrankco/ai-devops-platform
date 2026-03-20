from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)

memory = []

def store(log, solution):
    emb = model.encode([log])
    index.add(np.array(emb))
    memory.append((log, solution))

def search(log):
    if len(memory) == 0:
        return None
    emb = model.encode([log])
    D, I = index.search(np.array(emb), k=1)
    return memory[I[0][0]]