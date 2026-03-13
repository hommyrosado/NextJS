import requests
import json
from datetime import datetime, timedelta, UTC

CHANNELS_URL = "https://www.googleapis.com/youtube/v3/channels"
PLAYLIST_URL = "https://www.googleapis.com/youtube/v3/playlistItems"


def collect_channel_metrics(channel_id, api_key):

    now = datetime.now(UTC)

    day_24h = now - timedelta(hours=24)
    week = now - timedelta(days=7)
    month = now - timedelta(days=30)

    params = {
        "part": "statistics,snippet,contentDetails",
        "id": channel_id,
        "key": api_key
    }

    r = requests.get(CHANNELS_URL, params=params)
    data = r.json()

    if not data.get("items"):
        return None

    item = data["items"][0]

    name = item["snippet"]["title"]
    subs = int(item["statistics"]["subscriberCount"])
    views = int(item["statistics"]["viewCount"])
    videos_total = int(item["statistics"]["videoCount"])

    uploads_playlist = item["contentDetails"]["relatedPlaylists"]["uploads"]

    videos = []
    next_page = None

    while True:

        params = {
            "part": "snippet",
            "playlistId": uploads_playlist,
            "maxResults": 50,
            "key": api_key
        }

        if next_page:
            params["pageToken"] = next_page

        r = requests.get(PLAYLIST_URL, params=params)
        data = r.json()

        for video in data.get("items", []):

            published = datetime.fromisoformat(
                video["snippet"]["publishedAt"].replace("Z", "+00:00")
            )

            if published < month:
                break

            videos.append(video)

        next_page = data.get("nextPageToken")

        if not next_page:
            break

    count_24h = sum(
        1 for v in videos
        if datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z","+00:00")) > day_24h
    )

    count_week = sum(
        1 for v in videos
        if datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z","+00:00")) > week
    )

    count_month = sum(
        1 for v in videos
        if datetime.fromisoformat(v["snippet"]["publishedAt"].replace("Z","+00:00")) > month
    )

    return {
        "channel_name": name,
        "channel_id": channel_id,
        "subscribers": subs,
        "total_views": views,
        "total_videos": videos_total,
        "uploads_last_24h": count_24h,
        "uploads_last_7d": count_week,
        "uploads_last_30d": count_month
    }