from src.vector_store import VectorDB

db = VectorDB()
db.build("data/finance_dataset.csv")

def get_context(topic):

    return db.search(topic)