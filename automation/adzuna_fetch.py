import os
import json
import urllib.parse
import urllib.request
from pathlib import Path

app_id = os.environ.get("ADZUNA_APP_ID")
app_key = os.environ.get("ADZUNA_APP_KEY")

if not app_id or not app_key:
    raise SystemExit("Missing Adzuna credentials")

params = urllib.parse.urlencode({
    "app_id": app_id,
    "app_key": app_key,
    "results_per_page": 20,
    "where": "Kerala",
    "content-type": "application/json"
})

url = "https://api.adzuna.com/v1/api/jobs/in/search/1?" + params

request = urllib.request.Request(
    url,
    headers={"Accept": "application/json"}
)

with urllib.request.urlopen(request, timeout=30) as response:
    data = json.load(response)

jobs = []

for job in data.get("results", []):
    jobs.append({
        "source": "Adzuna",
        "id": str(job.get("id", "")),
        "title": job.get("title", ""),
        "company": job.get("company", {}).get("display_name", ""),
        "location": job.get("location", {}).get("display_name", ""),
        "url": job.get("redirect_url", ""),
        "status": "needs_review"
    })

output = Path("data/adzuna_candidates.json")
output.write_text(
    json.dumps(jobs, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print("Adzuna candidates:", len(jobs))
print("Saved:", output)
