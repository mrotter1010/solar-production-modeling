from __future__ import annotations

from datetime import datetime, timedelta


def build_hourly_index(year: int) -> list[datetime]:
    """Return deterministic non-leap-year hourly index (8760 rows)."""
    start = datetime(year, 1, 1, 0, 0)
    current = start
    out: list[datetime] = []
    while current.year == year:
        if not (current.month == 2 and current.day == 29):
            out.append(current)
        current += timedelta(hours=1)
    if len(out) != 8760:
        raise ValueError(f"Expected 8760 timestamps, found {len(out)}")
    return out
