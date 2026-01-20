import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone, timedelta

SECRET = b"hello-there-from-b12"
URL = "https://b12.io/apply/submission"

timestamp = (
    datetime.now(timezone(timedelta(hours=1)))
    .astimezone(timezone.utc)
    .isoformat(timespec="milliseconds")
    .replace("+00:00", "Z")
)

payload = {
    "action_run_link": "REPLACE_ME_AFTER_FIRST_RUN",
    "email": "andrzejgrabowski815@gmail.com",
    "name": "Andrzej Grabowski",
    "repository_link": "https://github.com/andrzej-caresolace/b12_apply",
    "resume_link": "https://www.linkedin.com/in/andrzej-grabowski-76a0793a7/",
    "timestamp": timestamp,
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

signature = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}",
}

response = requests.post(URL, data=body, headers=headers)
response.raise_for_status()

print(response.json()["receipt"])
