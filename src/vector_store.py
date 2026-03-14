import pandas as pd
import faiss
from src.embeddings import generate_embedding

class VectorDB:

    def __init__(self):
        self.index = None
        self.texts = []

    def build(self, path):

        df = pd.read_csv(path)

        self.texts = df["content"].tolist()

        embeddings = generate_embedding(self.texts)

        dimension = len(embeddings[0])

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

    def search(self, query):

        query_embedding = generate_embedding([query])

        distances, indices = self.index.search(query_embedding, 3)

        results = []

        for i in indices[0]:
            results.append(self.texts[i])

        return " ".join(results)