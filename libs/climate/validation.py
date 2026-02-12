from __future__ import annotations

from collections.abc import Iterable

REQUIRED_FIELDS = ("Year", "Month", "Day", "Hour", "GHI", "DNI", "DHI", "Tdry")


def validate_monthly_albedo(monthly_albedo: Iterable[float]) -> list[float]:
    values = list(monthly_albedo)
    if len(values) != 12:
        raise ValueError(f"monthly_albedo must contain exactly 12 values; received {len(values)}")
    return values


def validate_required_non_null(rows: list[dict[str, float | int]]) -> None:
    for idx, row in enumerate(rows):
        for field in REQUIRED_FIELDS:
            if row.get(field) is None:
                raise ValueError(f"Missing required field {field} at row index {idx}")


def validate_8760(rows: list[dict[str, float | int]]) -> None:
    if len(rows) != 8760:
        raise ValueError(f"Expected 8760 rows, found {len(rows)}")
