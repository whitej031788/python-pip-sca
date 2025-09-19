import requests
from typing import Any, Dict

DEFAULT_TIMEOUT = (3.05, 5)


def fetch_json(url: str, timeout=DEFAULT_TIMEOUT) -> Dict[str, Any]:
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.json()
