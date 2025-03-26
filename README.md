# LLM+RAG Function Execution API

This project is a **FastAPI-based API** that enables function execution using **retrieval-augmented generation (RAG)**. It employs **ChromaDB** for function retrieval and session-based memory, allowing users to execute predefined automation commands like opening applications, checking system resource usage, and running PowerShell commands.

## Features

- **Retrieval-based function execution** using ChromaDB.
- **Session-based memory** for contextual understanding.
- **FastAPI-based API** for easy integration.
- **Predefined automation functions** (open applications, check system status, run PowerShell commands).
- **Custom function execution** with optional runtime execution.

## Installation

### Prerequisites

- Python 3.8+
- pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the API

```bash
uvicorn main:app --reload
```

### API Endpoint

#### Execute Function

- **Endpoint:** `POST /execute`
- **Request Body:**

```json
{
  "session_id": "12345",
  "prompt": "open chrome",
  "run": true
}
```

- **Response:**

```json
{
  "function": "open_chrome",
  "code snippet": "def open_chrome(): ..."
}
```

## Project Structure

```
.
├── main.py                 # FastAPI application
├── session_handling.py      # Session-based memory using ChromaDB
├── function_retrieval.py    # Function retrieval using embedding-based search
├── automation_functions.py  # Automation functions (open apps, check system usage, etc.)
├── mappings.py              # Maps retrieved function IDs to actual functions
├── requirements.txt         # Project dependencies
```

## How It Works

1. **Session Handling**: The API stores past prompts in **ChromaDB** with a unique session ID.
2. **Function Retrieval**: The system retrieves the most relevant function based on the given prompt using **embedding-based search**.
3. **Function Execution**: If `run=true`, the retrieved function executes and returns the results.
4. **Response**: The API returns the function name and its source code.

## Example Test Run

```python
import requests

url = "http://127.0.0.1:8000/execute"
data = {"session_id": "12345", "prompt": "open chrome", "run": true}
response = requests.post(url, json=data)
print(response.json())
```
