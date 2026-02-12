from __future__ import annotations

import json
from pathlib import Path


def load_metar_hourly_json(path: str | Path) -> dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return payload["hourly"]
