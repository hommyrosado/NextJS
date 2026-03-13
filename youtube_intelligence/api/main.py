import pandas as pd
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from services.metrics_service import run_collection

app = FastAPI()

API_KEY = open("sample.txt").read().strip()

@app.get("/")
def root():
    return RedirectResponse("/app/")

@app.get("/status")
def status():
    return {"status": "YouTube Intelligence API running"}

@app.get("/collect")
def collect_metrics():
    results = run_collection(API_KEY)
    return results

@app.get("/metrics")
def get_metrics():

    columns = [
        "timestamp",
        "date",
        "hour",
        "channel_name",
        "channel_id",
        "subscribers",
        "total_views",
        "video_count",
        "videos_last_24h",
        "videos_last_7d",
        "videos_last_30d"
    ]

    df = pd.read_csv("data/youtube_daily_metrics.csv", names=columns)

    return df.to_dict(orient="records")
# Serve frontend SPA
app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")