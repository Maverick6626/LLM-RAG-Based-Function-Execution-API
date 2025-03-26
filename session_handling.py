from uuid import uuid1 # For generating unique id
import chromadb

# Create a persistent client for session history
chroma_client = chromadb.PersistentClient(path="./chroma_db")
session_history = chroma_client.get_or_create_collection(name="session_memory")

# Fetch session history with threshold distance <= 0.5
def fetch_session(session_id: str, prompt: str) -> str:
    results = session_history.query(
        query_texts=[prompt],
        where={"session_id": session_id}
    )
    history = ""

    # No previous session found; return empty history
    if not results['ids'] or not results['ids'][0]:
        return history
    
    # Fetch history with distance <= 0.5
    result_size = len(results['ids'])
    for idx in range(result_size):
        if results['distances'][0][idx] > 0.5:
            break
        history += results['documents'][idx][0] + " "

    return history

# Store session history
def store_session(session_id: str, prompt: str):
    unique_id = f"{session_id}_{uuid1()}" # Unique id for each session

    # Add the prompt to the session history
    session_history.add(
        documents=[prompt],
        metadatas=[{"session_id": session_id}],
        ids=[unique_id]
    )

# Test run
if __name__=='__main__':
    store_session_history("123", "open chrome", "open_chrome")
    print(fetch_session_history("123", 'open chrome'))
