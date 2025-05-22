from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load the JSON once at startup (faster, safer)
@app.on_event("startup")
def load_json_data():
    global data
    try:
        with open("output.json", "r") as file:
            data = json.load(file)
    except Exception as e:
        data = {"error": f"Failed to load data: {str(e)}"}

@app.get("/")
def get_pincode_data():
    return data

# Catch-all route
@app.get("/{full_path:path}")
def catch_all(full_path: str):
    return JSONResponse(
        content={"error": "There is nothing to find at this path."},
        status_code=404
    )
