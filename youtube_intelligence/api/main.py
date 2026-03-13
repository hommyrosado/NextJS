from fastapi import FastAPI
from services.metrics_service import run_collection

app = FastAPI()

API_KEY = open("sample.txt").read().strip()


@app.get("/")
def home():
    return {"status": "YouTube Intelligence API running"}


@app.get("/collect")
def collect_metrics():
    results = run_collection(API_KEY)
    return results