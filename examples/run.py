# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/bluesky-community-finder").call(run_input={
    "mode": "starterPacks",
    "queries": [
        "journalists",
        "science"
    ],
    "maxItems": 30
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
