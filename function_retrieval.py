import chromadb
from chromadb.utils import embedding_functions

# Define the documents and ids
documents = ['open chrome', 'open calculator', 'open notepad', 'cpu usage', 'memory usage', 'disk usage', 'use powershell'];
ids = ['open_chrome', 'open_calculator', 'open_notepad', 'cpu_usage', 'memory_usage', 'disk_usage', 'use_powershell']

# Create a client
chroma_client = chromadb.Client()

# Create a collection
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-MiniLM-L6-v2')
collection = chroma_client.create_collection(name='my_collection', embedding_function=sentence_transformer_ef)

# Add the documents to the collection
collection.add(
    documents=documents,
    ids=ids
)

# Perform a query
def perform_query(text: str):
    result = collection.query(
        query_texts=text,
        n_results=5
    )
    return result['ids'][0][0]

# Test run
if __name__=='__main__':
    query = 'open the google chrome'
    result = perform_query(query)
    print(result)