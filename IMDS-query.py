import sys
import requests

BASE_URL = "http://metadata.google.internal/computeMetadata/v1/"
HEADERS = {"Metadata-Flavor": "Google"}

endpoint = sys.argv[1] if len(sys.argv) > 1 else ""
url = BASE_URL + endpoint

response = requests.get(url, headers=HEADERS, timeout=5)
print(f"Status: {response.status_code}")
print(response.text)
