from __future__ import annotations

import json
from pathlib import Path


def load_nsrdb_hourly_json(path: str | Path) -> tuple[dict, list[float]]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return payload["hourly"], payload["monthly_albedo"]
