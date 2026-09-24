import os
from fastapi import FastAPI

app = FastAPI()

INSTANCE = os.getenv("INSTANCE", "unknown")

@app.get("/")
def hello():
    return {"message": f"Hello from FastAPI {INSTANCE}"}

@app.get("/health")
def health():
    return {"status": "ok"}