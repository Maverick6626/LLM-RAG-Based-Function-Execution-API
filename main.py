from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from function_retrieval import perform_query
from mappings import mappings
from session_handling import fetch_session, store_session
import inspect

# FastAPI App
app = FastAPI()

# Data Validation
class ExecuteRequest(BaseModel):
    session_id: str
    prompt: str
    run: bool = False

# API Endpoint
@app.post("/execute")
def execute_command(query: ExecuteRequest):
    try:
        # Fetch the session history
        history_text = fetch_session(query.session_id, query.prompt)
        combined_prompt = history_text + ' ' + query.prompt

        # Perform the query
        result = perform_query(combined_prompt)

        # Get the code snippet
        code_snippet = inspect.getsource(mappings[result])
        return_dict = {"function": result, "code snippet": code_snippet}

        # Execute the function if run is True
        if query.run:
            if result in ['cpu_usage', 'memory_usage', 'disk_usage', 'use_powershell']:
                mappings[result](return_dict)
            else:
                mappings[result]()

        # Store the session history
        store_session(query.session_id, query.prompt)

        return return_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))