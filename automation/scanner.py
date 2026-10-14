import json
from pathlib import Path
from datetime import datetime, timezone

DATA = Path("data/verified_jobs.json")

def main():
    jobs = json.loads(DATA.read_text(encoding="utf-8"))

    if not isinstance(jobs, list):
        raise ValueError("Expected a JSON array")

    print("Kera Jobs Automatic Scanner")
    print("Time:", datetime.now(timezone.utc).isoformat())
    print("Existing jobs:", len(jobs))
    print("Status: Workflow ready; source adapters pending")
    print("No unverified vacancies will be published.")

if __name__ == "__main__":
    main()
