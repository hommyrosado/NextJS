import csv
from pathlib import Path
from datetime import datetime, UTC

DATA_FILE = Path("data/youtube_daily_metrics.csv")

HEADERS = [
    "timestamp",
    "date",
    "hour",
    "channel_name",
    "channel_id",
    "subscribers",
    "total_views",
    "total_videos",
    "uploads_last_24h",
    "uploads_last_7d",
    "uploads_last_30d"
]


def save_metrics(rows):

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    file_exists = DATA_FILE.exists()

    now = datetime.now(UTC)

    timestamp = now.isoformat()
    date = now.date().isoformat()
    hour = now.hour

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=HEADERS)

        if not file_exists:
            writer.writeheader()

        for row in rows:

            output_row = {
                "timestamp": timestamp,
                "date": date,
                "hour": hour,
                "channel_name": row["channel_name"],
                "channel_id": row["channel_id"],
                "subscribers": row["subscribers"],
                "total_views": row["total_views"],
                "total_videos": row["total_videos"],
                "uploads_last_24h": row["uploads_last_24h"],
                "uploads_last_7d": row["uploads_last_7d"],
                "uploads_last_30d": row["uploads_last_30d"]
            }

            writer.writerow(output_row)

    print("CSV updated:", DATA_FILE)