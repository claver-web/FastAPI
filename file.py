from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def get_pincode_data():
    with open("output.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    return JSONResponse(
        content={"error": "There is nothing to find at this path."},
        status_code=404
    )
