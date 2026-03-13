import json
from collectors.youtube_collector import collect_channel_metrics
from storage.csv_writer import save_metrics


# def run_collection(api_key):

#     with open("config/competitors.json") as f:
#         competitors = json.load(f)

#     results = []

#     for comp in competitors:

#         print("Collecting:", comp["name"])

#         data = collect_channel_metrics(
#             comp["channel_id"],
#             api_key
#         )

#         if data:
#             results.append(data)

#     save_metrics(results)

#     return results

def run_collection(api_key):

    with open("config/competitors.json") as f:
        competitors = json.load(f)

    results = []

    for comp in competitors:

        print("Collecting:", comp["name"])

        data = collect_channel_metrics(
            comp["channel_id"],
            api_key
        )

        if data:
            results.append(data)

    print("Collected results:", results)

    save_metrics(results)

    return results